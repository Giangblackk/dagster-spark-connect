from setuptools import find_packages, setup

setup(
    name="dagster_spark_connect",
    packages=find_packages(exclude=["dagster_spark_connect_tests"]),
    install_requires=[
        "dagster",
        "pyspark[connect]==3.5.1",
        "dagster_pyspark",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
