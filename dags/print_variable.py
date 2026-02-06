from airflow.sdk import dag, task, Variable

@dag(schedule=None)
def variable():

    @task
    def print_my_variable():
        print(Variable.get("api", deserialize_json=True))
        
    print_my_variable()
        
variable()                