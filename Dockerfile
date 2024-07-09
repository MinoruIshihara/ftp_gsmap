FROM python:3.10.13-slim-bullseye

COPY ./src/sync_files /usr/sbin/sync_files
COPY ./src/inpainting /usr/sbin/inpainting
COPY ./settings.json /etc/ftp_gsmap.settings.json

RUN pip install numpy Pillow opencv-python matplotlib netCDF4

RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev

WORKDIR /usr/local/src