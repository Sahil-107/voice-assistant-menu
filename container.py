#!/usr/bin/python3
'''
This is the file which allows contianer operations for the menu app
'''

# imports for menu
import os
import subprocess

docker = '''
    Press 1 to create container
    Press 2 to pull image
    Press 3 to list running contianers
    Press 4 to list all containers
    Press 5 to list images
    Press 6 to start container
    Press 7 to stop container
    Press 8 to or delete contianer
    Press 9 to execute commands in the container
    Press b to back to main menu
    Enter your option: '''


def dockerMenu(sshIp=""):
    while True:
        out = ""

        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Docker Operations".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        subOpt = input(docker)
        out = ""
        os.system("tput reset")
        if subOpt == "1":
            out = startContainer(sshIp)
        elif subOpt == "2":
            out = pullImg(sshIp)
        elif subOpt == "3":
            out = operate("container", "ls", sshIp)
        elif subOpt == "4":
            out = operate("container", "ls -a", sshIp)
        elif subOpt == "5":
            out = operate("image", "ls", sshIp)
        elif subOpt == "6":
            cnameId = input("Enter container name or id: ")
            out = operate("container", "start", cnameId, sshIp)
        elif subOpt == "7":
            cnameId = input("Enter container name or id: ")
            out = operate("container", "stop", cnameId, sshIp)
        elif subOpt == "8":
            cnameId = input("Enter container name or id: ")
            out = operate("container", "rm -f", cnameId, sshIp)
        elif subOpt == "9":
            cnameId = input("Enter container name or id: ")
            cmd = input("Enter the command you want to run: ")
            cnameId = f"{cnameId} {cmd}"
            out = operate("container", "exec -it", cnameId, sshIp)
        else:
            return
        print(out)
        input("press any key to go back to menu")


def startContainer(sshIp=""):
    os.system("tput clear")
    imgname = input("enter docker image name (*req): ")
    imgv = input("enter docker image version (latest): ") or "latest"
    cname = input("enter docker container name (random): ") or None
    volname = input("enter docker volume name (none): ") or None
    volpath = input("enter docker volume path (none): ") or None
    netname = input(
        "enter docker net name[brigde/host/null] (bridge):") or "bridge"

    volmnt = ""

    if (cname):
        cname = f"--name {cname}"
    else:
        cname = ""
    if (volname and volpath):
        volmnt = f"-v {volname}:{volpath}"

    return subprocess.getoutput(f'{sshIp} sudo podman run -dit --net {netname} {volmnt} {cname} {imgname}:{imgv}')


def pullImg(sshIp=""):
    imgname = input("enter docker image name (*req): ")
    imgv = input("enter docker image version (latest): ") or "latest"

    return subprocess.getoutput(f'{sshIp} sudo podman pull {imgname}:{imgv}')


def operate(resourceType, op, cname="", sshIp=""):
    return subprocess.getoutput(f'{sshIp} sudo podman {resourceType} {op} {cname}')


if __name__ == '__main__':
    print("this code is not meant to be run.\nThis is a module")
