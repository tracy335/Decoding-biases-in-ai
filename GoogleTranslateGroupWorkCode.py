
#Google Translate API
#Group Work Decoding Bias in AI Code 


#Access Google Translate API and import relevant packages

import sys
import csv

import numpy as np
! pip install google.cloud-translate==2.0.1
! pip install --upgrade google-cloud-translate 


import os    
from google.cloud import translate_v2 as translate


#immer wieder neu den file hochladen und pfad verlinken
credential_path = "PERSONAL_CREDENTIALPATH.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


translate_client = translate.Client()

import panda as pd

#upload english list of jobs per category (eg. "Comupter Jobs Eng")

df = pd.read_csv("JOB LIST.csv")

#create a list of the "English Profession" column

Profession_list = df ["English Profession"].tolist()

#translate list into Vietnamese (vi) 

text = Profession_list
target = 'vi'
translation = translate_client.translate(text, target_language=target)

#export the translated list as a csv file (eg. ComputerProfessionVI.csv)

import csv
data = [translation]
file = open('JOBCATEGORYProfessionVI.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(data)

#translate list into Japanese (ja)

text = Profession_list
target = 'ja'
translation = translate_client.translate(text, target_language=target)

#export the translated list as a csv file (eg. ComputerProfessionJA.csv)

import csv
data = [translation]
file = open('JOBCATEGORYProfessionJA.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(data)

#repeat this for all job category files in english with both japanese and vietnamese (corporate jobs, computer jobs, health jobs, service jobs, science jobs, artistic jobs)

#translate all the japanese lists into english and export each as a csv

df = pd.read_csv("JOBCATEGORYProfessionJA.csv")
ProfessionCATEGORYJapan_list= df [Profession Japan"].tolist()

text = ProfessionCATEGORYJapan_list
target = 'en'
translation = translate_client.translate(text, target_language=target)

data = [translation]
file = open('JOBCATEGORYProfessionJAENG.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(data)

#translate all the vietnamese lists into english and export each as a csv
df = pd.read_csv("JOBCATEGORYProfessionVI.csv")
ProfessionCATEGORYVietnam_list= df [Profession Vietnam"].tolist()

text = ProfessionCATEGORYVietnam_list
target = 'en'
translation = translate_client.translate(text, target_language=target)

data = [translation]
file = open('JOBCATEGORYProfessionVIENG.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    write.writerows(data)

#count the number of "she" and "he" per category and create percentage for both female and male  (using excel)