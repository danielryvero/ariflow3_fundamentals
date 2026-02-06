from airflow.sdk import dag, task, DAG
from pendulum import datetime

with DAG(
    dag_id="my_dag2",
    schedule="@daily",
    start_date=datetime(2026, 1, 1), 
    description="this is me trying airflow 3.0 out",
    tags=["team_a", "source_a"],
    max_consecutive_failed_dag_runs=3
):
    
    @task
    def task_a():
        print("hello world from airflow")
    task_a()
    
    
with DAG(
    dag_id="my_dag2",
    schedule="@daily",
    start_date=datetime(2026, 1, 1), 
    description="this is me trying airflow 3.0 out",
    tags=["team_b", "source_b"],
    max_consecutive_failed_dag_runs=3
):
    
    @task
    def task_b():
        print("hello world from airflow erroring")
    task_b()    