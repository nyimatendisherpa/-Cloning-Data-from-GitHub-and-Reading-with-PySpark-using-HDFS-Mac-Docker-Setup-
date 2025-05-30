from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("Read_from_HDFS").getOrCreate()
 
#hdfspath
hdfs_path = "hdfs://localhost:9000/user/stock_data/Ali_Baba_Stock_Data.csv"
#read the CSV file
df=spark.read.csv(hdfs_path,header=True,inferSchema=True)
#show data
df.show()
spark.stop()
