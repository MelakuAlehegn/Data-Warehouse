from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def my_function():
    print("Hello, Airflow!")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['melakualehegn@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'my_first_dag',
    default_args=default_args,
    description='my first dag',
    schedule_interval=timedelta(days=1),
)

t1 = PythonOperator(
    task_id='my_first_task',
    python_callable=my_function,
    dag=dag,
)

t1