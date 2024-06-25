from dagster import (ConfigurableIOManager, Definitions,
                     load_assets_from_modules)

from . import assets
from .resources import PySparkConnectResource

all_assets = load_assets_from_modules([assets])

pyspark_resource = PySparkConnectResource(spark_config={"spark.app.name": "dagster"})


class ParquetIOManager(ConfigurableIOManager):
    pyspark: PySparkConnectResource
    path_prefix: str

    def _get_path(self, context) -> str:
        return "/".join(
            [context.resource_config["path_prefix"], *context.asset_key.path]
        )

    def handle_output(self, context, obj):
        obj.write.parquet(self._get_path(context))

    def load_input(self, context):
        spark = self.pyspark.spark_session
        return spark.read.parquet(self._get_path(context.upstream_output))


defs = Definitions(
    assets=all_assets,
    resources={
        "pyspark": pyspark_resource,
        "io_manager": ParquetIOManager(pyspark=pyspark_resource, path_prefix="/opt/spark/work-dir"),
    },
)
