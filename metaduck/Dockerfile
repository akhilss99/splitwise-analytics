FROM openjdk:19-buster

WORKDIR /home/splitwise-analytics/metaduck

ADD https://downloads.metabase.com/v0.46.6.4/metabase.jar .
ADD https://github.com/AlexR2D2/metabase_duckdb_driver/releases/download/0.2.2/duckdb.metabase-driver.jar plugins/

RUN chmod 744 plugins/duckdb.metabase-driver.jar

CMD ["java", "-jar", "metabase.jar"]