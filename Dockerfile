FROM python:3.10.13-slim-bullseye

COPY ./src/sync_files /usr/sbin/sync_files
COPY ./settings.json /etc/ftp_gsmap.settings.json

WORKDIR /usr/local/src