import os
import speech
import recog

awsPrompt = """
Configure AWS
Create a Key-pair
Create a Security group
Launch an Instance
Create an EBS
Attach EBS
Create S3 bucket
Store files in S3 bucket
Go back to main menu """

def check(opt):
    if any(ele in opt for ele in do) and not any(ele in opt for ele in donot):
        return True
    return False

do = ["configure","run","start","open","launch","manage","configuration","excute", "create" , "make"]
donot = ["don't","do not","no"]


def aws():
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("AWS cli Operations".center(size.columns))
        speech.speak("here are the services provided")
        os.system("tput setaf 7; tput setab 0")

        print(awsPrompt)
        speech.speak("What can i do for you?")
        opt = recog.voice_rec()
        opt = opt.lower()

        os.system("tput clear")
        if check(opt) and "aws" in opt:
            os.system("aws configure")

        elif check(opt) and "key" in opt:
            speech.speak("give key pair a name")
            name = input("Enter the key name: ")
            os.system(f"aws ec2 create-key-pair --key-name {name}")
            speech.speak("key pair created")

        elif check(opt) in opt and "security" in opt:
            speech.speak("give security group a name")
            group_name = input("Enter the group name: ")
            speech.speak("give some description")
            description = input("Enter the description of security group: ")
            os.system(
                f'aws ec2 create-security-group --group-name {group_name} --description "{description}"')
            speech.speak("security group created")

        elif check(opt) and "instance" in opt:
            speech.speak("enter amazon machine image ID")
            ami = input("Enter the Amazon Machine Image ID: ")

            speech.speak("enter intance type")
            instance_type = input("Enter the instance type: ")

            speech.speak("enter number of instances")
            count = input("Enter the number of instances you want to launch: ")

            speech.speak("enter subnet id")
            subnet_id = input("Enter the subnet ID where you want to launch: ")

            speech.speak("enter key pair value")
            key_name = input("Enter the key pair value you want to use: ")

            speech.speak("enter the security group name")
            security_group = input(
                "Enter the security group name that you use: ")
            os.system(
                f"aws ec2 run-instances --image-id {ami} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --key-name {key_name} --security-group-ids {security_group}")
            speech.speak("instance launched")

        elif check(opt) and "ebs" in opt:
            speech.speak("enter availability zone")
            zone = input("Enter availability zone: ")

            speech.speak("enter the size")
            size = input("Enter the size: ")

            os.system(
                f"aws ec2 create-volume --availability-zone {zone} --no-encrypted --size {size}")
            speech.speak("EBS created")

        elif "attach" or "connect" in opt and "ebs" in opt:
            speech.speak("Enter instance ID")
            instance_id = input("Enter the Instance-ID: ")

            speech.speak("enter volume ID")
            vol_id = input("Enter the Volume-ID: ")

            os.system(
                f"aws ec2 attach-volume --instance-id {instance_id} --volume-id {vol_id} --device xvdh")

        elif check(opt) and "s3" in opt:
            speech.speak("give S3 bucket a name")
            name = input("Enter the name you want to give to bucket: ")

            speech.speak("enter the region")
            region = input("Enter the region: ")

            os.system = input(
                f"aws s3api create-bucket --bucket {name} --region {region} --create-bucket-configuration LocationConstraint={region}")

        elif "store" or "upload" in opt and "s3" in opt:
            speech.speak("Enter the name of the bucket")
            bucket = input("Enter the name of the bucket: ")

            speech.speak("enter the path of the object with name")
            file_object = input("Enter the path of the object with name: ")

            speech.speak("enter the name of the object you want to give to object in bucket")
            name_dir = input(
                "Enter the name which you want to give to the object when i will save in the bucket: ")

            os.system(
                f"aws s3api put-object --bucket {bucket} --key {name_dir} --body \"{file_object}\"")

        elif "exit" or "quit" or "back" in opt:
            return

        else:
            print("Invalid request")
            speech.speak("invalid request")
        os.system("tput clear")
