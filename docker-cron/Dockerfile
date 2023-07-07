FROM alpine:3.16

RUN apk add --update py3-pip
WORKDIR /app/

COPY . /app/
COPY crontab /var/spool/cron/crontabs/root

RUN chmod +x /app/app.py

CMD crond -l 2 -f
