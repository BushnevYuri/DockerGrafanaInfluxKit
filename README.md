# [WIP] Docker Grafana, InfluxDb & SonarQube Client

* Start up
```
# docker-compose build
# docker-compose up -d
```

* Stop
```
# docker-compose down
```

* Container debug
```
# docker ps 
# docker exec -it [CONTAINER_ID] bash
```

* Backup
```
# docker-compose --down
#
# INFLUXDB_VOLUME_NAME="<VOLUME_PATH>_influxdb_data"
# GRAFANA_VOLUME_NAME="<VOLUME_PATH>_grafana_data"
# DATE=`date '+%d%m%Y-%H%M%S'`
#
# echo "Backup InfluxDb"
# docker run --rm -t -v ${INFLUXDB_VOLUME_NAME}:/volume -v $(pwd):/backup debian tar czvf /backup/${INFLUXDB_VOLUME_NAME}_${DATE}.tar.gz /volume/
# echo "Backup Grafana"
# docker run --rm -t -v ${GRAFANA_VOLUME_NAME}:/volume -v $(pwd):/backup debian tar czvf /backup/${GRAFANA_VOLUME_NAME}_${DATE}.tar.gz /volume/
#
# docker-compose up --build
```

* Restore
```
# docker-compose --down
#
# INFLUXDB_VOLUME_NAME="<VOLUME_PATH>_influxdb_data"
# GRAFANA_VOLUME_NAME="<VOLUME_PATH>_grafana_data"
# DATE=`date '+%d%m%Y-%H%M%S'`
#
# echo "Restore InfluxDb backup"
# docker run --rm -it -v ${INFLUXDB_VOLUME_NAME}:/volume -v $(pwd):/backup debian bash
rm -rf /volume/*
tar xvzf /backup/<INFLUXDB_DB_BACKUP>
exit
#
# echo "Restore Grafana"
# docker run --rm -it -v ${GRAFANA_VOLUME_NAME}:/volume -v $(pwd):/backup debian bash
rm -rf /volume/*
tar xvzf /backup/<GRAFANA_BACKUP>
exit
#
# docker-compose up --build
```


Reference:

- https://github.com/BushnevYuri/DockerGrafanaInfluxKit
- https://github.com/multiservicio/sonarqube-exporter
