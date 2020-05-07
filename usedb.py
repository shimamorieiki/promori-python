import sqlite3
from datetime import datetime as dt


def add_db(table, arr):

    conn = sqlite3.connect('./db/promoridb.sqlite3')
    c = conn.cursor()
    c.execute("insert into "+table+" values(" +
              arr[0] + ", '" + arr[1] + "', '" + arr[2] + "', '" +
              arr[3] + "', '" + arr[4] + "', '" + arr[5] + "')")
    conn.commit()
    conn.close()


def look_db_all(table):

    conn = sqlite3.connect('./db/promoridb.sqlite3')
    c = conn.cursor()
    c.execute("select * from " + table)
    data = c.fetchall()
    print(data)
    conn.commit()
    conn.close()


def look_db_itr(table):

    conn = sqlite3.connect('./db/promoridb.sqlite3')
    c = conn.cursor()
    for row in c.execute("select * from " + table):
        print(row)
    conn.commit()
    conn.close()


# def search_db_itr(table, id=True):

#     conn = sqlite3.connect('./db/promoridb.sqlite3')
#     c = conn.cursor()
#     for row in c.execute("select * from " + table):
#         print(row)
#     conn.commit()
#     conn.close()


def latest_date(table):
    conn = sqlite3.connect('./db/promoridb.sqlite3')
    c = conn.cursor()
    for row in c.execute("select * from " + table+" order by t_time desc"):
        ns = str(row[2])
        break
    conn.commit()
    conn.close()
    year = ns[0] + ns[1] + ns[2] + ns[3]
    month = ns[4] + ns[5]
    day = ns[6] + ns[7]
    hour = ns[8] + ns[9]
    minute = ns[10] + ns[11]
    second = ns[12] + ns[13]
    tstr = year + "-"+month+"-"+day+" "+hour+":"+minute+":"+second
    tdatetime = dt.strptime(tstr, '%Y-%m-%d %H:%M:%S')
    return tdatetime


if __name__ == "__main__":
    look_db_itr("tweets")
    # print(latest_date("tweets"))
