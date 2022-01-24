"""Create a Google BigQuery linear regression input table.

In the code below, the following actions are taken:
* A new dataset is created "natality_regression."
* A query is run against the public dataset,
    bigquery-public-data.samples.natality, selecting only the data of
    interest to the regression, the output of which is stored in a new
    "regression_input" table.
* The output table is moved over the wire to the user's default project via
    the built-in BigQuery Connector for Spark that bridges BigQuery and
    Cloud Dataproc.
"""

from google.cloud import bigquery

# Create a new Google BigQuery client using Google Cloud Platform project
# defaults.
import os

credential_path = "C:\\Users\\rohith.s.bheemreddy\\Downloads\\V-PoC\\XMLtoairflow\\docker-testing\\vgrid-gcp-mlops-c8c0c03b7a24.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

client = bigquery.Client()

# Prepare a reference to a new dataset for storing the query results.
dataset_id = "natality_regression"
dataset_id_full = f"{client.project}.{dataset_id}"

dataset = bigquery.Dataset(dataset_id_full)

# Create the new BigQuery dataset.
dataset = client.create_dataset(dataset)

# Configure the query job.
job_config = bigquery.QueryJobConfig()

# Set the destination table to where you want to store query results.
# As of google-cloud-bigquery 1.11.0, a fully qualified table ID can be
# used in place of a TableReference.
job_config.destination = f"{dataset_id_full}.regression_input"

# Set up a query in Standard SQL, which is the default for the BigQuery
# Python client library.
# The query selects the fields of interest.
query = """
    SELECT
        weight_pounds, mother_age, father_age, gestation_weeks,
        weight_gain_pounds, apgar_5min
    FROM
        `bigquery-public-data.samples.natality`
    WHERE
        weight_pounds IS NOT NULL
        AND mother_age IS NOT NULL
        AND father_age IS NOT NULL
        AND gestation_weeks IS NOT NULL
        AND weight_gain_pounds IS NOT NULL
        AND apgar_5min IS NOT NULL
    LIMIT 100000
"""

# Run the query.
query_job = client.query(query, job_config=job_config)
query_job.result()  # Waits for the query to finish
