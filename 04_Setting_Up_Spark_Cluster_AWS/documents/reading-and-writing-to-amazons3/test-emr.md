```python
log_of_songs = [
        "Despacito",
        "Nice for what",
        "No tears left to cry",
        "Despacito",
        "Havana",
        "In my feelings",
        "Nice for what",
        "despacito",
        "All the stars"
]

distributed_song_log = sc.parallelize(log_of_songs)
```


```python
distributed_song_log.map(lambda x: x.lower()).collect()
```


```python
sparkify_log_data = "s3n://sparkify/sparkify_log_small.json"
```


```python
df = spark.read.json(sparkify_log_data)
df.persist()

df.head(5)
```


```python
sparkify_log2_path = "hdfs:///user/sparkify_data/sparkify_log_small_2.json"

df2 = spark.read.json(sparkify_log2_path)
df2.persist()
```


```python
df2.head(5)
```
