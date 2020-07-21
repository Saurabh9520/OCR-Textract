import boto3
from trp import Document

# Document
s3BucketName = "bucket name here"
documentName = "image name"

# Amazon Textract client
textract = boto3.client('textract')

# Call Amazon Textract
response = textract.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    },
    FeatureTypes=["TABLES"])

#print(response)

doc = Document(response)

for page in doc.pages:
     # Print tables
    for table in page.tables:
        for r, row in enumerate(table.rows):
            for c, cell in enumerate(row.cells):
                print(cell)
                data=str(cell)

print(doc)
