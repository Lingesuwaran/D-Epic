import sqlite3

def convertToBinaryData(filename):
      # Convert digital data to binary format
      with open(filename, 'rb') as file:
          blobData = file.read()
      return blobData

def writeTofile(data):
    # Convert binary data to proper format and write it on Hard Disk
    with open("./data/data.txt", 'wb') as file:
      blobData = file.write(data)
    return blobData
    

class Database:

  def insertBLOB(game_name, password, creator_name, txt):
      try:
          sqliteConnection = sqlite3.connect('./data/data.db')
          cursor = sqliteConnection.cursor()
          print("Connected to SQLite")
          sqlite_insert_blob_query = """ INSERT INTO game_creator_data
                                    (Game_name,Password,Creator_name,Story) VALUES (?, ?, ?, ?)"""

          Story = convertToBinaryData(txt)
          # Convert data into tuple format
          data_tuple = (game_name, password, creator_name, Story)
          cursor.execute(sqlite_insert_blob_query, data_tuple)
          sqliteConnection.commit()
          print("Image and file inserted successfully as a BLOB into a table")
          cursor.close()

      except sqlite3.Error as error:
          print("Failed to insert blob data into sqlite table", error)
      finally:
          if sqliteConnection:
              sqliteConnection.close()
              print("the sqlite connection is closed")

  def readBlobData(Game_name):
    try:
        sqliteConnection = sqlite3.connect('./data/data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from game_creator_data where Game_name = ?"""
        cursor.execute(sql_fetch_blob_query, (Game_name,))
        record = cursor.fetchall()
        Story = None
        for row in record:
            Story = row[3]
        
        writeTofile(Story)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")
#db=Database.readBlobData("1")
#db = Database.insertBLOB("Smith","Smith","Smith", "./data/story.txt")