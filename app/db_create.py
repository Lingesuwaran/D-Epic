import sqlite3

conn = sqlite3.connect('./data/data.db')

c = conn.cursor()

c.execute(""" CREATE TABLE game_creator_data(
          Game_name text PRIMARY KEY,
          Password text NOT NULL,
          Creator_name text NOT NULL,
          Story blob NOT NULL,
          text_color_1 text,
          text_color_2 text,
          text_color_3 text,
          background_color text,
          text_font text,
          button_color_1 text,
          button_color_2 text
          ) """)

conn.commit()
conn.close()