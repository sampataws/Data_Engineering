from airflow.plugins_manager import AirflowPlugin

import plugins.operators as operators

# Defining the plugin class
class UdacityPlugin(AirflowPlugin):
    name = "udacity_plugin"
    operators = [
        operators.FactsCalculatorOperator,
        operators.HasRowsOperator,
        operators.S3ToRedshiftOperator
    ]
