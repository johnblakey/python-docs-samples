# import time
import logging
import time

from google.cloud import bigquery


# Query db  project_id = "personal-crypto-over-9000"

def gas_push_calculation():
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # ID of table to append to.
    table_id = "personal-crypto-over-9000.cryptocurrencies.fees"


    query_job = client.query(
        """
        SELECT *
        FROM `personal-crypto-over-9000.cryptocurrencies.fees`
        LIMIT 10"""
    )

    # Query db
    results = query_job.result()

    # parse results

    current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')
    