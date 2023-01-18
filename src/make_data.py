import sqlalchemy
import pandas as pd 
import os 
import sys 

sys.path.append('..')


filepath =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = os.path.join(filepath , 'data')
base_db = os.path.join(data, 'bank.csv')

try:
    df = pd.read_csv( base_db , sep=';')
    table_name = 'tb_base'
    string_conetion = 'sqlite:///{path}'
    string_conetion = string_conetion.format( path=os.path.join(data, 'dataset.db') )
    conection = sqlalchemy.create_engine( string_conetion )
    df.to_sql( name=table_name, con=conection, if_exists='replace' )
    
    
    
except Exception as e:
    print(e)