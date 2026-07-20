import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ai_data_platform"
)

if connection.is_connected():
    print("Connected to MySQL successfully!")