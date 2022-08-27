from datetime import datetime
import os
import dill
import json
import pandas as pd

path = os.environ.get('PROJECT_PATH', 'C:/Homework/airflow_hw')
file_pipe = os.listdir(f'{path}/data/models/')
file_test = os.listdir(f'{path}/data/test/')


def predict():
    df_final = pd.DataFrame()
    with open(f'{path}/data/models/{file_pipe[0]}', 'rb') as file:
        model = dill.load(file)
    for i in file_test:
        with open(f'{path}/data/test/{i}') as test:
            form = json.load(test)

        df = pd.DataFrame.from_dict([form])
        y = model.predict(df)
        df['predict'] = y
        df_final = pd.concat([df_final, df], ignore_index=True)
        print(df_final)

    df_final.to_csv(f'{path}/data/predictions/preds_{datetime.now().strftime("%Y%m%d%H%M")}.csv')





if __name__ == '__main__':
    predict()
