import secrets
import string
from django.conf import settings
import os

letters = string.ascii_letters
digits = string.digits
alphabet = letters + digits 
pwd_length = 12

def getpass():
 pwd = ''
 for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))
 return(pwd)

def add_pdf(post_image,report_id):
 image_name = ''
 image_path = settings.PDF_PATH
 if not os.path.exists(image_path):
  os.makedirs(image_path)
 image_name = None
 if post_image != '' and image_path != '' and report_id !='':
  try:
   filename = post_image.name
   filearr = filename.split('.')
   arr_len = len(filearr)
   if len(filearr) > 1 :
     file_name = filearr[0]
     file_ext = filearr[arr_len-1]

     image_name ="pdf_"+str(report_id)+"."+str(file_ext)
     imagefile = str(image_path)+str(image_name)
    
     with open(imagefile, 'wb+') as destination:
       for chunk in post_image.chunks():
         destination.write(chunk)
  except Exception as Error:
   pass
 return image_name

def add_ppt(post_image,report_id):
 image_name = ''
 image_path = settings.PPT_PATH
 if not os.path.exists(image_path):
  os.makedirs(image_path)
 image_name = None
 if post_image != '' and image_path != '' and report_id !='':
  try:
   filename = post_image.name
   filearr = filename.split('.')
   arr_len = len(filearr)
   if len(filearr) > 1 :
     file_name = filearr[0]
     file_ext = filearr[arr_len-1]

     image_name ="pdf_"+str(report_id)+"."+str(file_ext)
     imagefile = str(image_path)+str(image_name)
    
     with open(imagefile, 'wb+') as destination:
       for chunk in post_image.chunks():
         destination.write(chunk)
  except Exception as Error:
   pass
 return image_name

def add_excel(post_image,report_id):
 image_name = ''
 image_path = settings.EXCEL_PATH
 if not os.path.exists(image_path):
  os.makedirs(image_path)
 image_name = None
 if post_image != '' and image_path != '' and report_id !='':
  try:
   filename = post_image.name
   filearr = filename.split('.')
   arr_len = len(filearr)
   if len(filearr) > 1 :
     file_name = filearr[0]
     file_ext = filearr[arr_len-1]

     image_name ="pdf_"+str(report_id)+"."+str(file_ext)
     imagefile = str(image_path)+str(image_name)
    
     with open(imagefile, 'wb+') as destination:
       for chunk in post_image.chunks():
         destination.write(chunk)
  except Exception as Error:
   pass
 return image_name