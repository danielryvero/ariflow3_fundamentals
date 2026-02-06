from airflow.sdk import dag, task, chain
from pendulum import datetime
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator

#part of the pythonOperator way
# def _task_a():
#      print(open('/tmp/dummy', 'rb').read())

@dag(
    # dag_id="check_dag",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    description="DAG to check data",
    tags=["team", "data_engineering"],
    max_consecutive_failed_dag_runs=3    
)
#part of the pythonOperator way
# def read_file():
#     task_a = PythonOperator(
#         task_id="task_a",
#         python_callable=_task_a
#     )
    
def check_dag():
    
    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy'

    @task.bash
    def check_file():
        return 'test -f /tmp/dummy'
        
    @task
    def read_file():
        print(open('/tmp/dummy', 'rb').read())
    
    create_file() >> check_file() >> read_file() 
       
check_dag()       
#part of the pythonOperator way    
# create_file() >> check_file() >> task_a
# read_file()