import os
import sys

target = r"C:\Users\cjswh\Desktop\정리자료"
files = os.listdir(target)
sys.stdout = open('name.csv','w')

print("files.{}".format(files), end='\n')

sys.stdout.close()