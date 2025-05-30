git clone:"github-link"
cd  file name,
docker cp ~/Downloads/Ali_Baba_Stock_Data.csv <container_id>:/Ali_Baba_Stock_Data.csv
docker ps
docker exec -it <container_id> bash

hdfs dfs -mkdir -p /user/stock_data
hdfs dfs -put /Ali_Baba_Stock_Data.csv /user/stock_data
docker-compose up
docker compose up -d
 docker compose pull
docker exec -it spark bash
docker cp read_from_hdfs.py spark:/opt/bitnami/spark/read_from_hdfs.py
 docker cp read_from_hdfs.py (container_id):/opt/bitnami/spark/read_from_hdfs.py\n
 docker exec -it spark bash
 docker cp read_from_hdfs.py (container_id):/opt/bitnami/spark/read_from_hdfs.py\n
 docker cp read_from_hdfs.py (container_id)c6:/opt/bitnami/spark/read_from_hdfs.py\n
 docker ps -a
 docker cp read_from_hdfs.py (container_id):/opt/bitnami/spark/read_from_hdfs.py\n
 docker exec -it (container_id)bash
 spark-submit read_from_hdfs.py\n
