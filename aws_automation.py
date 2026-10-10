
import boto3
from botocore.exceptions import ClientError

REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=REGION)
ec2 = boto3.client("ec2", region_name=REGION)


def create_bucket():
    name = input("Enter a globally unique S3 bucket name: ").strip()

    if not name:
        print("Bucket name cannot be empty.")
        return

    try:
        s3.create_bucket(
            Bucket=name,
            CreateBucketConfiguration={
                "LocationConstraint": REGION
            }
        )
        print(f"Bucket created successfully: {name}")
    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def upload_file():
    bucket = input("Enter S3 bucket name: ").strip()
    path = input("Enter full local file path: ").strip().strip('"')
    key = input("Enter S3 object name (or press Enter for filename): ").strip()

    if not key:
        key = path.replace("\\", "/").split("/")[-1]

    try:
        s3.upload_file(path, bucket, key)
        print(f"File uploaded successfully to s3://{bucket}/{key}")
    except (ClientError, OSError) as e:
        print("Upload failed:", e)


def list_buckets():
    try:
        response = s3.list_buckets()
        buckets = response.get("Buckets", [])

        if not buckets:
            print("No S3 buckets found.")
            return

        print("\nYour S3 buckets:")
        for bucket in buckets:
            print("-", bucket["Name"])
    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def launch_instance():
    print("\nLaunching EC2 can incur charges.")
    ami = input("Enter a valid AMI ID for ap-south-1: ").strip()
    key_name = input("Enter an existing EC2 key pair name: ").strip()
    subnet_id = input("Enter an existing subnet ID: ").strip()
    sg_id = input("Enter an existing security group ID: ").strip()
    instance_type = input("Instance type [t3.micro]: ").strip() or "t3.micro"

    confirm = input("Launch this instance? Type YES to continue: ")
    if confirm != "YES":
        print("Launch cancelled.")
        return

    try:
        response = ec2.run_instances(
            ImageId=ami,
            InstanceType=instance_type,
            KeyName=key_name,
            SubnetId=subnet_id,
            SecurityGroupIds=[sg_id],
            MinCount=1,
            MaxCount=1
        )
        instance_id = response["Instances"][0]["InstanceId"]
        print("EC2 launch requested:", instance_id)
    except ClientError as e:
        print("Launch failed:", e.response["Error"]["Message"])


def list_instances():
    try:
        response = ec2.describe_instances()
        found = False

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                found = True
                print(
                    f"ID: {instance['InstanceId']} | "
                    f"State: {instance['State']['Name']} | "
                    f"Type: {instance['InstanceType']}"
                )

        if not found:
            print("No EC2 instances found in this region.")
    except ClientError as e:
        print("Error:", e.response["Error"]["Message"])


def manage_instance(action):
    instance_id = input("Enter EC2 instance ID: ").strip()

    if not instance_id.startswith("i-"):
        print("Please enter a valid-looking EC2 instance ID.")
        return

    if action == "terminate":
        print("Warning: termination can permanently destroy instance data.")
        confirm = input(
            f"Type the exact instance ID {instance_id} to confirm: "
        )
        if confirm != instance_id:
            print("Termination cancelled.")
            return
    else:
        confirm = input(f"Type YES to {action} {instance_id}: ")
        if confirm != "YES":
            print("Operation cancelled.")
            return

    try:
        if action == "start":
            ec2.start_instances(InstanceIds=[instance_id])
        elif action == "stop":
            ec2.stop_instances(InstanceIds=[instance_id])
        elif action == "terminate":
            ec2.terminate_instances(InstanceIds=[instance_id])

        print(f"Request submitted: {action} {instance_id}")
    except ClientError as e:
        print("Operation failed:", e.response["Error"]["Message"])


def main():
    while True:
        print("""
========== AWS RESOURCE AUTOMATION ==========
1. Create S3 bucket
2. Upload file to S3
3. List S3 buckets
4. Launch EC2 instance
5. List EC2 instances
6. Start EC2 instance
7. Stop EC2 instance
8. Terminate EC2 instance
9. Exit
=============================================
""")

        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            create_bucket()
        elif choice == "2":
            upload_file()
        elif choice == "3":
            list_buckets()
        elif choice == "4":
            launch_instance()
        elif choice == "5":
            list_instances()
        elif choice == "6":
            manage_instance("start")
        elif choice == "7":
            manage_instance("stop")
        elif choice == "8":
            manage_instance("terminate")
        elif choice == "9":
            print("Exiting AWS Automation Tool.")
            break
        else:
            print("Invalid option. Please choose 1-9.")


if __name__ == "__main__":
    main()
