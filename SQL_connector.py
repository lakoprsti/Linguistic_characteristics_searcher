import mysql.connector

from config import USER, HOST, PASSWORD

def connect_to_db(phonlang):
    cnx = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = phonlang
    )
    return cnx

def get_languages():
    try:
        db_name = 'phonlang'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f"Connected to {db_name}")

        query = "SELECT * FROM languages"
        cur.execute(query)
        result = cur.fetchall()

        for record in result:
            print(record)

        cur.close()

    except Exception:
        raise ConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("Db connection closed.")

get_languages()