"""
https://ethgasstation.info/api/ethgasAPI.json?.
Returns:
  Current eth gas fee value and saves it to db
"""  
import logging
import time
import json

from urllib.request import Request, urlopen
from google.cloud import bigquery


def eth_gas_fee (temp):
  # create request acting as a browser
  url = "https://www.etherchain.org/api/gasPriceOracle"
  request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

  response = urlopen(request)

  # decode response
  string = response.read().decode('utf-8')
  json_obj = json.loads(string)

  current_base_fee = json_obj['currentBaseFee']
  logging.info("Current Base Fee returned from etherchain api {}".format(current_base_fee))

  save_fee(current_base_fee)

  # Activate logic to check if new value results in an sms sent
  # create request acting as a browser
  url = "https://personal-crypto-over-9000.wm.r.appspot.com/checkgas"
  request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
  
  response = urlopen(request)

  # Must return string, dict, but not float
  return "Gas checked, uploaded, and alert checked."
  

def save_fee(fee):
  # Construct a BigQuery client object.
  client = bigquery.Client()

  # ID of table to append to.
  table_id = "personal-crypto-over-9000.cryptocurrencies.fees"

  current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')

  rows_to_insert = [
      {u"fee": fee, u"datetime": current_datetime, u"currency": "ETH"}
  ]

  # Make API request, save errors if they occur
  errors = client.insert_rows_json(
      table_id, rows_to_insert, row_ids=[None] * len(rows_to_insert)
  )
  
  if errors == []:
      logging.info("New rows have been added.")
  else:
      logging.error("Encountered errors while inserting rows: {}".format(errors))
