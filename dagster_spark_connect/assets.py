from dagster import asset
from pyspark.sql import Row
from pyspark.sql.connect.dataframe import DataFrame
from pyspark.sql.types import IntegerType, StringType, StructField, StructType

from .resources import PySparkConnectResource


@asset
def people(pyspark: PySparkConnectResource):
    schema = StructType(
        [StructField("name", StringType()), StructField("age", IntegerType())]
    )
    rows = [
        Row(name="Thom", age=51),
        Row(name="Jonny", age=48),
        Row(name="Nigel", age=49),
    ]
    return pyspark.spark_session.createDataFrame(rows, schema)


@asset
def people_over_50(people: DataFrame):
    return people.filter(people["age"] > 50)
