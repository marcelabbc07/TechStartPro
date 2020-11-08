import MySQLdb
import csv

connection = MySQLdb.connect(host="localhost", user="root", password="", database="testetsp")
cursor = connection.cursor()

csv_data = csv.reader(open('categories.csv'))
header = next(csv_data)
for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO categories (name) VALUES (%s)", row)
connection.commit()
cursor.close()