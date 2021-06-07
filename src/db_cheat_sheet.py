import os
import pandas as pd


# I'm using this to look at the data description and make easier the
# manually creation of all tables needed.


def describe_data(data):
    print(f"Shape: {data.shape}")
    print(f"Duplicates: {data.duplicated().any()}")

    is_na = data.isna().sum()
    is_na_percentage = data.isna().sum() / data.shape[0] * 100
    nan_data_frame = pd.concat([data.dtypes, is_na, is_na_percentage], axis=1)
    nan_data_frame.columns = ['data_types', 'nan_count', 'nan_percentage']
    return nan_data_frame


def helper_describe_tables():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    files_names = [file for file in os.listdir(DATA_DIR) if file.endswith('.csv')]
    for file_name in files_names:
        table_name = file_name.replace("olist_", "").replace("_dataset.csv", "")
        df_temp = pd.read_csv(os.path.join(DATA_DIR, file_name))
        print(f"Table name: {table_name}. \n{describe_data(df_temp)}")
        print("-" * 100, "\n")


def helper_show_select_query_results(db, table):
    db.cursor.execute(f"SELECT * FROM {table};")
    rows = db.cursor.fetchmany(5)
    for row in rows:
        print(row)