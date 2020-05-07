import sqlite3
conn = sqlite3.connect('./db/promoridb.sqlite3')
c = conn.cursor()
c.execute("insert into tweets values(2, '太郎', '20200507', '', '', '')")
c.execute('select * from tweets')
data = c.fetchall()
print(data)
conn.commit()
conn.close()
