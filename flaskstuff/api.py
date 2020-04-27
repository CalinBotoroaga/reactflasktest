import time
import random

from flask import Flask

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shortshort",
    database="testdb"
)
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cooltable(
theid INTEGER(10) PRIMARY KEY, 
name VARCHAR(100) 
)""")

app = Flask(__name__)

app.config['FLASK_ENV'] = 'development'


@app.route('/time')
def get_current_time():
    cursor.execute("SELECT * FROM cooltable")

    return {'time': cursor.__iter__().__next__()[1]}


if __name__ == "__main__":
    app.run(debug=True)
