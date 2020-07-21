##Context ,Templating and Run-time Variables

[Here](https://airflow.apache.org/macros.html) is the Apache Airflow documentation on ```context variables``` that can be included as kwargs.

Here is a link to a [blog post](https://blog.godatadriven.com/zen-of-python-and-apache-airflow) that also discusses this topic.

###Runtime Variables
Airflow leverages templating to allow users to “fill in the blank” with important runtime variables for tasks.

```text
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def hello_date(*args, **kwargs):
    print(f“Hello {kwargs['execution_date']}”)

divvy_dag = DAG(...)
task = PythonOperator(
    task_id='hello_date',
    python_callable=hello_date,
    provide_context=True,
    dag=divvy_dag)
```
NOTE:

The link for the Airflow documentation on context variables has changed since the video was created. Here is the new link: https://airflow.apache.org/macros.html