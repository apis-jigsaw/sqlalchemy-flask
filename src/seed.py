import pandas as pd
from sqlalchemy import create_engine
conn_string = 'postgresql://jeffreykatz@localhost/moes_bar'
conn = create_engine(conn_string)
root_url = "./data/"
names = ['bartenders', 'customers', 'drinks', 'orders', 'ingredients', 'ingredients_drinks']
loaded_dfs = [pd.read_csv(f'{root_url}{name}.csv') for name in names]
for df, name in zip(loaded_dfs, names):
    df.to_sql(name, conn, if_exists='replace', index = False)