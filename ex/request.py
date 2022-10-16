import psycopg2

connection = psycopg2.connect(database="NFT", user="postgres", password="550215", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SHOW DATABASE")

# Fetch all rows from database
record = cursor.fetchall()
 
print("Data from Database:- ", record)
connection.close()