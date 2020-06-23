import os
import mysql.connector as msql
from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta

connstr = os.getenv('connstr')
db_host = os.getenv('dbhost')
db_user = os.getenv('dbuser')
db_pwd = os.getenv('dbpwd')
db_name = os.getenv('dbname')
containerName = os.getenv('containerName')

blob_service_client = BlobServiceClient.from_connection_string(connstr)
container_client=blob_service_client.get_container_client(containerName)
blob_list = container_client.list_blobs()
game_db=msql.connect(host=db_host ,user=db_user,password=db_pwd,database=db_name)
game_cur=game_db.cursor()
for file in blob_list:
       blob_client= blob_service_client.get_blob_client(container="landing",blob=file.name)
       db_values="("+ blob_client.download_blob().readall() + ")"
       sql= "INSERT INTO games (name, place, thing, animal) VALUES "+ db_values
       game_cur.execute(sql)
       blob_client.delete_blob()

game_db.commit()
