###Citations for slides:

* https://en.wikipedia.org/wiki/Dimension_(data_warehouse)
* https://en.wikipedia.org/wiki/Fact_table

The following image shows the relationship between the fact and dimension tables for the example shown in the video. As you can see in the image, the unique primary key for each Dimension table is included in the Fact table.

In this example, it helps to think about the ```Dimension tables``` providing the following information:

* Where the product was bought? (Dim_Store table)
* When the product was bought? (Dim_Date table)
* What product was bought? (Dim_Product table)

The ```Fact table``` provides the  ```metric of the business process``` (here Sales).

* ```How many``` units of products were bought? (Fact_Sales table)

![image](/Users/sampatbudankayala/PycharmProjects/Data_engineering/01_Data_Modeling/02_Relational_Data_Models/documents/topic_docs/fact_dim.png)

If you are familiar with ```Entity Relationship Diagrams``` (ERD), you will find the depiction of STAR and SNOWFLAKE schemas in the demo familiar. The ERDs show the data model in a concise way that is also easy to interpret. ERDs can be used for any data model, and are not confined to STAR or SNOWFLAKE schemas. Commonly available tools can be used to generate ERDs. However, more important than creating an ERD is to learn more about the data through conversations with the data team so as a data engineer you have a strong understanding of the data you are working with.

More information about ER diagrams can be found at this [Wikipedia](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model) page.