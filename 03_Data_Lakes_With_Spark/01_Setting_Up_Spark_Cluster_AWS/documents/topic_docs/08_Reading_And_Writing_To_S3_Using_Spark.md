###S3 Buckets
With the convenient AWS UI, we can easily mistake AWS S3 (Simple Storage Service) equivalent as Dropbox or even Google Drive. This is not the case for S3. S3 stores an object, and when you identify an object, you need to specify a bucket, and key to identify the object. For example,

```python
df = spark.read.load("s3://my_bucket/path/to/file/file.csv")
```
From this code, ```s3://my_bucketis``` the bucket, and ```path/to/file/file.csv``` is the key for the object. Thankfully, if we’re using spark, and all the objects underneath the bucket have the same schema, you can do something like below.

```python
df = spark.read.load("s3://my_bucket/")
```
This will generate a dataframe of all the objects underneath the ```my_bucket``` with the same schema. Pretend some structure in s3 like below:

```text
my_bucket
  |---test.csv
  path/to/
     |--test2.csv
     file/
       |--test3.csv
       |--file.csv
```
If all the csv files underneath my_bucket, which are ```test.csv```, ```test2.csv```, ```test3.csv```, and ```file.csv``` have the same schema, the dataframe will be generated without error, but if there are conflicts in schema between files, then the dataframe will not be generated. As an engineer, you need to be careful on how you organize your data lake.

[Link to Github Repo](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/demo_code) on Demo code referred to in video: HERE