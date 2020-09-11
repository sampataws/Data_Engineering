###Launching a Redshift Cluster in the AWS Console

* Follow the instructions below to create a Redshift cluster
* Use the query editor to create a table and insert data
* Delete the cluster

Note: You can use the IAM role and security group created in the last lesson.

###Launch a Redshift Cluster
```WARNING```: The cluster that you are about to launch will be live, and you will be charged the standard Amazon Redshift usage fees for the cluster until you delete it. ```Make sure to delete your cluster each time you're finished working to avoid large, unexpected costs.``` Instructions on deleting your cluster are included on the last page. You can always launch a new cluster, so don't leave your Redshift cluster running overnight or throughout the week if you don't need to.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at https://console.aws.amazon.com/redshift/.
2. On the Amazon Redshift Dashboard, choose Launch cluster.
    ![image](../images/rcluster1.png)
3. On the Cluster details page, enter the following values and then choose Continue:
    * ```Cluster identifier```: Enter redshift-cluster.
    * ```Database name```: Enter dev.
    * ```Database port```: Enter 5439.
    * ```Master user name```: Enter awsuser.
    * ```Master user password and Confirm password```: Enter a password for the master user account.
    ![image](../images/rcluster2.png)
4. On the Node Configuration page, accept the default values and choose ```Continue```.
    ![image](../images/rcluster3.png)
5. On the Additional Configuration page, enter the following values:
    * VPC security groups: redshift_security_group
    * Available IAM roles: myRedshiftRole
   
   Choose Continue.
    ![image](../images/rcluster4.png)
6. Review your Cluster configuration and choose Launch cluster.
    ![image](../images/rcluster5.png)
7. A confirmation page will appear and the cluster will take a few minutes to finish. Choose ```Clusters``` in the left navigation pane to return to the list of clusters.
    ![image](../images/rcluster6.png)


##Delete a Redshift Cluster
Make sure to delete your cluster each time you're finished working to avoid large, unexpected costs. You can always launch a new cluster, so don't leave it running overnight or throughout the week if you don't need to.

1. On the ```Clusters``` page of your Amazon Redshift console, click on the box next to your cluster to select it, and then click on ```Cluster > Delete cluster.```
    ![image](../images/rcluster7.png)
2. You can choose No for Create snapshot, check the box that you acknowledge this, and then choose ```Delete```.
    ![image](../images/rcluster8.png)
3. Your cluster will change it's status to deleting, and then disappear from your Cluster list once it's finished ```deleting```. You'll no longer be charged for this cluster.
    ![image](../images/rcluster9.png)






