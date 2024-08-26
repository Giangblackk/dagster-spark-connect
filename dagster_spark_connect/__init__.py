from dagster import (
    ConfigurableIOManager,
    Definitions,
    load_assets_from_modules,
    OutputContext,
)
from pyspark.sql.connect.dataframe import DataFrame

from . import assets
from .resources import PySparkConnectResource

all_assets = load_assets_from_modules([assets])

pyspark_resource = PySparkConnectResource(
    spark_remote="sc://localhost", spark_config={}
)


class ParquetIOManager(ConfigurableIOManager):
    pyspark: PySparkConnectResource
    path_prefix: str

    def _get_path(self, context) -> str:
        return "/".join(
            [context.resource_config["path_prefix"], *context.asset_key.path]
        )

    def handle_output(self, context, obj: DataFrame):
        obj.write.parquet(self._get_path(context), mode="overwrite")

    def load_input(self, context):
        spark = self.pyspark.spark_session
        return spark.read.parquet(self._get_path(context.upstream_output))


class IcebergIOManager(ConfigurableIOManager):
    pyspark: PySparkConnectResource

    def _get_asset_name(self, context: OutputContext):
        return context.asset_key.path[-1]

    def handle_output(self, context, obj: DataFrame):
        obj.write.format("iceberg").mode("overwrite").saveAsTable(
            self._get_asset_name(context)
        )

    def load_input(self, context):
        spark = self.pyspark.spark_session
        return spark.read.format("iceberg").load(
            self._get_asset_name(context.upstream_output)
        )


defs = Definitions(
    assets=all_assets,
    resources={
        "pyspark": pyspark_resource,
        "io_manager": IcebergIOManager(
            pyspark=pyspark_resource,
        ),
    },
)
