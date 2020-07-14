###Creating EMR Script
While creating EMR through AWS console has been shown, but if you know the specificity of your instances, such as which applications you need or what kind of clusters you’ll need, you can reuse the EMR script that we will create below multiple times.

```text
aws emr create-cluster --name <cluster_name> \
 --use-default-roles --release-label emr-5.28.0  \
--instance-count 3 --applications Name=Spark Name=Zeppelin  \
--bootstrap-actions Path="s3://bootstrap.sh" \
--ec2-attributes KeyName=<your permission key name> \
--instance-type m5.xlarge --log-uri s3:///emrlogs/
```

####Learning Components on EMR Script
Let’s break down the code and go over each part of the code in the EMR script. It’s important that you know what each component does in order to launch a proper cluster and services attached to this script.

###EMR Script Components
* ```aws emr``` : Invokes the AWS CLI, and specifically the command for EMR.
* ```create-cluster``` : Creates a cluster
* ```--name``` : You can give any name for this - this will show up on your AWS EMR UI. This can be duplicate as existing EMR.
* ```--release-label``` : This is the version of EMR you’d like to use. [AWS EMR release versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-components.html)
* ```--instance-count``` : Annotates instance count. One is for the primary, and the rest are for the secondary. For example, if --instance-count is given 4, then 1 instance will be reserved for primary, then 3 will be reserved for secondary instances.
* ```--applications```: List of applications you want to pre-install on your EMR at the launch time. The following are the applications that are available from 6.x versions of EMR .
   * ```Ganglia```
   * ```Hadoop``` 
   * ```HBase``` 
   * ```HCatalog```
   * ```Hive```
   * ```Hue``` 
   * ```JupyterHub```
   * ```Livy```
   * ```MXNet```
   * ```Oozie```
   * ```Phoenix```
   * ```Presto```
   * ```Spark```
   * ```TensorFlow```
   * ```Tez```
   * ```Zeppelin```
   * ```ZooKeeper```
* ```--bootstrap-actions```: You can have a script stored in S3 that pre-installs or sets environmental variables, and call that script at the time EMR launches
* ```--ec2-attributes KeyName```: Specify your permission key name, for example, if it is MyKey.pem, just specify MyKey for this field
* ```--instance-type```: Specify the type of instances you want to use. [Detailed list can be accessed here](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-supported-instance-types.html), but find the one that can fit your data and your budget.
* ```--log-uri```: S3 location to store your EMR logs in. This log can store EMR metrics and also the metrics/logs for submission of your code.

Now it’s your turn to create your own EMR script.

### Exercise: Create Your Own EMR Script

```NOTE 1```: Do not forget to add the ```--auto-terminate``` field because EMR clusters are costly. Once you run this script, you’ll be given a unique cluster ID.

```NOTE 2```. Check the status of your cluster using ```aws emr --cluster-id <cluster_id>```.

####For this exercise, we will be creating an EMR cluster.

Step 1. Install ```awscli``` using pip.
* You can get instructions for MacOS, Windows, Linux here on [AWS Documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

Step 2. This will give you access to ```create an EMR cluster and EC2 cluster```.
* The EC2 cluster shows a status of all the clusters with your keys, etc.

Step 3. Once it's installed, run the script below to ```launch your cluster```.
* Be sure to include the appropriate file names within the <> in the code.

```text
# Add your cluster name
aws emr create-cluster --name <YOUR_CLUSTER_NAME> 
--use-default-roles  
--release-label emr-5.28.0
--instance-count 2 
--applications Name=Spark  
--bootstrap-actions Path=<YOUR_BOOTSTRAP_FILENAME> 
--ec2-attributes KeyName=<YOUR_KEY_NAME>
--instance-type m5.xlarge 
--instance-count 3 --auto-terminate`

# Specify your cluster name 
`YOUR_CLUSTER_NAME: <INPUT NAME HERE>

# Insert your IAM KEYNAME - 
# Remember, your IAM key name is saved under .ssh/ directory
YOUR_KEY_NAME: <IAM KEYNAME>

# Specify your bootstrap file. Please note that this step is optional. 
# It should be an executable (.sh file) in an accessible S3 location. 
# If you aren't going to use the bootstrap file, 
# you can remove the `--bootstrap-actions` tag above.
# This file is provided in the zipped folder titled
# “Exercise_Creating EMR Cluster” at the bottom of this page.

# In this EMR script, execute using Bootstrap
YOUR_BOOTSTRAP_FILENAME: <BOOTSTRAP FILE>   
```

A copy of the exercises are also available in the lesson git repo: ```Here is the``` [Link to Github](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Setting_Spark_Cluster_In_AWS/exercises/starter)

###Desired Output

####The output should look like this:

```text
{
    "ClusterId": "j-2PZ79NHXO7YYX",
    "ClusterArn": "arn:aws:elasticmapreduce:us-east-2:027631528606:cluster/j-2PZ79NHXO7YYX"
}


# Go to AWS EMR console from your web browser, 
# then check if the cluster is showing up.

#Or you can type

aws emr describe-cluster --cluster-id <CLUSTER_ID FROM ABOVE>`

# You can run `aws emr describe-cluster --cluster-id j-2PZ79NHXO7YYX`
# to confirm if this cluster is ready to go.
```

###Changing Security Groups
1. Once you launch your instance, we will want to log in. Alternately you can use SSH protocol (allows secure remote login) to access your master node on the EMR cluster. Each cluster gets its own security setting.
2. You’ll need to allow EMR to accept incoming SSH protocol so your local machine can connect to your EMR cluster in the AWS Cloud by changing the security group.
3. Next, we’ll be making the SSH connection from your laptop to your EMR cluster. To allow this, we’ll need to change the Security Group on EC2.


Let’s log into AWS EC2 console.

![image](/Users/sampatbudankayala/PycharmProjects/Data_engineering/04_Setting_Up_Spark_Cluster_AWS/documents/topic_docs/security_group_ec2_console.png)

###Setting up Port Forwarding
1. One last thing to do before using the Jupyter Notebook, or even browsing the Spark UI, is to set up proxy.
2. Let’s install FoxyProxy on your Chrome or Firefox browser.

Here is the link to [Amazon’s documentation on managing clusters using it’s web interfaces](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-connect-master-node-proxy.html)

####Testing Port Forwarding
Let’s see if your port forwarding works!

```shell script
# SSH into your cluster first. Note that the port number matches 
# what is in foxyproxy-settings.xml.
ssh -i ~/.aws/<YOUR_PEM_FILE>.pem hadoop@<YOUR IP> -ND 8157

# Open another terminal tab, then copy this code into your cluster 
# with your PEM file .
scp -i ~/.aws/<YOUR_PEM_FILE>.pem hadoop@<YOUR IP>:/home/hadoop/

# Execute the file
python spark_test_script.py

# Open up Resource Manager Tab from AWS console
# If you’re able to see the Resource Manager from your browser,
#  then you have successfully done port forwarding.
```
Click on the Spark UI from the cluster management site. If this is directed to another tab and shows you the Spark executor information, you have done port forwarding successfully!

You should be able to see those application names turn into blue - as in clickable link, then you can tell your port forwarding has been successful.

####See below for the desired screen.

![image](/Users/sampatbudankayala/PycharmProjects/Data_engineering/04_Setting_Up_Spark_Cluster_AWS/documents/topic_docs/Resource_Manager_Dashboard.png)





