import os 
import pandas as pd
import sqlalchemy
import sys


def db_one():
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base = os.path.join(file, 'data')
    return base 


def base_csv():
    file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base = os.path.join(file, 'data')
    csv_dir = os.path.join(base, 'data-set-atualizado.csv')
    return csv_dir

try:
    df_tmp = pd.read_csv( db_one() , sep=';')
    table_name = 'tb_base'
    string_conetion = 'sqlite:///{path}'
    string_conetion = string_conetion.format( path=os.path.join(db_one, 'bancoset.db') )
    conection = sqlalchemy.create_engine( string_conetion )
    df_tmp.to_sql( name=table_name, con=conection, if_exists='replace' )
    
    
except Exception as e:
    print(e)