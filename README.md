## AWS Resource Automation Using Python



## Project Overview

This project automates common AWS resource management tasks using Python and the Boto3 SDK. It provides a menu-driven program to manage Amazon S3 buckets and Amazon EC2 instances.



## Technologies Used

- Python

- AWS Boto3

- Amazon S3

- Amazon EC2

- AWS CLI

- AWS IAM



## Features

- Create S3 buckets

- Upload files to S3

- List S3 buckets

- Launch EC2 instances

- List EC2 instances

- Start and stop EC2 instances

- Terminate EC2 instances with confirmation



## Project Structure

```text

project6/

├── aws\_automation.py

├── README.md

└── .gitignore

```



## Setup Instructions



1. Install Python 3.

2. Configure the AWS CLI with appropriate credentials.

3. Install Boto3:



&#x20;  ```bash

&#x20;  pip install boto3

&#x20;  ```



4. Run the application:



&#x20;  ```bash

&#x20;  python aws\_automation.py

&#x20;  ```



## AWS Configuration

The application uses the AWS Mumbai region (`ap-south-1`). Your AWS identity must have the necessary IAM permissions for the operations you perform.



## Cost and Security

- EC2 usage and other AWS resources may incur charges.

- Stop EC2 instances when they are not needed.
- Never upload AWS access keys, secret keys, or passwords to GitHub.

- Use IAM permissions following the principle of least privilege.



## Learning Outcomes

- AWS resource automation using Python and Boto3

- S3 bucket and file management

- EC2 instance management

- AWS API error handling



## Author

AWS Cloud Engineering Capstone Project

<img width="1536" height="1024" alt="AWS Python Automation Architecture" src="https://github.com/user-attachments/assets/f4617a36-ed7b-46a1-b8fd-b2b6204b78e3" />
