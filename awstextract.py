#extract data from image using aws txtract

import boto3
from trp import Document

# Document
s3BucketName = "your bucket name here"
documentName = "img.png"


# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.detect_document_text(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    })


text = ""
dict2=[]
for item in response["Blocks"]:
    if item["BlockType"] == "LINE":
        print (  item["Text"] )
        text += item["Text"]
        dict2.append(item["Text"])

#print(text)
list2=[]

for dl in dict2:
    sub=dl.split(',')
    list2.append(sub)
#print(list2)
list2.pop(5)


values = [] 
keys = [] 
for i in range(1, len(list2)): 
    if i % 2: 
        keys.append(list2[i]) 
    else : 
        values.append(list2[i])
print(key)
print(values)