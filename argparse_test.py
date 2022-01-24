#! /opt/conda/default/bin/python

import sys
import argparse
from google.cloud import bigquery, storage

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, required=True)
parser.add_argument('--table', type=str, required=True)
args = parser.parse_args()
bq_client = bigquery.Client()
storage_client = storage.Client()
bucket = storage_client.bucket("anuj-suchchal-bucket")
blob_in = bucket.blob('query.sql')
query = blob_in.download_as_string().decode("utf-8")
query = query.format(dataset=args.dataset, table=args.table)
query_job = bq_client.query(query)
results = query_job.result()
for row in results:
    print(row)
