# dagster-spark-connect

Dagster library for developing Pyspark pipelines using Spark Connect.


Since Apache Spark 3.4, [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html) introduced a new decoupled client-server architecture for Spark applications to run remotely without requiring the Spark driver to be on the same host as your application (might crash applications when critical exceptions happen) or requiring submiting Spark application to a remote Spark cluster (harder to debug, non-interactive).

![Spark Connect API](https://spark.apache.org/docs/latest/img/spark-connect-api.png)

By using Spark Connect API, we have a new approach of developing Spark data pipeline in Dagster which is easier to develop, test and debug data pipeline locally, and more straight foward deployment flow.


References:
- [Spark Connect](https://spark.apache.org/spark-connect/)
- [Airflow PySpark decorator support Spark Connect](https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/stable/decorators/pyspark.html#spark-connect)
