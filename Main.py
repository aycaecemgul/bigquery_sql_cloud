import os
import pyarrow
from google.cloud.bigquery.client import Client
from google.cloud.bigquery.dataset import TableReference,DatasetReference
from google.cloud import bigquery_storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\aycae\\OneDrive\\Belgeler\\First-3c6a5828300b.json'
client = Client()

dataset_ref = DatasetReference(project="bigquery-public-data",dataset_id="hacker_news")
dataset = client.get_dataset(dataset_ref)

table_ref = TableReference(dataset_ref=dataset_ref,table_id="full")
table= client.get_table(table_ref)

client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe()