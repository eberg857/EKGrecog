import wfdb
import os

def download():
    try:
        wfdb.dl_database('mitdb', os.getcwd() +'\mitdb')
    except:
        print("donwload fucked")

if __name__ == "__main__":
    download()  


