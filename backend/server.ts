import * as express from 'express';
import * as bodyParser from 'body-parser';
import * as session from 'express-session';
import * as mysql from 'mysql';
import * as fs from 'fs';
import { safeLoad, safeDump } from 'js-yaml';
import * as path from 'path';
import cors from 'cors';
import { Limiter } from 'express-rate-limit';
import { generate } from 'randomstring';

const app = express();
app.use(bodyParser.json());
app.use(cors({ credentials: true, origin: true }));

const limiter = new Limiter({
  windowMs: 60 * 1000, // 1 minute
  max: 3,
  keyGenerator: (req) => req.ip,
});
app.use(limiter);

const sessionDir = path.join(__dirname, 'sessions');
if (!fs.existsSync(sessionDir)) {
  fs.mkdirSync(sessionDir);
}

const secretKeyFilePath = './backend/secret_key.yml';
const secretKey = fs.existsSync(secretKeyFilePath)
  ? safeLoad(fs.readFileSync(secretKeyFilePath, 'utf8'))['SECRET_KEY']
  : generate({ length: 16, charset: 'alphanumeric' });

fs.writeFileSync(secretKeyFilePath, safeDump({ SECRET_KEY: secretKey }));

const pool = mysql.createPool({
  host: process.env.MYSQL_HOST || '127.0.0.1',
  port: parseInt(process.env.MYSQL_PORT) || 3307,
  user: process.env.MYSQL_USER || 'root',
  password: process.env.MYSQL_PASSWORD || 'default',
  database: process.env.MYSQL_DB || 'default',
});

const createTestUsers = () => {
  pool.getConnection((err, connection) => {
    if (err) throw err;
    connection.query("SHOW TABLES LIKE 'users'", (err, result) => {
      if (err) throw err;
      if (!result.length) {
        connection.query(`
          CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
          )
        `, (err) => {
          if (err) throw err;
          const defaultPassword = generate({ length: 8, charset: 'alphanumeric' });
          connection.query("INSERT INTO users (email, password) VALUES ? ", [
            [["first@example.com", defaultPassword], ["second@example.com", defaultPassword]]
          ], (err) => {
            if (err) throw err;
            connection.release();
          });
        });
      } else {
        connection.release();
      }
    });
  });
};

const isUserLoggedIn = (req: express.Request): boolean => {
  return !!req.session && !!req.session.user_id;
};

app.use(session({
  secret: secretKey,
  resave: false,
  saveUninitialized: true,
  cookie: { secure: false },
}));

app.get('/', (req, res) => {
  res.send('It works.');
});

app.post('/login', (req, res) => {
  const { email, password } = req.body;
  pool.query("SELECT id, email, password FROM users WHERE email = ?", [email], (err, results) => {
    if (err) throw err;
    if (results.length > 0) {
      const user = results[0];
      if (user.password === password) {
        req.session.user_id = user.id;
        console.log(`User logged in. User ID: ${user.id}`);
        res.status(200).json({ message: "200: The login was successful!" });
      } else {
        res.status(401).json({ message: "401: The user exists, but the password entered is incorrect!" });
      }
    } else {
      console.log("The user is not known to us.");
      res.status(401).json({ message: "401: The user is not known to us." });
    }
  });
});

app.get('/check-login', (req, res) => {
  if (isUserLoggedIn(req)) {
    res.status(200).json({ logged_in: true });
  } else {
    res.status(401).json({ logged_in: false });
  }
});

app.listen(3000, () => {
  createTestUsers();
  console.log('Server is running on port 3000');
});
