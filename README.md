# dagster-spark-connect

Sample Dagster project for developing Pyspark pipelines with Spark Connect.


Since Apache Spark 3.4, [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html) introduced a new decoupled client-server architecture for Spark applications to run remotely without requiring the Spark driver to be on the same host as your application (might crash applications when critical exceptions happen) or requiring submiting Spark application to a remote Spark cluster (harder to debug, non-interactive).

![Spark Connect API](https://spark.apache.org/docs/latest/img/spark-connect-api.png)

By using Spark Connect API, we have a new approach of developing Spark data pipeline in Dagster which is easier to develop, test and debug data pipeline locally, and more straight foward deployment flow.


References:
- [Spark Connect](https://spark.apache.org/spark-connect/)
- [Airflow PySpark decorator support Spark Connect](https://airflow.apache.org/docs/apache-airflow-providers-apache-spark/stable/decorators/pyspark.html#spark-connect)

## Getting started

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

### Environment setup

First, start Spark Connect Server container with `docker compose`:

```bash
docker compose up -d
```

You should found a new container named `spark-connect` when list running containers:

```bash
# if you use Docker
docker ps
# if you use Podman
podman ps
```

This `spark-connect` container exposes 2 ports:
- Port `4040` for Spark Web UI, you can access via address `localhost:4040` and
- Port `15002` for Spark Connect Server.

### Project setup

Second, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_spark_connect_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_spark_connect_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.
