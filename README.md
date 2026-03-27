# Data pileline aws 


📊 Serverless Student Data Pipeline using AWS

📌 Project Overview

This project is a Serverless Data Pipeline built using AWS services to store, manage, and retrieve student data efficiently.
The system allows users to add, fetch, search, and delete student records through a web dashboard. The backend uses AWS Lambda, API Gateway, and DynamoDB, while the frontend is hosted on Amazon S3.

The pipeline also supports bulk data import from Amazon S3 into DynamoDB, making it suitable for handling structured datasets.


┌──────────────────────────┐
                │        User              │
                │   (Web Browser)          │
                └──────────┬───────────────┘
                           │
                           ▼
                ┌──────────────────────────┐
                │   Frontend Dashboard     │
                │   (Hosted on Amazon S3)  │
                └──────────┬───────────────┘
                           │ API Request
                           ▼
                ┌──────────────────────────┐
                │      API Gateway         │
                │  (CORS Enabled, REST)   │
                └──────────┬───────────────┘
                           │ Lambda Proxy
                           ▼
                ┌──────────────────────────┐
                │      AWS Lambda          │
                │     (Python Code)        │
                │  CRUD Operations         │
                └──────────┬───────────────┘
                           │
                           ▼
                ┌──────────────────────────┐
                │      DynamoDB            │
                │  Students Table          │
                │  Auto Scaling Enabled    │
                └──────────┬───────────────┘
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
┌──────────────────┐               ┌──────────────────┐
│    Amazon S3     │               │       IAM        │
│ (Bulk Data File) │               │   Roles & Policy │
│ Import to DB     │               │ Secure Access    │
└──────────────────┘               └──────────────────┘


🎯 Project Objectives

Build a serverless data pipeline using AWS
Store student data in DynamoDB
Provide REST APIs using API Gateway
Process requests using AWS Lambda (Python)
Enable bulk data import from S3
Host frontend dashboard using Amazon S3
Ensure scalability using DynamoDB Auto Scaling



🏗️ Architecture Overview

Flow of Data:

User interacts with Dashboard (Frontend hosted on S3)
Dashboard sends request to API Gateway
API Gateway triggers AWS Lambda
Lambda processes request using Python code
Lambda performs CRUD operations on DynamoDB
Data is stored or retrieved from DynamoDB
Response is sent back to Dashboard
Additionally:
Student data can be imported into DynamoDB using S3 Import
IAM roles manage secure access between services
DynamoDB uses Auto Scaling for performance



🧰 AWS Services Used

Amazon DynamoDB — NoSQL database to store student records
AWS Lambda — Backend logic written in Python
Amazon API Gateway — REST API management
Amazon S3 —
Frontend hosting
Bulk data import source

AWS IAM — Secure role-based access control



📂 Data Model (DynamoDB)

Table Name: StudentRecord

Attributes:    Attribute          Type         Description

               student_id         String       Unique student ID (Primary Key)
               name               String       Student Name
               email              String       Student Email



🔐 IAM Configuration
IAM roles were created to allow secure communication:
Lambda IAM Role
Access to DynamoDB
Logging permissions (CloudWatch)
DynamoDB Access Role
Allows read/write operations





⚙️ Lambda Function Details

Language: Python

Lambda handles:

POST → Add student data
GET → Fetch student data
DELETE → Remove student data
SEARCH → Find specific student


Lambda Function (Python)
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentRecord')

def lambda_handler(event, context):
  
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET,POST,DELETE,OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    try:
        method = event.get('httpMethod')
        
        if method == 'GET':
           
            response = table.scan()
            items = response.get('Items', [])
            
            
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps(items)
            }
            
        elif method == 'POST':
            body = json.loads(event['body'])
            table.put_item(Item=body)
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps("Success")
            }
            
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps("Unsupported method")
        }

    except Exception as e:
        
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({"error": str(e)})
        }





🌐 API Gateway Configuration

API Gateway was configured to:
Use Lambda Proxy Integration
Enable CORS (Cross-Origin Resource Sharing)

Support REST methods:

Method       Purpose

POST         Add student
GET          Fetch all students
DELETE       Delete student
SEARCH       Find student

The API endpoint is used in the frontend dashboard to perform operations.




💻 Frontend Dashboard

Hosting: Amazon S3
Frontend features:
Add new student
Fetch all students
Delete student
Search student
Display student list
The dashboard communicates with API Gateway endpoints.




📥 Data Import from S3

Bulk student data can be uploaded to Amazon S3 and imported into DynamoDB.
Steps:
1. Upload JSON file to S3 bucket
2. Use DynamoDB Import from S3 feature
3. Data automatically loads into DynamoDB table



📈 DynamoDB Auto Scaling

Auto Scaling is enabled to:
Automatically adjust read/write capacity
Handle large numbers of requests
Maintain performance under load

Sample Test Data

JSON
{
  "student_id": "101",
  "name": "Aryan",
  "email": "aryan@example.com"
}



🔄 Data Flow Explanation

Step-by-step Workflow

1️⃣ User opens the Frontend Dashboard hosted on Amazon S3

2️⃣ User performs actions:
     Add Student
     Search Student
     Delete Student
     View All Students

3️⃣ Frontend sends request to:
   ➡️ API Gateway

4️⃣ API Gateway triggers:
   ➡️ AWS Lambda Function

5️⃣ Lambda executes Python code:
     POST → Insert data
     GET → Fetch data
     DELETE → Remove data
     SEARCH → Query data

6️⃣ Lambda interacts with:
    ➡️ DynamoDB (Students Table)

7️⃣ DynamoDB stores:
     Student ID
     Name
     Email

8️⃣ Response flows back:

DynamoDB → Lambda → API Gateway → Frontend → User


📥 Bulk Data Import Flow

This is your second data pipeline path:

JSON File → Amazon S3 → DynamoDB Import
Used for: Loading large student datasets
Initial database setup
Bulk updates


🔐 Security Layer

IAM Roles handle:
Lambda → DynamoDB access
API → Lambda permissions
Secure service communication


📌 Architecture Highlights

✅ Fully Serverless
✅ Auto Scaling Enabled
✅ REST API Based
✅ Secure IAM Access
✅ Highly Scalable
✅ Low Maintenance
✅ Supports Real-Time + Bulk Data
