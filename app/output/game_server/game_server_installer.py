import shutil

list_dir = ["/content/D-Epic/app/data/data.db#..#/content/D-Epic/app/output/game_server/data/data.db","/content/D-Epic/app/engine/db_conn.py#..#/content/D-Epic/app/output/game_server/engine/db_conn.py",
            "/content/D-Epic/app/engine/app.html#..#/content/D-Epic/app/output/game_server/templates/app.html","/content/D-Epic/app/engine/game.py#..#/content/D-Epic/app/output/game_server/engine/game.py"]
for i in list_dir:
  data = i.split("#..#")
  original = data[0]
  target = data[1]
  shutil.copyfile(original, target)
dir_o = r"/content/D-Epic/app/checkpoint"
dir_t = r"/content/D-Epic/app/output/game_server/"
shutil.move(dir_o, dir_t)