from flask_ngrok import run_with_ngrok
from flask import Flask, render_template,request,redirect,session
import flask
from werkzeug.utils import secure_filename
import os
from engine.db_conn import Database
from engine import game
from multiprocessing import Pool,Process
import threading
import sqlite3
import shutil

app = Flask(__name__)
app.secret_key = "Hole"
run_with_ngrok(app)


UPLOAD_FOLDER = './data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def process(type_d):
  game_name = session["game_name"]
  #p1 = Process(target = game.generator(game_name,session["epoch"],session["model"]))
  if type_d ==1:
    p1 = threading.Thread(target = game.generator, args = (game_name,session["epoch"],session["model"]) )
    p1.start()
    p1.join()
    #p = game.generator(game_name,session["epoch"],session["model"])
  elif type_d == 0:
    p2 = game.loader(game_name)
    return p2
  elif type_d == 2:
    p1 = threading.Thread(target = game.generator, args = (game_name,session["epoch"],session["model"]) )
    #p1 = Process(target = game.generator(game_name,session["epoch"],session["model"]))
    p1.start()
  


@app.route('/')
def Menu():
  return render_template('index.html')

@app.route('/Configure',methods=["GET","POST"])
def Configure():
    if request.method =="POST":
      game_name = request.form["game_name"]
      password = request.form["password"]
      creator_name = request.form["creator_name"]

      session["game_name"] = game_name
      session["password"] = password
      session["creator_name"] = creator_name

      file = request.files['file']
      filename = "story.txt"
      #filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      
      db = Database.insertBLOB(game_name,password,creator_name, "./data/story.txt")
      #data = game.Play(game_name)
      session["epoch"] = 10
      session["model"] = '124M'
      process(1)
      return redirect("Dashboard")
    else:
      return render_template('Configure.html')

@app.route('/Existing_project',methods=["GET","POST"])
def Existing_project():
  if request.method =="POST":
      session["game_name"] = request.form["game_name"]
      session["password"] = request.form["password"]

      sqliteConnection = sqlite3.connect('./data/data.db')
      cursor = sqliteConnection.cursor()
      print("Connected to SQLite")
      sql_fetch_ = """SELECT * from game_creator_data where Game_name = ?"""
      cursor.execute(sql_fetch_, (session["game_name"],))
      password = None
      record = cursor.fetchall()
      for row in record:
        password = row[1]

      if session["password"] == password:
        return redirect("Dashboard")
      else:
        return "Game name or password incorrect"
  else:
    return render_template('Existing_project.html')

@app.route('/Help')
def Help():
  return render_template('Help.html')

@app.route('/Dashboard',methods= ["GET","POST"])
def Dashboard():
  if request.method =="POST":
    session["epoch"] = int(request.form["epoch"])
    session["model"] = str(request.form["model-name"])

    session["text-color-1"] = request.form["text-color-1"]
    session["text-color-2"] = request.form["text-color-2"]
    session["text-color-3"] = request.form["text-color-3"]

    session["background-color"] = request.form["background-color"]

    session["text-font"] = request.form["font"]

    session["button-color-1"] = request.form["button-color-1"]
    session["button-color-2"] = request.form["button-color-2"]
    sqliteConnection = sqlite3.connect('./data/data.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    #sql_fetch_="""INSERT INTO game_creator_data where Game_name = ?
                        #  (text_color_1, text_color_2, text_color_3, background_color, text_font,button_color_1,button_color_2) 
                         #  VALUES
                         # (?,?,?,?,?,?,?)"""
    sql_fetch_ = """UPDATE game_creator_data SET text_color_1 = ?, text_color_2 = ?,text_color_3 = ?,background_color=?,text_font=?,button_color_1=?,button_color_2=?
    
    WHERE Game_name = ?;
    
    """
    cursor.execute(sql_fetch_, (session["text-color-1"],session["text-color-2"],session["text-color-3"],session["background-color"],session["text-font"], session["button-color-1"], session["button-color-2"],session["game_name"]))
    sqliteConnection.commit()
    cursor.close()
    if  os.path.isdir("./checkpoint/run1")== True:
      try:
        shutil.rmtree("./checkpoint/run1")
      except OSError as e:
        print("Error: %s : %s" % ("./checkpoint/run1", e.strerror))
    process(2)
    #data = game.generator(session["game_name"],session["epoch"])
    return redirect("preview_1")
  else:
    data = process(0)
    return render_template("Dashboard.html",data = data)

@app.route('/preview_1')
def Preview_1():
  return "<h2>Preview</h2> under development"

app.run()