import psycopg2
import random

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

def insert_transaction(amount, sender, recipient=None):
    new_user = 'INSERT INTO users (number) VALUES (%s)'
    transaction = 'INSERT INTO transactions (uri, amount, sender, recipient) '
    transaction += 'VALUES (%s, %s, %s, %s)'
    get_user = 'SELECT id FROM users WHERE number = %s LIMIT 1'
    url = random_url()
    if not recipient:
        recipient = sender
    with dbconn() as cur:
        cur.execute(get_user, (recipient,))
        recipient_id = cur.fetchone()
        if not recipient_id:
            cur.execute(new_user, (recipient,))
            cur.execute(get_user, (recipient,))
            recipient_id = cur.fetchone()
        cur.execute(transaction, (url, amount, sender, recipient_id))
    return url

def get_amount(transaction_uri):
    url_fetch = "SELECT amount FROM transactions WHERE uri = %s"
    with dbconn() as cur:
        cur.execute(url_fetch, (transaction_uri,))
        return cur.fetchone()[0]

def mark_as_payed(transaction_uri):
    update_is_payed = "UPDATE transactions SET is_payed=True WHERE uri=%s"
    with dbconn() as cur:
        cur.execute(update_is_payed, (transaction_uri,))

def is_payed(transaction_uri):
    select_is_payed = "SELECT is_payed FROM transactions WHERE uri=%s"
    with dbconn() as cur:
        cur.execute(select_is_payed, (transaction_uri,))
        return cur.fetchone()[0]

def get_transaction_parts(transaction_uri):
    select_transaction = "SELECT sender, users.number AS payer, amount FROM "
    select_transaction += "transactions INNER JOIN users ON users.id "
    select_transaction += "= transactions.recipient WHERE transactions.uri=%s"
    with dbconn() as cur:
        cur.execute(select_transaction, (transaction_uri,))
        return cur.fetchone()

def random_url():
    adjectives = []
    nouns = []
    with open('data/adjectives.txt', 'r') as f:
        adjectives = list(map(lambda x: x.strip(), f))
    with open('data/nouns.txt', 'r') as f:
        nouns = list(map(lambda x: x.strip(), f))
    return '%s-%s%03d' % (
                            random.choice(adjectives),
                            random.choice(nouns),
                            random.randint(0, 999)
                        )

if __name__ == '__main__':
    drop_database()
    create_database()
    pass
