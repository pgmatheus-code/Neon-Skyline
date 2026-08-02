import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        # get the name and serach for database, if didn't find, create one
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

        # create table for the first time
        self.conn.execute('''
                            CREATE TABLE IF NOT EXISTS dados 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            date TEXT NOT NULL)
                          '''
                         )

    def save(self, score_dict: dict):
        self.conn.execute('insert into dados (name, score, date)'
                          'values (:name, :score, :date)', score_dict)
        self.conn.commit()

    def retrieve_top10(self) -> list:
        return self.conn.execute('select * from dados order by score desc limit 10').fetchall()

    def close(self):
        return self.conn.close()