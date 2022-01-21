import pickle
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("docker-pandas").getOrCreate()
sc = spark.sparkContext

import pandas as pds
print("PANDAS VERSION IN THE SESSION:", pds.__version__)

from google.cloud import storage

def download_blob(bucket_name, source_blob_name, destination_file_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )

download_blob("rohith", "spark-docker-files/model.pkl", "model_download.pkl")

print("LOADING PICKLE FILE.......")
clf2  = pickle.load(open('model_download.pkl', 'rb'))
print("PICKLE FILE SUCCESSFULLY LOADED")


# predict a new sample
X_new = [[3.0, 3.6, 1.3, 0.25]]
print('Input sample: {}'.format(X_new))
pred = clf2.predict(X_new)
print('Predicted class is {}'.format(pred))