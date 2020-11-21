#!/usr/bin/python3
'''
This is the file which allows contianer operations for the menu app
'''

# imports for menu
import os
import subprocess
from time import sleep
import speech
import recog

docker = '''
    Create container
    Pull image
    List running containers
    List all containers
    List images
    Start container
    Stop container
    Delete container
    Execute mannually'''

def dockerMenu(sshIp=""):
    while True:
        out = ""

        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Docker Operations".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        speech.speak("Here are the services provided")
        print(docker)

        speech.speak("What can i do for you?")
        subOpt = recog.voice_rec()
        subOpt = subOpt.lower()

        out = ""
        os.system("tput reset")
        if "create" or "new" in subOpt and "container" or "containers" in subOpt:
            speech.speak("Creating container...")
            out = startContainer(sshIp)

        elif "pull" or "download" in subOpt and "image" or "images" in subOpt:
            speech.speak("Pulling Image...")
            out = pullImg(sshIp)

        elif "running" in subOpt and "container" in subOpt:
            speech.speak("These are the running containers...")
            out = operate("container", "ls", sshIp)

        elif "list" or "show" in subOpt and "container" or "containers" in subOpt:
            speech.speak("Listing all containers...")
            out = operate("container", "ls -a", sshIp)

        elif "list" or "show" in subOpt and "os" or "images" in subOpt:
            speech.speak("Listing all images...")
            out = operate("image", "ls", sshIp)

        elif "start" or "launch" in subOpt and "container" or "containers" in subOpt:
            speech.speak("please enter container name or id")
            cnameId = input("Enter container name or id: ")
            speech.speak("Starting container...")
            out = operate("container", "start", cnameId, sshIp)
            speech.speak("container started...")
        
        elif "stop" or "pause" in subOpt and "container" or "containers" in subOpt:
            speech.speak("please enter container name or id")
            cnameId = input("Enter container name or id")
            out = operate("container", "stop", cnameId, sshIp)
            speech.speak("container stopped...")
        
        elif "delete" or "terminate" in subOpt and "container" or "containers":
            speech.speak("please enter container name or id")
            cnameId = input("Enter container name or id: ")
            out = operate("container", "rm -f", cnameId, sshIp)
            speech.speak("container terminated...")
        
        elif "execute" or "run" in subOpt and "mannual" or "mannually" in subOpt:
            cnameId = input("Enter container name or id: ")
            cmd = input("Enter the command you want to run: ")
            cnameId = f"{cnameId} {cmd}"
            out = operate("container", "exec -it", cnameId, sshIp)

        elif "exit" or "quit" or "back" in subOpt:
            return
        
        else:
            print("Invalid request")
            speech.speak("invalid request")
        os.system("tput clear")
        
        print(out)
        # input("press any key to go back to menu")


def startContainer(sshIp=""):
    os.system("tput clear")
    speech.speak("please enter docker image name")
    imgname = input("Enter docker image name (*req): ")

    speech.speak("please enter docker image version")
    imgv = input("Enter docker image version (latest): ") or "latest"

    speech.speak("Enter give container name")
    cname = input("Enter docker container name (random): ") or None

    speech.speak("enter docker volume name")
    volname = input("Enter docker volume name (none): ") or None

    speech.speak("please enter docker volume path")
    volpath = input("Enter docker volume path (none): ") or None

    speech.speak("please enter docker net name")
    netname = input("Enter docker net name[brigde/host/null] (bridge):") or "bridge"

    volmnt = ""

    if (cname):
        cname = f"--name {cname}"
    else:
        cname = ""
    if (volname and volpath):
        volmnt = f"-v {volname}:{volpath}"

    return subprocess.getoutput(f'{sshIp} sudo podman run -dit --net {netname} {volmnt} {cname} {imgname}:{imgv}')


def pullImg(sshIp=""):
    speech.speak("Enter docker image name")
    imgname = input("Enter docker image name (*req): ")

    speech.speak("enter docker image version by default it's latest")
    imgv = input("Enter docker image version (latest): ") or "latest"

    return subprocess.getoutput(f'{sshIp} sudo podman pull {imgname}:{imgv}')


def operate(resourceType, op, cname="", sshIp=""):
    return subprocess.getoutput(f'{sshIp} sudo podman {resourceType} {op} {cname}')


# if __name__ == '__main__':
#     print("this code is not meant to be run.\nThis is a module")
