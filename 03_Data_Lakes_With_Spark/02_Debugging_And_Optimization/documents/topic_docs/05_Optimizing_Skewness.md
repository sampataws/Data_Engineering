##Optimizing skewness
####Use Cases in Business Datasets
Skewed datasets are common. In fact, you are bound to encounter skewed data on a regular basis. In the video above, the instructor describes a year-long worth of retail business’ data. As one might expect, retail business is likely to surge during Thanksgiving and Christmas, while the rest of the year would be pretty flat. Skewed data indicators: If we were to look at that data, partitioned by month, we would have a large volume during November and December. ```We would like to process this dataset through Spark using different partitions```, if possible. What are some ways to solve skewness?

* Data preprocess
* Broadcast joins
* Salting

####So how do we solve skewed data problems?
The goal is to change the partitioning columns to take out the data skewness (e.g., the year column is skewed).

#####1. Use Alternate Columns that are more normally distributed:
E.g., Instead of the ```year``` column, we can use ```Issue_Date``` column that isn’t skewed.

#####2. Make Composite Keys:
For e.g., you can make composite keys by combining two columns so that the new column can be used as a composite key. For e.g, combining the ```Issue_Date``` and ```State``` columns to make a new composite key titled ```Issue_Date + State```. The ```new``` column will now include data from 2 columns, e.g., ```2017-04-15-NY```. This column can be used to partition the data, create more normally distributed datasets (e.g., distribution of parking violations on 2017-04-15 would now be more spread out across states, and this can now help address skewness in the data.


#####3. Partition by number of Spark workers:
Another easy way is using the Spark workers. If you know the number of your workers for Spark, then you can easily partition the data by the number of workers  ```df.repartition(number_of_workers)``` to repartition your data evenly across your workers. For example, if you have 8 workers, then you should do ```df.repartition(8)``` before doing any operations.

##Optimizing skewness
Let’s recap how I solved the skewed data problem.
I would like to use two different ways to solve this problem.

* I would like to assign a new, temporary partition key before processing any huge shuffles.
* The second method is using repartition.

##Practice Optimizing Skewness
Here is a link to the starter code for you to [practice repartitioning](https://github.com/udacity/nd027-c3-data-lakes-with-spark/tree/master/Debugging_And_Optimization/exercises/starter) to address challenges with Skewed data.

You will find the zipped Parking_violations.csv file below. This file is not available in the gitrepo because of its size.
Supporting Materials
 Parking Violation.Csv