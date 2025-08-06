# AWS Lambda S3 Reader Project

## 📌 Project Overview
This project demonstrates how to use **AWS Lambda** to read a file from an **S3 bucket** using Python (Boto3).  
The Lambda function retrieves the content of a text file from S3 and returns it as output.

---

## 🛠️ Services Used
- **AWS Lambda** – Serverless compute to run the Python code.
- **Amazon S3** – To store and retrieve the test file.
- **IAM** – To grant Lambda permissions to access S3.

---

## 📂 Project Steps
1. **Created an IAM Role** with `AmazonS3ReadOnlyAccess`.
2. **Created an S3 bucket** and uploaded `lambda-test.txt`.
3. **Created a Lambda Function** with Python 3.9 runtime.
4. **Attached IAM Role to Lambda** to allow S3 access.
5. **Created a test event** in Lambda and verified the function retrieves the file content.

---

## ✅ Test Output
Lambda successfully returned the following file content:

"This is Project 4 test file for AWS Lambda access."


---

## 📸 Screenshots
Below are key screenshots of the project:

1. **Lambda Test Event Creation**
   ![Test Event Screenshot](screenshots/lambda-test-event.png)

2. **Lambda Code Execution**
   ![Lambda Execution Screenshot](screenshots/lambda-execution.png)

3. **Successful Output**
   ![Lambda Success Output](screenshots/lambda-success-output.png)

---

## 🧰 Tech Stack
- Python 3.9
- AWS Lambda
- AWS S3
- AWS IAM
