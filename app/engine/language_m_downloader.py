import os
import gpt_2_simple as gpt2


if  os.path.isdir("/content/app/models/774M")== True:
    print("model exists")
else:
  os.chdir("/content/app/")
  print("downloading model")
  gpt2.download_gpt2(model_name="124M")
  gpt2.download_gpt2(model_name="774M")