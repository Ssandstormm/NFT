
from flask import Flask, request,render_template,jsonify,redirect,url_for
import sqlite3

app = Flask(__name__)




@app.route('/', methods = ['POST', 'GET'])
def data():
    return render_template('form.html')
     


if __name__ == "__main__":

    app.run(debug=True)
import requests




nft = input

url = f"https://solana-gateway.moralis.io/nft/mainnet/{nft}/metadata"



headers = {

    "accept": "application/json",

    "X-API-Key": "qoTYAokKqHK6xS5e0Zbq3qg2kh2uUzy4FfObczDjE5VdBa9Pi87PDxRl3RV54Fpc"

}



response = requests.get(url, headers=headers)



print(response.json)

@app.route('/json-data/')
def json_data():
    # get number of items from the javascript request
    nitems = request.args.get('1', 2)
    # query database
    cursor = g.db.execute('select * from items limit ?', (1,))
    # return json
    return jsonify(dict(cursor.fetchall(), start=1))



import psycopg2

connection = psycopg2.connect(database="NFT", user="postgres", password="550215", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * from nfts")

# Fetch all rows from database
record = cursor.fetchall()
 
print("Data from Database:- ", record)
connection.close()