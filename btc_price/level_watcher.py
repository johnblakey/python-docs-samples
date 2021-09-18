import logging

from google.cloud import bigquery
from push_notification import send_sms


def gas_push_calculation():
    # Construct a BigQuery client object.
    bqclient = bigquery.Client()

    # Create query
    table_id = "`personal-crypto-over-9000.cryptocurrencies.fees`"
    query_string = "SELECT * FROM " + table_id + "ORDER BY datetime DESC LIMIT 3"

    query_job = bqclient.query(query_string)

    # Build array of fees
    fees = []
    for row in query_job:
        fees.append(row[0])

    # TODO add way for user to apply Fee alert limit (data studio?)
    limit = 40

    # TODO timer of 30 minutes once a message is sent (build into sms push?)

    # Simple logic to send a message based on prior fee reading
    if fees[0] > limit and fees[1] <= limit:
        send_sms("Current gas fee: {} is now higher than your setting:{}".format(fees[0], limit))
        logging.info("SMS sent: Current gas fee: {} is now higher than your setting:{}".format(fees[0], limit)) 
    elif fees[0] < limit and fees[1] >= limit:
        send_sms("Current gas fee: {} is now lower than your setting:{}".format(fees[0], limit))
        logging.info("SMS sent: Current gas fee: {} is now lower than your setting:{}".format(fees[0], limit))
    else:
        logging.info("No SMS sent: Current gas fee: {}".format(fees[0]))

    return "Query finished, current ETH Gas fee is {}".format(fees[0])
    