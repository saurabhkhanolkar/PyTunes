import pymysql
import Transform as t
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import delete
from sqlalchemy.sql import text

engine=create_engine('mysql+pymysql://admin:12345678@database-1.cod1kdbr9qur.us-east-2.rds.amazonaws.com/Finaldb',echo=False)
dfglobal=t.getdataglobal()
dfglobal.rename(columns = {'key': 'key1'}, inplace = True)
mycon=engine.connect()


delete_stmt = delete(text('GLOBALCURRENT'))
mycon.execute(delete_stmt)





#d = GLOBALCURRENT.delete()
#d.execute()

dfglobal.to_sql('GLOBALCURRENT',mycon,index = False,if_exists='append')














































"""
engine=create_engine('mysql+pymysql://admin:12345678@database-1.cod1kdbr9qur.us-east-2.rds.amazonaws.com/trialagain',echo=False)

dfindia=t.getdataindia()
dfglobal=tg.getdataglobal()
#print(dfindia)
#print(dfglobal)
dfindia.rename(columns = {'key': 'key1'}, inplace = True)
dfglobal.rename(columns = {'key': 'key1'}, inplace = True)
#print(dfindia)
#print(dfglobal)
mycon=engine.connect()

#dfindia.to_sql('INDIATRACKSFINAL1',mycon,index = False,if_exists='append')
dfglobal.to_sql('GLOBALTRACKSFINAL',mycon,index = False,if_exists='append')





import pandas as pd
df=pd.read_sql_table('GLOBALTRACKSFINAL',engine)
print(df)
"""
