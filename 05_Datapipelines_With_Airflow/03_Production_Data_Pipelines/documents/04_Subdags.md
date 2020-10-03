#SubDAGs
Commonly repeated series of tasks within DAGs can be captured as reusable SubDAGs. Benefits include:

* Decrease the amount of code we need to write and maintain to create a new DAG
* Easier to understand the high level goals of a DAG
* Bug fixes, speedups, and other enhancements can be made more quickly and distributed to all DAGs that use that SubDAG

##Drawbacks of Using SubDAGs
* Limit the visibility within the Airflow UI
* Abstraction makes understanding what the DAG is doing more difficult
* Encourages premature optimization

##Common Questions
```Can Airflow nest subDAGs?``` - Yes, you can nest subDAGs. However, you should have a really good reason to do so because it makes it much harder to understand what's going on in the code. Generally, subDAGs are not necessary at all, let alone subDAGs within subDAGs.