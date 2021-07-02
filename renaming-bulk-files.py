#Python program that bulks the name of the files in a folder
import os

def main():
    i = 0 #by default assuming no. of files=0 to iterate over
    path = "C:/Users/Lenovo/Desktop/6 Python Projects/renaming-bulk-file-test/"
    for filename in os.listdir(path): #gets all the files stored in path as a list
        my_dest = "img" + str(i) + ".jpg" 
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i+=1

if __name__== '__main__':
    main()
    