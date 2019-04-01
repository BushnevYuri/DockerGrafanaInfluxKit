FROM influxdb:1.5.4-alpine

WORKDIR /app
COPY entrypoint.sh ./
RUN chmod u+x entrypoint.sh
COPY influxdb.generated.conf /etc/influxdb/influxdb.conf

ENTRYPOINT ["/app/entrypoint.sh"]
