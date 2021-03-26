import pyfiglet 
from colorama import Fore, Back, Style  #Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
                                        #Style: DIM, NORMAL, BRIGHT, RESET_ALL
import gpt_2_simple as gpt2
import os
from engine.db_conn import Database
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 


def generator(data_1,data_2,data_3):

  game_name = data_1
  epoch = data_2
  model = data_3
  db=Database.readBlobData(game_name)
  file_name = "./data/data.txt"

  g=pyfiglet.figlet_format("Generating world...", font = "slant")
  print(Fore.BLACK + Style.DIM)
  
  print(Fore.GREEN)
  print(Style.BRIGHT+g)
  print(Fore.BLACK + Style.DIM)
  sess = gpt2.start_tf_sess()

  sample = gpt2.finetune(
        sess,
        dataset  = file_name,
        model_name = data_3,
        steps=epoch,
        restore_from='fresh',
        run_name = "run1",
        print_every = 1,
        sample_every = epoch,
        save_every = epoch         
                  )
  return sample

def loader(game_name):
  print(Fore.GREEN)
  l=pyfiglet.figlet_format("Loading...", font = "slant")
  print(Style.BRIGHT+l)
  print(Fore.RESET)
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess)

  
  input1 = "I am Leo"
  stories = gpt2.generate(sess,
                length=250,
                temperature=0.7,
                prefix=input1,
                nsamples=5,
                batch_size=5,
                top_k=40,
                return_as_list=True
                )
    
  print(Fore.RESET + Style.RESET_ALL)
  story = ""
  temp = stories[3].split(".")
  del temp[-1]
  for i in temp:
    story = story +i+'.'
  return str(story)

def loader1(game_name,input1):
  print(Fore.GREEN)
  l=pyfiglet.figlet_format("Loading...", font = "slant")
  print(Style.BRIGHT+l)
  print(Fore.RESET)
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess)

  stories = gpt2.generate(sess,
                length=100,
                temperature=0.7,
                prefix=input1,
                nsamples=5,
                batch_size=5,
                top_k=40,
                return_as_list=True
                )
    
  print(Fore.RESET + Style.RESET_ALL)
  story = ""
  temp = stories[3].split(".")
  del temp[-1]
  for i in temp:
    story = story +i+'.'
  return str(story)



