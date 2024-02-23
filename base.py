import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, queryType):
        db = psql.connect(
            database = os.getenv("DB_NAME"),
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD")
        )

        cursor = db.cursor()
        cursor.execute(query)

        queryData = ["insert","create","delete","update"]

        if queryType in queryData:
            db.commit()

            if queryType == "insert":
                return "INSERTED"
            elif queryType == "create":
                return "CREATED"
            elif queryType == "delete":
                return "DELETED"
            elif queryType == "update":
                return "UPDATED"
            
        else:
            return cursor.fetchall()

