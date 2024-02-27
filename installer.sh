#!/bin/bash

#+------------------------------------------------+
#|       This installer was made by L5ONdev       |
#|   https://github.com/l50n/security-dashboard   |
#|             Version: SNAPSHOT-1.2              |
#+------------------------------------------------+

PREFIX='[SecurityDashboard]'

# Function to install required packages and Flask
install_dependencies() {
    echo "$PREFIX" "Installing dependencies and Flask..."
    if command -v yum &> /dev/null; then
        yum update && yum install -y python3 python3-pip mariadb-server ufw docker-ce docker-compose screen
    elif command -v apt-get &> /dev/null; then
        apt update && apt install -y python3 python3-pip mysql-server ufw docker-ce docker-compose screen
    elif command -v dnf &> /dev/null; then
        dnf update && dnf install -y python3 python3-pip mariadb-server ufw docker-ce docker-compose screen
    else
        echo "$PREFIX" "We could not recognize your package manager."
        exit 1
    fi

    # Install Flask and other Python packages
    python3 -m pip install --user flask flask-cors Flask-Limiter PyMySQL PyYAML
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
}

# Function to start services
start_services() {
    echo "$PREFIX" "Starting services..."
    docker-compose -f /etc/sec-dashboard/docker-compose.yml up -d

    # Start the backend in a detached screen session
    screen -dmS backend python3 /etc/sec-dashboard/backend/app.py
}

# Function to add script to autostart
configure_autostart() {
    START_SCRIPT="/etc/sec-dashboard/start_dashboard.sh"
    echo "$PREFIX" "Configuring autostart..."

    cat > "$START_SCRIPT" <<EOF
#!/bin/bash
sleep 20
cd /etc/sec-dashboard/
docker-compose -f docker-compose.yml up -d
screen -dmS backend python3 /etc/sec-dashboard/backend/app.py
EOF

    chmod +x "$START_SCRIPT"

    if [[ -f /etc/rc.local ]]; then
        # Add the script to /etc/rc.local for backward compatibility
        sed -i '/^exit 0/d' /etc/rc.local
        echo "$START_SCRIPT" >> /etc/rc.local
        echo "exit 0" >> /etc/rc.local
    else
        # Add the script to systemd
        cat > /etc/systemd/system/security-dashboard.service <<EOF
[Unit]
Description=Security Dashboard
After=network.target

[Service]
Type=simple
ExecStart=/bin/bash $START_SCRIPT
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

        systemctl daemon-reload
        systemctl enable security-dashboard.service
    fi

    echo "$PREFIX" "Autostart configured."
}

# Main function
main() {
    clear
    install_dependencies
    configure_ufw
    copy_files
    start_services
    configure_autostart

    # Prompt to change passwords
    echo "$PREFIX" "You should change your password IMMEDIATELY."
    echo "$PREFIX" "You can do this by opening /etc/sec-dashboard/docker-compose.yml"
    echo "$PREFIX" "and changing the MariaDB server password data there."
    echo "$PREFIX" "Then, update the data in /etc/sec-dashboard/backend/app.py as well."
}

main
