FROM python:3.11.4-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends

WORKDIR /home/splitwise-analytics/transform

COPY . .

RUN pip install \
         --no-cache-dir \
         -r requirements.txt

CMD dbt build --profiles-dir . && sleep infinity