import pyperclip
import os

# os.environ["PATH"] = "/var/run/host:" + os.environ["PATH"]
# os.environ["LD_LIBRARY_PATH"] =  "/var/run/host/usr/lib/x86_64-linux-gnu"
# os.system('echo text | xclip -sel clip')
# print(os.environ)

# for item in os.environ.items():
#     print(item)
pyperclip.copy('Hello, world!')
print(pyperclip.paste())

