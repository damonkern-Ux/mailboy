import sqlite3
import json
import os


def initing():
    connection = sqlite3.connect("mailboy.db")
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS connections(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    method TEXT,
    url TEXT,
    headers TEXT,
    body TEXT,
    status_code INTEGER,
    response TEXT,
    response_time REAL
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def input_record(base,response):
    initing()
    connection = sqlite3.connect("mailboy.db")
    cursor = connection.cursor()
    print(response)

    cursor.execute("""
    INSERT INTO connections(method, url, headers, body, status_code, response, response_time)
    VALUES(?, ?, ?, ?, ?, ?, ?);""", (base[0],base[1],base[2],base[3],response["status"],json.dumps(response["body"]),response["response time"])
    )

    connection.commit()
    cursor.close()
    connection.close()

def get_history():
    initing()
    connection = sqlite3.connect("mailboy.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM connections;")
    output = cursor.fetchall()
    return output

def delete():
    initing()
    connection = sqlite3.connect("mailboy.db")
    cursor = connection.cursor()

    cursor.execute("DELETE FROM connections;")
    connection.commit()
    cursor.close()
    connection.close()
