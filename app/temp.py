import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

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

insertBLOB("Smith","Smith","Smith", "./data/story.txt")