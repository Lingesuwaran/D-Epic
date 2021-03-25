import csv

def names(data,name):
  text = data

  with open('/content/AGT_rpg/Books/names.csv') as file:
    csv_reader = csv.reader(file)
    for i in csv_reader:
      if i[1] in text:
        text = text.replace(i[1],i[0])
      elif "%Name%" in text:
        text = text.replace("%Name%",name)
    return text 