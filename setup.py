from setuptools import find_packages, setup

setup(
    name="dagster_spark_connect",
    packages=find_packages(exclude=["dagster_spark_connect_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
