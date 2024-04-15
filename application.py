#Oceanofpeople app - A simple crud app that manage data of employees, student, workers along with names, email, number and a photo.
#Technologies Used in this Project - Flask, sqlite3, 

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

#Function to create database if not already exists

def create_table():
  conn = sqlite3.connect('data.db')
  c = conn.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number TEXT NOT NULL,
            email TEXT NOT NULL,
            work TEXT NOT NULL,
            department TEXT NOT NULL,
            department TEXT NOT NULL,
            photo TEXT NOT NULL
  )''')