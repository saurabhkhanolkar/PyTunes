import pymysql
import Transform as t
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import delete
from sqlalchemy.sql import text

engine=create_engine('RDS Endpoint/DBname',echo=False)
dfglobal=t.getdataglobal()
dfglobal.rname(columns = {'key': 'key1'}, inplace = True)
mycon=engine.connect()


delete_stmt = delete(text('GLOBALCURRENT'))
mycon.execute(delete_stmt)





#d = GLOBALCURRENT.delete()
#d.execute()

dfglobal.to_sql('GLOBALCURRENT',mycon,index = False,if_exists='append')
