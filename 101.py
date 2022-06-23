import cv2
import dropbox
import time
import random
 
start_time = time.time()
def upload_file(img_name):
     access_token = 'sl.BIZoyfdOHyUZFB2n2QP-8grbyQNex0ahjX44kVTlTaCcoKBukt8AXjGPKyRZOIf_fbgB7vcNKn2v9CHjlAbYN9YxOmALbCHIFzj6pC8LF9r4EpE3AZB95gZaqEUTd80xun3MGUQ'
     file = img_name
     file_from = file
     file_to = "/newFolder1/" + (img_name)
     dbx = dropbox.Dropbox(access_token)

     with open(file_from, 'rb' ) as f:
        dbx.files_upload(f.read(), file_to, mode= dropbox.files.WriteMode.overwrite)
        print("file uploaded")
def takesnap():

    number = random.randint(0,100)
    v=cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame=v.read()
        print(ret)

        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken!")
    v.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time() - start_time) >= 300):
            name = takesnap()
            upload_file(name)
main()