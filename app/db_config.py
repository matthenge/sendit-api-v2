"""Database configuration"""
import os
import psycopg2


db_url = os.getenv('DB_URL')
conn = psycopg2.connect('db_url')


def init_db():
    conn = connection('db_url')
    return conn

def create_tables():
    con = connection('db_url')
    curr = con.cursor()
    queries = tables()
    for query in queries:
        curr.execute(query)
        con.commit()

def destroy_tables():
    userdb = """DROP TABLE IF EXISTS users CASCADE"""
    orderdb = """DROP TABLE IF EXISTS orders CASCADE"""

def tables():
    userdb = """CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    firstname varchar NOT NULL,
    lastname varchar NOT NULL,
    user_role varchar,
    username varchar NOT NULL,
    email varchar NOT NULL,
    password varchar NOT NULL,
    date timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    )"""

    orderdb = """CREATE TABLE IF NOT EXISTS orders (
    order_id serial PRIMARY KEY NOT NULL,
    pickup_location varchar NOT NULL,
    destination varchar NOT NULL,
    status varchar NOT NULL,
    price numeric NOT NULL,
    weight numeric NOT NULL,
    date timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    )"""

    queries = [userdb, orderdb]
    return queries
    

