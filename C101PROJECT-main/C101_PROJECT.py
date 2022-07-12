import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.A6mQztexIk5oUv3rvTJXMXAAkVIw206m5tn_45C2MCayEzTWECyKEnJOaIprJ-7-0TPelU2y81mPJdTRYQiJYOWI9CST6AY_ycJB5uYYhRyTtzboOTW8hv2NlLrU99u9VpqITXk'
    transferData = TransferData(accessToken)
    fileFrom = str(input("Enter the folder path which you want to transfer:- "))
    fileTo = input("Enter the path to upload to dropbox:- ")
    transferData.uploadFile(fileFrom, fileTo)
    print("File has been transferred to your desired place")

main()