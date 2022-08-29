#!/bin/bash
while true ; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
      break
    fi
    echo upgrade failed, retrying in 5 secs...
    sleep 5
done
flask seed
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app