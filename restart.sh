#!/bin/bash

#+------------------------------------------------+
#|    This restart script was made by L5ONdev     |
#|   https://github.com/l50n/security-dashboard   |
#|             Version: SNAPSHOT-1.0              |
#+------------------------------------------------+

# Prefix variable
PREFIX='[SecurityDashboard]'

# Function to display error message and exit
error_exit() {
    echo "$PREFIX ERROR: $1" >&2
    exit 1
}

# Check if the Dashboard directory exists
if [[ ! -d "/etc/sec-dashboard" ]]; then
  error_exit "Dashboard installation directory not found."
fi

# Restart Docker Compose services
echo "$PREFIX Restarting MariaDB server and frontend..."
docker-compose down -f /etc/sec-dashboard/docker-compose.yml || error_exit "Failed to stop Docker services."
docker-compose up -d -f /etc/sec-dashboard/docker-compose.yml || error_exit "Failed to start Docker services."

# Restart the backend
echo "$PREFIX Restarting backend..."
pkill -f "dashboard" || error_exit "Failed to stop backend process."
sleep 8
screen -dmS backend python3 /etc/sec-dashboard/backend/app.py || error_exit "Failed to start backend."

# Finished
echo "$PREFIX Your dashboard has been restarted. Visit https://localhost:3000."
