### Distribution Styles To Partition a Redshift Tables

* EVEN distribution
* ALL distribution
* AUTO distribution
* KEY distribution

### ```EVEN``` Distribution Example Fact and Dim:
  * ![image](../images/distribution_even.png)
  * ![image](../images/distribution_even1.png)

#### Cost of Join with Even Distribution 
  * ![image](../images/distribution_even2.png)
  ```NOTE```: Below image shows the possibility of network traffic over the even distribution when joining a fact and dimension tables.
  * ![image](../images/distribution_even3.png)
  
  
### ```ALL``` Distribution Example Fact and Dim:
  * ![image](../images/distribution_all.png)
  * ![image](../images/distribution_all1.png)

### ```AUTO``` Distribution Example Fact and Dim:
  * ![image](../images/distribution_auto.png)
  
### ```KEY``` Distribution Example Fact and Dim:
  * ![image](../images/distribution_key.png)
  * ![image](../images/distribution_key1.png)
  ```NOTE```: Distributing both facts and dimensions on the joining KEY's eliminates shuffling
  * ![image](../images/distribution_key2.png)

  









  
