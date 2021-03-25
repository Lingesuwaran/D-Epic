import shutil

list_dir = ["/content/app/data/data.db#..#/content/app/output/game_server/data/data.db","/content/app/engine/db_conn.py#..#/content/app/output/game_server/engine/db_conn.py",
            "/content/app/engine/app.html#..#/content/app/output/game_server/templates/app.html"]
for i in list_dir:
  data = i.split("#..#")
  original = data[0]
  target = data[1]
  shutil.copyfile(original, target)
dir_o = r"/content/app/checkpoint"
dir_t = r"/content/app/output/game_server/"
shutil.move(dir_o, dir_t)