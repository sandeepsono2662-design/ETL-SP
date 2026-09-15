from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Create RDD
data = [
    "Hello world",
    "PySpark is powerful",
    "Hello PySpark"
]

rdd = spark.sparkContext.parallelize(data)

# Word Count
word_counts = (
    rdd.flatMap(lambda line: line.split())
       .map(lambda word: (word, 1))
       .reduceByKey(lambda a, b: a + b)
)

# Display results
for word, count in word_counts.collect():
    print(word, count)

spark.stop()