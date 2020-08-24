import os
import pyarrow
from google.cloud import bigquery
from google.cloud.bigquery.client import Client
from google.cloud.bigquery.dataset import TableReference,DatasetReference
from google.cloud import bigquery_storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\aycae\\OneDrive\\Belgeler\\First-3c6a5828300b.json'
client = Client()

dataset_ref = DatasetReference(project="bigquery-public-data",dataset_id="hacker_news")
dataset = client.get_dataset(dataset_ref)

table_ref = TableReference(dataset_ref=dataset_ref,table_id="full")
table= client.get_table(table_ref)


def estimate_query_size(query):
    # Create a QueryJobConfig object to estimate size of query without running it
    dry_run_config = bigquery.QueryJobConfig(dry_run=True)

    # API request - dry run query to estimate costs
    dry_run_query_job = client.query(query, job_config=dry_run_config)

    print("This query will process {} bytes.".format(dry_run_query_job.total_bytes_processed))

