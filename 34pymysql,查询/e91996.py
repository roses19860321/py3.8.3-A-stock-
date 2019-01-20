#!/usr/bin/python3
import pymysql
sql1='select * from brand'
db=pymysql.connect("localhost","root","123456*","E91996")
cursor1=db.cursor()
cursor1.execute(sql1)
results=cursor1.fetchall()
print('id,factory,name,price,sum,sell,last')
for col in results:
    id=col[0]
    factory=col[1]
    name=col[2]
    price=col[3]
    sum=col[4]
    sell=col[5]
    last=col[6]
    print("%s,%s,%s,%s,%s,%s,%s"% (id,factory,name,price,sum,sell,last))
db.close()
