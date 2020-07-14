###Submitting Spark Script Instructions
Here is the link to the [GitHub](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/exercises/starter) repo where a copy of the exercise instructions are located along with cities.csv file.

* Download the cities.csv dataset to your local machine.
* Upload a file into an S3 location using the AWS S3 console, or you can use the AWS CLI command, like aws s3 cp <your current file location>/<filename> s3://<bucket_name>.
* Create an EMR instance.
* Copy the file to your EMR instance, preferably in your home directory of EMR instance.
* Execute the file using spark-submit <filename>.py.
* A note about SSH
* SSH is a specific protocol for secure remote login and file transfer.

The instructor is showing you one way to save your files. He is using SSH protocol to save the files in the EMR instance. When you see ```hadoop@ip-###- ###-####```, this indicates that the instructor accessed the EMR instance using SSH protocol. However, once he terminates the EMR instance, everything he would saved on the EMR instance will be lost. This is because EMR instance is not kept active all the time since it is expensive.

In the Reflection Exercise you can experiment with an alternate good industry practice. Data engineers always save their initial, final, and intermediate data of the data pipeline in the S3 for future retrieval. It is best practice to move your files from your local machine to AWS S3, then use the program to read the data from AWS S3.

####Reflection exercise:
Use your proxy to view the Spark UI to understand how your code and workers are working, i.e. which are transformation vs action words (and if they are correctly showing up on Spark UI), and to get familiar with reading the Spark UI. This will give you a better understanding on how your Spark program runs.

```Reminder link``` to [Amazon documentation](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html) on FoxyProxy