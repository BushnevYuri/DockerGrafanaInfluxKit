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
# INFLUXDB_VOLUME_NAME="<VOLUME_PATH>_influxdb_data"
# GRAFANA_VOLUME_NAME="<VOLUME_PATH>_grafana_data"
# DATE=`date '+%d%m%Y-%H%M%S'`
# docker run --rm -t -v ${INFLUXDB_VOLUME_NAME}:/volume -v $(pwd):/backup debian tar czvf /backup/${INFLUXDB_VOLUME_NAME}_\${DATE}.tar.gz /volume/
# docker run --rm -t -v ${GRAFANA_VOLUME_NAME}:/volume -v $(pwd):/backup debian tar czvf /backup/${GRAFANA_VOLUME_NAME}_\${DATE}.tar.gz /volume/
```


Reference:

- https://github.com/BushnevYuri/DockerGrafanaInfluxKit
- https://github.com/multiservicio/sonarqube-exporter
