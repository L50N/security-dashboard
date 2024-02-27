#!/bin/bash

#+------------------------------------------------+
#|    This restart script was made by L5ONdev     |
#|   https://github.com/l50n/security-dashboard   |
#|             Version: SNAPSHOT-1.0              |
#+------------------------------------------------+

## Prefix variable
PREFIX='[SecurityDashboard]'

## Checking, if the Dashboard was already installed
if [[ -d "/etc/sec-dashboard" ]]; then
  ## Restarting the Docker Compose
  echo "$PREFIX" "We restart the MariaDB server and the frontend..."
  docker-compose down /etc/sec-dashboard/docker-compose.yml
  docker-compose up -d /etc/sec-dashboard/docker-compose.yml

  ## Restarting the backend
  echo "$PREFIX" "We have completed that. Now the backend will be restarted..."
  pkill -f "dashboard"
  screen -dmS backend python3 /etc/sec-dashboard/backend/app.py

  ## Finished
  echo "$PREFIX" "Your dashboard has now been restarted... Take a look at https://localhost:3000."
  else
    echo "$PREFIX" "We could not recognize your installation."
fi