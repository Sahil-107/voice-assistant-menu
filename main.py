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
        print('true')
        return True
    print("false")
    return False

do = ["configure","run","start","open","launch","manage","configuration","eexcute"]
donot = ["don't","do not","no"]

if __name__ == "__main__":
    text = '''
    Docker Management
    Amazon Web Services
    Hadoop Configuration
    Webserver Configuration
    Yum Configuration
    Manage Logical Volumes
    Manage static partitions'''

    # sshIp = ""
    # print('Do you want to do ssh? Say (yes/no)')
    # speech.speak("Do you want to do ssh?")
    # sleep(2)
    # isSsh = recog.voice_rec()
    # isSsh.lower()

    while True:
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Welcome to the menu".center(size.columns))
        os.system("tput setaf 7; tput setab 0")
        speech.speak("Welcome to the menu!")

        # if "yes" in isSsh:
        #     sshIp = input('Enter the ssh IP or domain: ')
        #     speech.speak("Please enter IP address")
        #     sshIp = f"ssh {sshIp}"

        speech.speak("Here are the services provided")
        print(text)
        sleep(2)
        speech.speak("What can i do for you?")
        toolOpt = recog.voice_rec()
        toolOpt.lower()

        if "quit" and "exit" in toolOpt:
            print("Exiting...!")
            speech.speak("Exiting")
            sleep(1)
            break

        elif check(toolOpt) and "docker" or "container" in toolOpt:
            speech.speak("opening docker management")
            container.dockerMenu()

        elif check(toolOpt) and "amazon" or "hosting" in toolOpt:
            speech.speak("opening amazon web hosting service")
            awsmenu.aws()

        elif check(toolOpt) and "hadoop" or "cluster" in toolOpt:
            speech.speak("opening hadoop management")
            hadoop.hadoop()

        elif check(toolOpt) and "webserver" or "web server" in toolOpt:
            speech.speak("opening web server configuration")
            webserver.webServer()

        elif check(toolOpt) and "yum" or "repo" or "repositry" in toolOpt:
            speech.speak("opening yum configuration")
            yum_config.yum()

        elif check(toolOpt) and "partition" or "partitions" or "volume" or "volumes" or "logical" in toolOpt:
            speech.speak("opening logical volume management")
            lvm.logical_vol()

        elif check(toolOpt) and "static" in toolOpt:
            speech.speak("opening static partitions")
            partition_2.static_part()

        else:
            continue

    os.system("tput clear")