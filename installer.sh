#!/bin/bash

#+------------------------------------------------+
#|       This installer was made by L5ONdev       |
#|   https://github.com/l50n/security-dashboard   |
#|             Version: SNAPSHOT-1.1              |
#+------------------------------------------------+

## Prefix variable
PREFIX='[SecurityDashboard]'

## Autostart variables
SCRIPT_DIR="/usr/local/bin"
START_COMMAND="cd /etc/sec-dashboard/ && docker-compose -f docker-compose.yml up -d && screen -dmS backend python3 /etc/sec-dashboard/backend/app.py"

## Empty the terminal to ensure a clean overview.
clear

## Check whether the script was loaded as root user.
if [ "$EUID" -ne 0 ]; then
  echo "$PREFIX" "Please run this installer as root."
  exit
fi

## Package manager detection and package names
if command -v yum &> /dev/null; then
    yum update && yum install -y python3 screen curl wget python3-pip
    clear
elif command -v apt-get &> /dev/null; then
    apt update && apt install -y python3 screen curl wget python3-pip
    clear
elif command -v dnf &> /dev/null; then
    dnf update && dnf install -y python3 screen curl wget python3-pip
    clear
else
    clear
    echo "$PREFIX" "We could not recognize your package manager."
    exit
fi

## Install Flask via PIP
pip install --user flask flask-cors Flask-Limiter PyMySQL PyYAML flask_mysqldb

## Creating directory where we can store our needed files
mkdir -p /etc/sec-dashboard
echo "$PREFIX" "'/etc/sec-dashboard' created, where the dashboard is saved."

## Install docker from https://get.docker.com/#
if ! command -v docker &>/dev/null; then
    echo "$PREIFX" "Docker is not installed. Proceeding with Docker installation..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    chmod +x ./get-docker.sh
    sudo bash ./get-docker.sh
fi

## Installing docker-compose from package manager
if command -v yum &> /dev/null; then
    yum install -y docker-compose
elif command -v apt-get &> /dev/null; then
    apt install -y docker-compose
elif command -v dnf &> /dev/null; then
    dnf install -y docker-compose
else
    echo "$PREFIX" "We could not recognize your package manager."
    exit
fi

## Copy some needed files to the project diretory...
cp -r ./docker-compose.yml /etc/sec-dashboard
cp -r ./backend /etc/sec-dashboard
cp -r ./frontend /etc/sec-dashboard
cp -r ./LICENSE /etc/sec-dashboard

## If UFW is installed, allow the user to open the ports.
if command -v ufw &>/dev/null; then
    clear
    read -p "$PREFIX" "We have detected that UFW is installed on your system. Would you like to allow ports 3000, 5000 and 3007? (y/n): " allow_ports

    case $allow_ports in
        [yY])
            # Allow specified ports
            ufw allow 3000
            ufw allow 5000
            ufw allow 3307
            ;;
        [nN])
            echo "$PREFIX" "Allowing ports via UFW is skipped"
            sleep 2
            ;;
        *)
            echo "$PREFIX" "Mhmm, your input is unknown to us - we'll skip this part."
            sleep 2
            ;;
    esac
fi

## Running the docker-compose to start MariaDB-Server and frontend.
docker-compose up -d /etc/sec-dashboard/docker-compose.yml

## Starting the backend via Python.
screen -dmS backend python3 /etc/sec-dashboard/backend/app.py
sleep 2
clear
echo "$PREFIX" "Here is your 'secret-key.yml' - you can find it in the backend."
cat /etc/sec-dashboard/backend/secret-key.yml

## Enabling autostart, if the user wants
read -p "$PREFIX" "Do you want to activate the dashboard automatically after logging into the system? (y/n): " enable_autostart
if [[ $enable_autostart =~ ^[yY](es)?$ ]]; then
  echo -e "#!/bin/bash\nsleep 20\n$START_COMMAND" > "$SCRIPT_DIR/start_dashboard.sh"
  chmod +x "$SCRIPT_DIR/start_dashboard.sh"
  echo "$SCRIPT_DIR/start_dashboard.sh" >> ~/.bash_profile
fi

## Information that the user should definitely change his passwords.
clear
echo "$PREFIX" "You should change your password IMMEDIATELY. You can do this by opening /etc/sec-dashboard/docker-compose.yml and changing the MariaDB server password data there and then telling the backend the new password by also changing the data in /etc/sec-dashboard/backend/app.py as you had changed it in docker-compose.yml!"
sleep 8

## Empty the installation directory
rm -rf *

exit
