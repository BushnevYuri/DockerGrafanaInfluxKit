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

* Sonar Client

Setup:
```
# pip3 install -r pip requirements.txt
```
Start:
```
./sonar-client.py
```

* Container debug
```
# docker ps 
# docker exec -it [CONTAINER_ID] bash
```

Reference:

- https://github.com/BushnevYuri/DockerGrafanaInfluxKit
- https://github.com/multiservicio/sonarqube-exporter
