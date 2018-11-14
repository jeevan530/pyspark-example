from utils import SparkOperations

spark_utils = SparkOperations()

spark = spark_utils.create_session('sample_app')
df = spark_utils.read_csv(spark, '/temp.csv')
print(spark_utils.find_count(df))
