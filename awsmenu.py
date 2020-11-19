import os

awsPrompt = """
Press 1 to configure AWS
Press 2 to create a Key-pair
Press 3 to create a Security group
Press 4 to launch an Instance
Press 5 to create an EBS
Press 6 to attach EBS
Press 7 to create S3 bucket
Press 8 to store files in S3 bucket
Press b to go back to main menu
Enter your choice here: """


def aws():
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("AWS cli Operations".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        x = input(awsPrompt)

        os.system("tput clear")
        if x == "1":
            os.system("aws configure")

        elif x == "2":
            name = input("Enter the key name: ")
            os.system(f"aws ec2 create-key-pair --key-name {name}")

        elif x == "3":
            group_name = input("Enter the group name: ")
            description = input("Enter the description of security group: ")
            os.system(
                f'aws ec2 create-security-group --group-name {group_name} --description "{description}"')

        elif x == "4":
            ami = input("Enter the Amazon Machine Image ID: ")
            instance_type = input("Enter the instance type: ")
            count = input("Enter the number of instances you want to launch: ")
            subnet_id = input("Enter the subnet id where you want to launch: ")
            key_name = input("Enter the key pair value you want to use: ")
            security_group = input(
                "Enter the security group name that you use: ")
            os.system(
                f"aws ec2 run-instances --image-id {ami} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --key-name {key_name} --security-group-ids {security_group}")

        elif x == "5":
            zone = input("Enter availability zone: ")
            size = input("Enter the size: ")

            os.system(
                f"aws ec2 create-volume --availability-zone {zone} --no-encrypted --size {size}")

        elif x == "6":
            instance_id = input("Enter the Instance-ID: ")
            vol_id = input("Enter the Volume-ID: ")

            os.system(
                f"aws ec2 attach-volume --instance-id {instance_id} --volume-id {vol_id} --device xvdh")

        elif x == "7":
            name = input("Enter the name you want to give to bucket: ")
            region = input("Enter the region: ")

            os.system = input(
                f"aws s3api create-bucket --bucket {name} --region {region} --create-bucket-configuration LocationConstraint={region}")

        elif x == "8":
            bucket = input("Enter the name of the bucket: ")
            file_object = input("Enter the path of the object with name: ")
            name_dir = input(
                "Enter the name which you want to give to the object when i will save in the bucket: ")

            os.system = input(
                f"aws s3api put-object --bucket {bucket} --key {name_dir} --body \"{file_object}\"")

        elif x == "b":
            return

        else:
            print("Invalid request")
        input("Press any key to continue")
