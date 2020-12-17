import sqlite3
from sqlite3 import Error
from mimesis import Person, Text, Datetime
import random

person = Person('en')
text = Text()
datetime = Datetime()


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_user_data(conn, insert_into_sql):
    sql = '''INSERT INTO twitteruser(username,password,displayname)
              VALUES(?,?,?);'''
    c = conn.cursor()
    c.execute(sql, insert_into_sql)
    conn.commit()


def insert_tweet_data(conn, insert_into_sql):
    sql = '''INSERT INTO tweet(user_id,message,created_at)
              VALUES(?,?,?);'''
    c = conn.cursor()
    c.execute(sql, insert_into_sql)
    conn.commit()


def notification_user_data(conn, insert_into_sql):
    sql = '''INSERT INTO notification(tweet_id, sent_from, user_mentioned)
              VALUES(?,?,?);'''
    c = conn.cursor()
    c.execute(sql, insert_into_sql)
    conn.commit()


def drop_tables(conn, drop_table):
    try:
        c = conn.cursor()
        c.execute(f'DROP TABLE IF EXISTS {drop_table}')
    except Error as e:
        print(e)


def random_user_id(conn, random_num):
    try:
        c = conn.cursor()
        user_id = c.execute(f'SELECT user_id FROM tweet WHERE id={random_num}')
    except Error as e:
        print(e)
    return user_id.fetchone()[0]


def main():
    database = "twitterclone.db"
    sql_create_twitteruser_table = """CREATE TABLE IF NOT EXISTS twitteruser(
                                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      username text NOT NULL,
                                      password text NOT NULL,
                                      displayname text NOT NULL
                                      ); """

    sql_create_tweet_table = """CREATE TABLE IF NOT EXISTS tweet(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                message text NOT NULL,
                                created_at TIMESTAMPZ
                                ); """

    sql_create_notification_table = """CREATE TABLE IF NOT EXISTS notification(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        tweet_id INTEGER NOT NULL,
                                        sent_from INTEGER NOT NULL,
                                        user_mentioned INTEGER NOT NULL,
                                        message_seen BOOL DEFAULT 'f'
                                        ); """
    conn = create_connection(database)
    drop_tables(conn, "twitteruser")
    drop_tables(conn, "tweet")
    drop_tables(conn, "notification")

    if conn is not None:
        create_table(conn, sql_create_twitteruser_table)

        create_table(conn, sql_create_tweet_table)

        create_table(conn, sql_create_notification_table)

    else:
        print("Error, cannot create the database connection")

    for _ in range(500):
        sql_insert_into_twitteruser = (person.username(template=None),
                                       person.password(length=10, hashed=False),
                                       person.full_name(gender=None, reverse=False))
        insert_user_data(conn, sql_insert_into_twitteruser)

    for _ in range(1000):
        sql_insert_into_tweet = (random.randint(1, 500),
                                 text.text(quantity=1),
                                 datetime.timestamp())

        insert_tweet_data(conn, sql_insert_into_tweet)

    random_tweet_id = random.randint(1, 1000)
    sent_to = random.randint(1, 500)

    for _ in range(200):
        sql_insert_into_notification = (random_tweet_id,
                                        random_user_id(conn, random_tweet_id),
                                        sent_to)

        notification_user_data(conn, sql_insert_into_notification)


if __name__ == '__main__':
    main()
