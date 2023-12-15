def Palindrom():
    str = input("Введите строку: ").lower()
    print("Палиндром" if str.replace(" ","") == ''.join(reversed(str)).replace(" ","") else "Не палиндром")


def MIN():
    matrix = list()
    s = input()
    while (s != 'end'):
        matrix.append((list(map(int, s.split(' ')))))
        s = input()
    for row in matrix:
        print(min(row))



def WaP():
    name = input().lower().split(' ')
    d = dict()
    for i in name:
        d[i] = name.count(i)
    k = 0
    for i in d.items():
        k += 1
        print(k, ") ", i, " : ", d.get(i), end="\n")

def mysql():
    import pymysql
    import cryptography
    connect = pymysql.connect(host="127.0.0.1", user="root", password="pass", db="my_db")
    year = "1981"
    sql = "select * from user where YEAR(date_of_birth)=%s"
    cur = connect.cursor()
    cur.execute(sql,year)

    for i in cur:
        print(i[0],i[1])

mysql()