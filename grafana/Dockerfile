FROM grafana/grafana:5.3.2

USER root

RUN apt-get update \
	&& apt-get install -y -f curl gettext-base \
	&& rm -rf /var/lib/apt/lists/* 

WORKDIR /etc/grafana
COPY datasources ./datasources

WORKDIR /app
COPY entrypoint.sh ./
RUN chmod u+x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
