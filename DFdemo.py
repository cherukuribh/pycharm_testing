import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType


#def print_hi(name):
#    print(name)

if __name__ == '__main__':
    os.environ['PYSPARK_PYTHON'] = sys.executable
    spark = SparkSession.builder.master("local").appName("p2").getOrCreate()

    orderSchema = StructType([
        StructField("orderid", IntegerType(), nullable=True),
        StructField("orderdate", StringType(), nullable=True),
        StructField("custid", IntegerType(), nullable=True),
        StructField("orderstatus", StringType(), nullable=True)
    ])
    #ordersdf = spark.read.option("header","true").schema(orderSchema).csv("C:\\Users\\cheru\\PycharmProjects\\pythonProject1\\orders.csv")
    ordersdf = spark.read.option("header","true").schema(orderSchema).csv("/user/ec2-user/UKUSMarHDFS/bharathi/orders.csv")
    print("testing webhook")
    print("testing 2 webhook")
    print("testing 3 webhook")
    print("testing 4 webhook")

    ordersdf.show(5)