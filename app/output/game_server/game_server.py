from flask_ngrok import run_with_ngrok
from flask import Flask, render_template,request,redirect,session
import flask
from werkzeug.utils import secure_filename
import os
from engine.db_conn import Database
from engine import game
import sqlite3
 
app = Flask(__name__)
app.secret_key = "Hole"
run_with_ngrok(app)


def process():
  game_name = session["game_name"]
  input1 = session["input"]
  p2 = game.loader1(game_name,input1)
  return p2


@app.route('/',methods= ["GET","POST"])
def temp():
  if request.method =="POST":
    session["input"] = request.form["data"]
  else:
    session["game_name"] = input("Enter game name")
    session["input"] = "My name is "+ str(input("Enter character name"))
    sqliteConnection = sqlite3.connect('/content/D-Epic/app/output/game_server/data/data.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    #sql_fetch_="""INSERT INTO game_creator_data where Game_name = ?
                        #  (text_color_1, text_color_2, text_color_3, background_color, text_font,button_color_1,button_color_2) 
                         #  VALUES
                         # (?,?,?,?,?,?,?)"""
    sql_fetch_ = """SELECT * from game_creator_data where Game_name = ?"""
    cursor.execute(sql_fetch_, (session["game_name"],))
    record = cursor.fetchall()
    for i in record:
      session["text-color-1"] = i[4]
      session["text-color-2"] = i[5]
      session["text-color-3"] = i[6]
      session["background-color"] = i[7]
      session["text-font"] = i[8]
      session["button-color-1"] = i[9]
      session["button-color-2"] = i[10]
    cursor.close()
    
  
  data = session["game_name"]
  game_story = process()
  return render_template("app.html",text_color_1 = session["text-color-1"], text_color_2 = session["text-color-2"], text_color_3 = session["text-color-3"], background_color = session["background-color"], text_font = session["text-font"],button_color_1 = session["button-color-1"],button_color_2 = session["button-color-2"],data=data,game_story = game_story)

app.run()