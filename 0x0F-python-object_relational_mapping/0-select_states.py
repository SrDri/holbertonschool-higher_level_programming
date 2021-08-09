#!/usr/bin/python3
""" Lists all states """

if __name__ == "__main__":
    from sys import argv as argv

    if len(argv) < 4:
        print("Error: this script requires 3 arguments")
        exit()

    import MySQLdb

    host = "localhost"
    port = 3306
    user = argv[1]
    passwd = argv[2]
    db = argv[3]

    connection = MySQLdb.connect(host, user, passwd, db, port)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        print(row)
