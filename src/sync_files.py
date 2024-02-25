import ftplib
import json

def retrieve(host, files):
    ftp = ftplib.FTP(host)
    ftp.set_pasv("true")
    ftp.login()
    
    for file in files:
        with open(files, "wb") as f:
            ftp.retrievebinary("RETR {}".format(file), f.write)

    ftp.close()

with open("../settings.json") as f:
    settings_text = f.read()
    settings = json.loads(settings_text)
    host = settings["host"]
    root_path = settings["root_path"]

ftp = ftplib.FTP(host)
ftp.set_pasv("true")
ftp.login()

file_list = ftp.nlst(root_path)
print(file_list)

ftp.close()