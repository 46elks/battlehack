import psycopg2

class dbconn:
    def __enter__(self):
        self.conn = psycopg2.connect(
                                     dbname='apini',
                                     user='apini',
                                     password='apini',
                                     host='127.0.0.1'
                                    )
        return self.conn.cursor()
    def __exit__(self, type, value, traceback):
        self.conn.commit()
        self.conn.close()


def drop_database():
    with dbconn() as cur:
        with open('sql/drop.sql', 'r') as drop:
            cur.execute(drop.read())

def create_database():
    with dbconn() as cur:
        with open('sql/create.sql', 'r') as create:
            cur.execute(create.read())

if __name__ == '__main__':
    #drop_database()
    #create_database()
    pass
