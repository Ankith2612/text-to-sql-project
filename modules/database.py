# database.py
import sqlite3
from config import SQLITE_DB_PATH, CREATE_SQL_PATH

class DatabaseManager:
    def __init__(self, db_path=SQLITE_DB_PATH):
        self.db_path = db_path
        self.conn = None

    def initialize_db(self, init_sql_path=CREATE_SQL_PATH):
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        with open(init_sql_path, 'r') as f:
            sql_script = f.read()
        self.conn.executescript(sql_script)
        print("Inside initialize_db")
        self.conn.commit()

    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        return self.conn

    def execute_query(self, query, params=None):
        if not self.conn:
            self.connect()
        cursor = self.conn.cursor()
        cursor.execute(query, params or [])
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None