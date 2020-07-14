###Overview of the Set up of a Spark Cluster
1. ```Amazon S3``` will store the dataset.
2. We rent a cluster of machines, i.e., our ```Spark Cluster```, and iti s located in AWS data centers. We rent these using AWS service called ```Elastic Compute Cloud (EC2)```.
3. We log in from your local computer to this Spark cluster.
4. Upon running our Spark code, the cluster will load the dataset from ```Amazon S3``` into the cluster’s memory distributed across each machine in the cluster.

New Terms:
* ```Local mode```: You are running a Spark program on your laptop like a single machine.
* ```Standalone mode```: You are defining Spark Primary and Secondary to work on your (virtual) machine. You can do this on EMR or your machine. Standalone mode uses a resource manager like YARN or Mesos.