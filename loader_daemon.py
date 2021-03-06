#!/usr/bin/env python
import time
import sys
import os
import logging
import threading
import pandas as pd
from sqlalchemy import create_engine, String, Column, ForeignKey, Table, MetaData

"""
    Constants
"""
version = 1.0
name = 'loader-daemon'
title = name + ' v' + str(version)


"""
    Default Configuration Value
"""
config = {
    'logging':{
        'format':'%(asctime)s %(msecs)d -> %(module)s %(levelname)s : %(message)s',
        'dateformat':'%Y%m%d_%H%M%S',
        'path':'var/log/' + name + '.log',
        'level':'INFO'
    },
    'db':{
        'hostname':'localhost',
        'dbname':'loader_daemon',
        'uname':'root',
        'pwd':''
    }

}

def data_process(dir_contents, dir_path):  
    threads = list()
    index = 0
    for file in dir_contents:
        logging.info("[Main    ]: create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index, file, dir_path))
        threads.append(x)
        x.start()
        index +=1

    for index, thread in enumerate(threads):
        thread.join()
        logging.info("[Main    ]: thread %d done", index)
  

def thread_function(index, file, dir_path):
    logging.info("[Thread %s]: starting", index)
    logging.info('[Thread %s]: '+ file + ' is detected', index)

    try:
        df = pd.read_csv((dir_path + file), sep=',', header = 0, quotechar='\'', encoding='utf-8')
        fileName = os.path.splitext(file)[0]
        logging.info('[Thread %s]: read the '+ file +' is done', index)
        with engine.begin() as connection:
            df.to_sql(fileName, con=connection, index=False, if_exists='append')
            logging.info('[Thread %s]: insert into '+ fileName +' table is done', index)
            engine.dispose()

    except Exception as e:
        logging.info(e)

    if os.path.exists(dir_path + file):
        os.remove(dir_path + file)
        logging.info('[Thread %s]: delete the '+ file +' is done', index)

    logging.info('[Thread %s]: finishing', index)

def create_tables():
    ''' Create new tables handler'''
    metadata = MetaData()
    with engine.connect() as conn:
        team_table = Table('team', metadata,
            Column('TEAM_ID', String(10), primary_key=True)
        )
 

        task_table = Table('task', metadata,
            Column('TASK_ID', String(10), primary_key=True),
            Column('SKILL', String(10), nullable=False)
        )
   

        team_skill_table = Table('team_skill', metadata,
            Column('TEAM_ID', String(10), nullable=False),
            Column('SKILL', String(10), nullable=False)
        )
 

        metadata.create_all(conn, checkfirst=False)
        conn.close()
        return


if __name__ == "__main__":
    """
        log configuration
    """
    try:
        logging.basicConfig(
            format = config['logging']['format'],
            datefmt = config['logging']['dateformat'],
            filename = config['logging']['path'],
            level = getattr(logging, config['logging']['level'].upper(), None)
        )
    except Exception as e:
        print(e)
        sys.exit(0)
    
    """
        db connection
    """
    # Credentials to database connection
    hostname=config['db']['hostname']
    dbname=config['db']['dbname']
    uname=config['db']['uname']
    pwd=config['db']['pwd']

    try:
        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}"
                        .format(host=hostname, user=uname, pw=pwd))    
        existing_databases = engine.execute("SHOW DATABASES;")
        existing_databases = [d[0] for d in existing_databases]
        # DB checking
        if dbname not in existing_databases:
            engine.execute("CREATE DATABASE {0}".format(dbname))
            

        engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                        .format(host=hostname, user=uname, pw=pwd, db=dbname))

        existing_tables = engine.execute("SHOW TABLES")
        existing_tables = [d[0] for d in existing_tables]
        # Tables checking
        if len(existing_tables)==0:
            create_tables()

    except Exception as e:
        print(e)



    """
        content directory checking
    """
    dir_path = (os.path.expanduser('~') + '/content/')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    print(title+'\n')

    """
        Main Loop: if find the files in the content folder
    """
    while True:
        try:
            dir_contents = os.listdir(dir_path)
            if len(dir_contents) !=0:
                data_process(dir_contents, dir_path)        
        except Exception as e:
            if 'Received Signal ' in e.args[0]:
                logging.info(e)
                break
        time.sleep(1)

    logging.info("[ Terminated ]")