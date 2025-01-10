from pony.orm import  Database

db = Database("postgres", host="localhost", port="5432", user="reg", password="reg", database="fcms")