##What Is A Data Warehouse? A Business Perspective
You are in charge of a retailer’s data infrastructure. Let’s look at some business activities.

* Customers should be able to find goods & make orders
* Inventory Staff should be able to stock, retrieve, and re-order goods
* Delivery Staff should be able to pick up & deliver goods
* HR should be able to assess the performance of sales staff
* Marketing should be able to see the effect of different sales channels
* Management should be able to monitor sales growth

Ask yourself: Can I build a database to support these activities? Are all of the above questions of the same nature?

Let's take a closer look at details that may affect your data infrastructure.

* Retailer has a nation-wide presence → ```Scale```?
* Acquired smaller retailers, brick & mortar shops, online store → ```Single database? Complexity?```
* Has support call center & social media accounts → ```Tabular data?```
* Customers, Inventory Staff and Delivery staff expect the system to be fast & stable → ```Performance```
* HR, Marketing & Sales Reports want a lot information but have not decided yet on everything they need → ```Clear Requirements?```

Ok, maybe one single relational database won’t suffice :)