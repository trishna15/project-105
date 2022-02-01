import os
import shutil

source = input("Enter the source name of file:")
destination = input("Enter the destination of the file:")

source = source + "/"
destination = destination + "/"

files = os.listdir(source)

for i in files :
    shutil.copy((source + i), destination)