import time
import logging

from coinbase.wallet.client import Client
from secrets import access_secret_version
from google.cloud import bigquery


def add_btc_price():
    current_price = get_coinbase_spot_price()
    save_price(current_price)

    return current_price


def get_coinbase_spot_price():
    # Get secrets from Secret Google Service
    project_id = "personal-crypto-over-9000"
    api_key = access_secret_version(project_id, "coinbase-api-key-jb", "1")
    api_secret = access_secret_version(project_id, "coinbase-api-secret-jb", "2")

    client = Client(api_key, api_secret)

    currency_code = 'USD'  # can also use EUR, CAD, etc.

    # Make the request
    price = client.get_spot_price(currency=currency_code)

    return price.amount


def save_price(price):
    # Construct a BigQuery client object.
    client = bigquery.Client()

    # ID of table to append to.
    table_id = "personal-crypto-over-9000.cryptocurrencies.price"

    current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')

    rows_to_insert = [
        {u"btc_price": price, u"timestamp": current_datetime, u"currency": "USD"}
    ]

    errors = client.insert_rows_json(
        table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert)
    )  # Make an API request.
    if errors == []:
        logging.info("New rows have been added.")
    else:
        logging.error("Encountered errors while inserting rows: {}".format(errors))