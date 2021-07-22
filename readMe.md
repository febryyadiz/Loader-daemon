How to run the service:
1. clone the package from github
2. install python 3.9.5, mariadb, sqlalchemy, pandas
3. run the service : "python3.9 /HOME_DIR/loader_daemon/loader_daemon.py"
4. please open the log : tail -f /HOME_DIR/loader_daemon/var/log/loader_daemon.log
5. open all of csv files, then remove double quotation marks("") from the file (I created Column names without the questation marks)
6. paste your files (team.csv, task.csv and team_skill.csv) into /HOME_DIR/content/
7. After the thread done, please check the content folder. If the content folder is empty, the service is running well
8. please changes the rows value on your csv files, then paste it again.



Note: I have created the docker container, but somehow when i started the container, the status was exit. I still searching the rootcause and the solustion

Here's the docker image: https://hub.docker.com/layers/febryyadiz/loader-daemon/1.0/images/sha256-1afd8c6a7c448bd842bc529b86056364a3b58955ebca00013cd821ce1c993e35?context=explore