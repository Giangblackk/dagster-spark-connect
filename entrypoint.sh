#!/bin/bash

echo "Starting Spark Connect Server"

bash /opt/spark/sbin/start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:3.5.1

sleep infinity