C:\Users\User>curl -X POST -H "Content-Type: application/json" -d "{\"email\":\"leon@example.com\",\"password\":\"changeme\"}" http://localhost:5000/login
{
  "loggedIn": true,
  "message": "Login successful"
}

C:\Users\User>curl http://localhost:5000/check-login
{
  "loggedIn": false,
  "user": null
}