#!/bin/bash

# Stop container metabase
docker stop metaduck-visualize

# Execute command on dbt
docker exec dbt-proc dbt run

# Restart container metabase
docker start metaduck-visualize
