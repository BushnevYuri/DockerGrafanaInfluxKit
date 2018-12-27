FROM grafana/grafana:5.3.2

USER root

WORKDIR /etc/grafana

COPY datasources ./datasources

WORKDIR /app
COPY entrypoint.sh ./
RUN chmod u+x entrypoint.sh

#USER grafana

ENTRYPOINT ["/app/entrypoint.sh"]
