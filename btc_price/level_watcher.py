import logging

from google.cloud import bigquery
from push_notification import send_sms


# Query db  project_id = "personal-crypto-over-9000"

def gas_push_calculation():
    # Construct a BigQuery client object.
    bqclient = bigquery.Client()

    # ID of table to append to.
    table_id = "`personal-crypto-over-9000.cryptocurrencies.fees`"
    query_string = "SELECT * FROM " + table_id + "ORDER BY datetime DESC LIMIT 10"

    dataframe = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(
            # https://cloud.google.com/bigquery/docs/bigquery-storage-python-pandas
            create_bqstorage_client=True,
        )
    )
    print(dataframe.head())

    # parse results
    # if a message should be sent create message and send
    # send_sms()

    return "Query finished"
    