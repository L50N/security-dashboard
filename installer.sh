#!/bin/bash

PREFIX='[SecurityDashboard]'

#+------------------------------------------------+
#|       This installer was made by L5ONdev       |
#|   https://github.com/l50n/security-dashboard   |
#|             Version: SNAPSHOT-1.6              |
#+------------------------------------------------+

## TODO: - If directory already exists, ask user if he wants to remove dashboard - Hash passwords by default and print after installation. - test installation on centos and fedora

# Function to install required packages and Flask
install_dependencies() {
    echo "$PREFIX" "Installing dependencies and Flask..."
    if command -v yum &> /dev/null; then
        yum update && yum install -y python3 python3-pip mariadb-server ufw docker python3-setuptools pkg-config mysql-devel
        yum install -y docker-compose
        systemctl start docker
        systemctl enable docker
    elif command -v apt-get &> /dev/null; then
        apt update && apt install -y python3 python3-pip mysql-server ufw docker.io python3-setuptools pkg-config libmysqlclient-dev
        apt install -y docker-compose
        systemctl start docker
        systemctl enable docker
    elif command -v dnf &> /dev/null; then
        dnf update && dnf install -y python3 python3-pip mariadb-server ufw docker-ce python3-setuptools pkg-config mysql-devel
        dnf install -y docker-compose
        systemctl start docker
        systemctl enable docker
    else
        echo "$PREFIX" "We could not recognize your package manager."
        exit 1
    fi

    # Install Flask and other Python packages
    pip3 install --user flask==2.3.3 flask-cors Flask-Limiter PyMySQL PyYAML mysql-connector-python SQLAlchemy flask_mysqldb
}

# Function to configure UFW
configure_ufw() {
    if command -v ufw &>/dev/null; then
        echo "$PREFIX" "UFW is installed. Allowing specified ports..."
        ufw allow 3000
        ufw allow 5000
        ufw allow 3307
        ufw --force enable
    else
        echo "$PREFIX" "UFW is not installed. Skipping port configuration."
    fi
}

# Function to copy necessary files
copy_files() {
    echo "$PREFIX" "Copying necessary files..."
    mkdir -p /etc/sec-dashboard
    cp -r ./docker-compose.yml /etc/sec-dashboard
    cp -r ./backend /etc/sec-dashboard
    cp -r ./frontend /etc/sec-dashboard
    cp -r ./LICENSE /etc/sec-dashboard
    cp -r ./restart.sh /etc/sec-dashboard
}

# Function to start services
start_services() {
    echo "$PREFIX" "Starting services..."
    docker-compose -f /etc/sec-dashboard/docker-compose.yml up -d

    # Start the backend in a detached screen session
    sleep 8
    screen -dmS backend python3 /etc/sec-dashboard/backend/app.py
}

# Main function
main() {
    clear
    install_dependencies
    configure_ufw
    copy_files
    start_services

    # Prompt to change passwords
    echo "$PREFIX" "Thank you very much for your installation. Your dashboard should now run on http://localhost:3000."
}

main
