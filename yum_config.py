from os import system
import subprocess

initialPrmpt = """Please ensure that optical drive is attached before proceeding......
If yes....the press enter to continue....."""


def yum():
    input(initialPrmpt)

    username = subprocess.check_output("whoami")
    username = str(username)[2:-3]

    datafile = f"""[dvd11]\nbaseurl = file:///run/media/{username}/RHEL-8-0-0-BaseOS-x86_64/AppStream\ngpgcheck=0\n\n[dvd12]\nbaseurl = file:///run/media/{username}/RHEL-8-0-0-BaseOS-x86_64/BaseOS\ngpgcheck=0"""

    yumfile = open("/etc/yum.repos.d/hhhgh.repo", "w")
    if yumfile:
        print("File created succesfully ..... now writing in file.....\n")
        yumfile.writelines(datafile)
        print("File written successfully..... now closing file")
        yumfile.close()

    print("Installing additonal Repos for redhat.......\n")
    system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")

    system("dnf install --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm")

    system("yum repolist")

    print("\nYum has been successfully configured on your system.......")
    speech.speak("Yum has been successfully configured on your system")
