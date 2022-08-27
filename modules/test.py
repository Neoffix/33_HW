import os

path = os.environ.get('PROJECT_PATH', '.')
path1 = os.path.expanduser('~/airflow_hw')
print(path1)