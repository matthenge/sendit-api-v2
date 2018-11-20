"""Database configuration"""
import psycopg2
import os


def tables():
    userdb = """CREATE TABLE IF NOT EXISTS users (
    user_id serial PRIMARY KEY NOT NULL,
    firstname character varying(50) NOT NULL,
    lastname character varying(50) NOT NULL,
    user_role character varying(15),
    username character varying(30) NOT NULL,
    email character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    date timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    )"""

    orderdb = """CREATE TABLE IF NOT EXISTS orders (
    order_id serial PRIMARY KEY NOT NULL,
    pickup_location character varying(50) NOT NULL,
    destination character varying(50) NOT NULL,
    status character varying(50) NOT NULL,
    price numeric NOT NULL,
    weight numeric NOT NULL,
    date timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    )"""

    queries = [userdb, orderdb]
    return queries

