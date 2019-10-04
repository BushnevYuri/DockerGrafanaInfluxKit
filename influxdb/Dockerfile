FROM influxdb:1.7.8-alpine

WORKDIR /app
COPY entrypoint.sh ./

RUN chmod u+x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
