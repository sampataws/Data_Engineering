
###EC2 vs EMR


|                            | AWS EMR                                                                                                                    | AWS EC2                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| Distributed computing      | Yes                                                                                                                        | Yes                                                                  |
| Node categorization        | Categorizes secondary nodes into core and task nodes as a result of which data can be lost in case a data node is removed. | Does not use node categorization                                     |
| Can support HDFS?          | Yes                                                                                                                        | Only if you configure HDFS on EC2 yourself using multi-step process. |
| What protocol can be used? | Uses S3 protocol over AWS S3, which is faster than s3a protocol                                                            | ECS uses s3a                                                         |
| Comparison cost            | Bit higher                                                                                                                 | Lower                                                                |



###Circling back about HDFS
Previously we have looked over the Hadoop Ecosystem. To refresh those concepts, we have provided reference material here. HDFS (Hadoop Distributed File System) is the file system. HDFS uses MapReduce system as a resource manager.

Spark can replace the MapReduce algorithm. Since Spark does not have its own distributed storage system, it leverages using HDFS or AWS S3, or any other distributed storage. Primarily in this course, we will be using AWS S3, but let’s review the advantages of using HDFS over AWS S3.

###What is HDFS?
HDFS (Hadoop Distributed File System) is the file system in the Hadoop ecosystem. Hadoop and Spark are two frameworks providing tools for carrying out big-data related tasks. While Spark is faster than Hadoop, Spark has one drawback. It lacks a distributed storage system. In other words, Spark lacks a system to organize, store and process data files.

###MapReduce System
HDFS uses MapReduce system as a resource manager to allow the distribution of the files across the hard drives within the cluster. Think of it as the MapReduce System storing the data back on the hard drives after completing all the tasks.

Spark, on the other hand, runs the operations and holds the data in the RAM memory rather than the hard drives used by HDFS. Since Spark lacks a file distribution system to organize, store and process data files, Spark tools are often installed on Hadoop because Spark can then use the Hadoop Distributed File System (HDFS).


###Why do you need EMR Cluster?
Since a Spark cluster includes multiple machines, in order to use Spark code on each machine, we would need to download and install Spark and its dependencies. This is a manual process. ```Elastic Map Reduce``` is a service offered by AWS that negates the need for you, the user, to go through the manual process of installing Spark and its dependencies for each machine.

###Setting up AWS
Please refer to the latest [AWS documentation to set up an EMR Cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs-launch-sample-cluster.html).

Let’s pause to do a quick check for understanding from a previous page.