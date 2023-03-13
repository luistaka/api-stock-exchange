from pytz import timezone
from pyspark import SparkConf
from pyspark.sql import SparkSession
from datetime import datetime

conf = SparkConf()
conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.2.0')
conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'com.amazonaws.auth.DefaultAWSCredentialsProviderChain')

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("app_projeto_aplicado") \
    .config(conf=conf) \
    .getOrCreate()

current_datetime = datetime.now(timezone('America/Sao_Paulo'))
print(current_datetime)

df_customer = spark.read \
    .option("header", "true") \
    .option("encoding", "utf-8") \
    .option("delimiter", ",") \
    .option("inferSchema", "true") \
    .csv(f"s3a://datalake-xpe-raw/gsheet/{current_datetime.date()}/customer_data.csv")

print(df_customer.show())
# df_customer.write.mode("overwrite").parquet("s3a://datalake-xpe-curated/customer_data.parquet")


# # Read JSON file into dataframe
# df = spark.read.json(f"s3a://datalake-xpe-raw/api_stock/{current_datetime.date()}/")
# print(df.show())