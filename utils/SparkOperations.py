from pyspark.sql import SparkSession

class SparkOperations:
	def __init__(self):
		'''
		constructor
		'''
	def create_session(self, app):
		spark = SparkSession.builder.appName(app).getOrCreate()
		return spark

	def find_count(self, df):
		return df.count()

	def read_csv(self, spark, file_name):
		return spark.read.csv(file_name,header=True)
