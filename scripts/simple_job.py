from pyspark.sql import SparkSession 

# Membuat session Spark
spark = SparkSession.builder \
    .appName("SimpleJob") \
    .getOrCreate() 

# Menyiapkan data
data = [("A", 10), ("B", 20), ("A", 30)] 
columns = ["category", "value"] 

# Membuat DataFrame
df = spark.createDataFrame(data, columns) 

# Proses: GroupBy category lalu hitung jumlah (sum) value
df.groupBy("category").sum("value").show() 

# Menutup session
spark.stop()