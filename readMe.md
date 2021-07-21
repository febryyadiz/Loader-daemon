How to run the service:
1. clone the package from github
2. install python 3.9.5, mariadb, sqlarchemy, pandas
3. run the service : "python3.9 /HOME_DIR/loader_daemon/loader_daemon.py"
4. please open the log : tail -f /HOME_DIR/loader_daemon/var/log/loader_daemon.log
5. paste your files in /HOME_DIR/content/
6. After the thread done, please check the content folder


Note: I have created the docker container, but somehow when i start the container, the status was exit. I still searching the rootcause and the solustion