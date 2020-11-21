import os
import speech
import recog

partition="""
List Partitions
Create Partition
Delete Partiton
Mount Partition
Format the Partitiion
""" 

def static_part():
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()
        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Partitions".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        speech.speak("here are the services provided")
        print(partition)
        speech.speak("What can i do for you?")
        opt = recog.voice_rec()
        opt = opt.lower()

        if "list" or "show" in opt:
            os.system("fdisk -l")

        elif "create" or "make" or "new" in opt:
            speech.speak("enter the device name")
            device = input("Enter the Device name: ")

            speech.speak("primary or extended")
            p_type = input("Which type of partition you want to create? [p(Primary)/e(Extended)]: ").lower()

            speech.speak("enter partition number")
            number=input("Enter the partition number (leave empty for default): ")

            speech.speak("enter first sector")
            start=input("Enter the First sector (leave empty for default): ")

            speech.speak("input last sector")
            end=input("Enter the Last sector (leave empty for default): ")
            os.system(f"printf 'n\n{p_type}\n{number}\n{start}\n{end}\nw\n' | fdisk {device}")

        elif "delete" or "remove" in opt:
            speech.speak("enter the device name")
            device = input("Enter the Device name: ")
            os.system(f"printf 'd\nw\n' | fdisk {device}")

        elif "mount" or "connect" in opt:
            speech.speak("enter the device name")
            device = input("Enter the Device name: ")

            speech.speak("enter the path of directory")
            path=input("Enter the Directory path: ")
            os.system(f"mount {device} {path}")
            print(f"{device} mounted to {path} directory.")
                
        elif "format" in opt:
            speech.speak("enter the device name")
            device = input("Enter the Device name: ")
            os.system(f"mkfs.ext4 {device}")

        elif "exit" or "quit" or "back" in opt:
            return

        else:
            print("Invalid request")
            speech.speak("invalid request")
        os.system("tput clear")