FROM python:3.9.6

FROM mariadb:10.6.3

FROM mysql:8.0.26

FROM redis:latest

COPY loader_daemon.py /loader_daemon/loader_daemon.py

CMD [ "python3.9", "/loader_daemon/loader_daemon.py" ]