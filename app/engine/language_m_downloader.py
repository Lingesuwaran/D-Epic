import os
#import gpt_2_simple as gpt2


if  os.path.isdir("/content/D-Epic/app/models/774M")== True:
    print("model exists")
else:
  os.chdir("/content/D-Epic/app/engine")
  print("downloading model")
  os.system('sh model.sh')