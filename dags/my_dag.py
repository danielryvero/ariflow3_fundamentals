from airflow.sdk import dag, task, chain
from pendulum import datetime
from airflow.providers.standard.operators.python import PythonOperator

def _task_a():
    print("Hello from task A")

@dag(
    schedule="@daily",
    start_date=datetime(2026, 1, 1), 
    description="this is me trying airflow 3.0 out",
    tags=["team_a", "source_a"],
    max_consecutive_failed_dag_runs=3
)

def my_dag():
    task_a = PythonOperator(
        task_id="task_a",
        python_callable=_task_a        
    )

    @task
    def task_b():
        print("hello world from airflow task B")
        
    @task
    def task_c():
        print("hello world from airflow task C")        
    
    @task
    def task_d():
        print("hello world from airflow task D") 

    @task
    def task_e():
        print("hello world from airflow task E")  
        
    @task
    def task_f():
        print("hello world from airflow task F")                    
    
    #standard bigshift operator method
    #task_a >> task_b() >> [task_c(), task_d()]

    #splitting into a variable so you can get the correct flow
    # a=task_a
    # a >> task_b() >> task_c()
    # a >> task_d() >> task_e()

    #chain method
    #chain(task_a, [task_b(), task_c()], [task_d(), task_e()])
    [task_a, task_b()] >> task_c() >> [task_d(), task_e()] >> task_f()
my_dag()