#!/usr/bin/python3
from time import sleep
import os
import subprocess
import container
import awsmenu
import hadoop
import webserver
import yum_config
import recog
import speech
import lvm
import partition_2

def check(toolOpt):
    if any(ele in toolOpt for ele in do) and not any(ele in toolOpt for ele in donot):
        return True
    return False

do = ["configure","run","start","open","launch","manage","configuration","excute"]
donot = ["don't","do not","no"]
# docker_list=["docker","container"]
# hadoop_list=["hadoop","cluster"]
# aws_list=["amazon","hosting","aws"]
# server_list=["web","server"]
# lvm_list=["lvm","logical","volume"]
# yum_list=["yum","repo","repositry"]

if __name__ == "__main__":
    text = '''
    Docker Management
    Amazon Web Services
    Hadoop Configuration
    Webserver Configuration
    Yum Configuration
    Manage Logical Volumes
    Manage static partitions'''

    sshIp = ""
    print('Do you want to do ssh? Say (yes/no)')
    speech.speak("Do you want to do ssh?")
    sleep(2)
    isSsh = recog.voice_rec()
    isSsh.lower()

    while True:
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Welcome to the menu".center(size.columns))
        os.system("tput setaf 7; tput setab 0")
        speech.speak("Welcome to the menu!")

        if "yes" in isSsh:
            sshIp = input('Enter the ssh IP or domain: ')
            speech.speak("Please enter IP address")
            sshIp = f"ssh {sshIp}"

        speech.speak("Here are the services provided")
        print(text)
        sleep(2)
        speech.speak("What can i do for you?")
        toolOpt = recog.voice_rec()
        toolOpt = toolOpt.lower()

        if "quit" and "exit" in toolOpt:
            print("Exiting...!")
            speech.speak("Exiting")
            sleep(1)
            break

        elif check(toolOpt) and "docker" in toolOpt:
            speech.speak("opening docker management")
            container.dockerMenu(isSsh)

        elif check(toolOpt) and "amazon" in toolOpt:
            speech.speak("opening amazon web hosting service")
            awsmenu.aws()

        elif check(toolOpt) and "hadoop" in toolOpt:
            speech.speak("opening hadoop management")
            hadoop.hadoop()

        elif check(toolOpt) and "server" in toolOpt:
            speech.speak("opening web server configuration")
            webserver.webServer(isSsh)

        elif check(toolOpt) and "yum" in toolOpt:
            speech.speak("opening yum configuration")
            yum_config.yum()

        elif check(toolOpt) and "locical" in toolOpt:
            speech.speak("opening logical volume management")
            lvm.logical_vol()

        elif check(toolOpt) and "static" in toolOpt:
            speech.speak("opening static partitions")
            partition_2.static_part()

        else:
            continue

    os.system("tput clear")