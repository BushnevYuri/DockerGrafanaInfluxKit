#!/usr/bin/env sh

if [ ! -f "/var/lib/influxdb/.init" ]; then
    exec influxd $@ &

    until wget -q "http://localhost:${INFLUX_PORT}/ping" 2> /dev/null; do
        sleep 1
    done

    influx -host=0.0.0.0 -port=${INFLUX_PORT} -execute="CREATE USER ${INFLUX_USER} WITH PASSWORD '${INFLUX_PASSWORD}' WITH ALL PRIVILEGES"
    influx -host=0.0.0.0 -port=${INFLUX_PORT} -execute="CREATE DATABASE ${INFLUX_DB}"    
    
    ip add

    touch "/var/lib/influxdb/.init"

    kill -s TERM %1
fi

exec influxd $@
