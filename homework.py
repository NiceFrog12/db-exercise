#Импорт
from flask import Flask, render_template,request, redirect, url_for
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import sqlite3

#this is to read the database
df = pd.read_csv("./inventors.csv")


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
#Создание таблицы

class Inventor(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Заголовок
    name = db.Column(db.String(25), nullable=False)
    birthyear = db.Column(db.Integer, nullable=False)
    #Описание
    invention = db.Column(db.String(25), nullable=False)
    #Текст
    job = db.Column(db.String(25), nullable=False)

    #Вывод объекта и id
    def __repr__(self):
        return f'<Inventor {self.id}>'
"""AFTER MAKING A DATABASE, I KIND OF JUST CTRL+C CTRL+V'D IT INTO A .CSV FILE BECAUSE ITS EASIER TO WORK WITH AND IM TOO LAZY TO LEARN HOW TO USE CSV FILES RN"""    

#this is my attempt to re-do all the tasks using the actual database


#         THIS IS HOW TO WORK WITH A DATABASE LIKE YOU WOULD WITH A CSV FILE
#####################################################################
engine = create_engine('sqlite:///./instance/diary.db')
db = pd.read_sql_table('card', engine)


task1x = db['id'].max()
print(task1x)

task2x = db[db['birthyear'] == db['birthyear'].min()]['name'].tolist()
print(task2x)

task3x = db[db['job'] == 'gépészmérnök']['name'].tolist()
print(task3x)

if "transzformátor" not in db['invention']: #idk why you have to use "not" in it, but it doesnt seem to work otherwise
    task4x = db[db['invention'] == 'transzformátor']['name'].tolist()
    print(task4x)
else:
    print("nobody of those guys invented a transformator")

#"""SOLUTION FOR TASK 5"""
task5x = db[db['birthyear'] >= 1900]['name'].tolist()
#this is done to make it into a string
strtask5x = ", ".join(task5x)
with open('their_nameX.txt', 'w', encoding='utf-8') as file:
    file.write(strtask5x)

#####################################################################






def real():
    #"""SOLUTION FOR TASK 1"""
    task1 = df["number"].max()
    print(task1)

    #"""SOLUTION FOR TASK 2"""
    task2 = df[df['birthyear'] == df['birthyear'].min()]['names'].tolist()
    print(task2)

    #"""SOLUTION FOR TASK 3"""
    #engineer in hungarian: gépészmérnök (note for self)
    task3 = df[df['job'] == 'gépészmérnök']['names'].tolist()
    print(task3)

    #"""SOLUTION FOR TASK 4""" 
    if "transzformátor" not in df['invention']: #idk why you have to use "not" in it, but it doesnt seem to work otherwise
        task4 = df[df['invention'] == 'transzformátor']['names'].tolist()
        print(task4)
    else:
        print("nobody of those guys invented a transformator")

    #"""SOLUTION FOR TASK 5"""
    task5 = df[df['birthyear'] >= 1900]['names'].tolist()
    #this is done to make it into a string
    strtask5 = ", ".join(task5)
    with open('their_name.txt', 'w', encoding='utf-8') as file:
        file.write(strtask5)

