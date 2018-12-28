FROM alpine:3.7

ENV HTTPS_PROXY "http://172.25.1.1:3128"
ENV HTTP_PROXY "http://172.25.1.1:3128"

RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache


COPY crontab /etc/cron/crontab
RUN crontab /etc/cron/crontab

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY sonar-client.py ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "crond", "-f" ]
