import os
import speech
import recog

lvm_part="""
Check storage devices is attached to the OS
Create Physical Volume
Display Physical Volume
Manage Volume Group
Display Volume Groups
Manage Logical Volume
Display Logical Volumes
Exit to go back to main menu
"""

def logical_vol():
    while True:
        os.system("clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Logical Volume Management".center(size.columns))
        speech.speak("Welcome to the logical volume management")
        os.system("tput setaf 7; tput setab 0")

        speech.speak("Here are the services provided")
        print(lvm_part)
        speech.speak("What can i do for you?")
        x = recog.voice_rec()
        x = x.lower()
        
        if "show" or "check" or "list" in x and "partitions" or "partition" or "storage" in x:
            speech.speak("listing partitions")
            os.system("fdisk -l")

        elif "create" or "make" or "new" in x and "physical" or "volumes" or "volumes" in x:
            while True:
                speech.speak("enter name of storage")
                pv1 = input("Enter the name of storage: ")
                os.system(f"pvcreate {pv1}")

                speech.speak("Do you want to create another Physical Volume")
                another = input("Do you want to create another PV [Y/N]: ").lower()
                if another == 'y':
                    pass
                else:
                    exit()

        elif "display" or "show" in x and "physical" in x:
            speech.speak("enter the name of the storage")
            pv = input("Enter the name of storage: ")
            os.system(f"pvdisplay {pv}")

        elif "extend" or "create" in x and "volume" in x:
            speech.speak("Here are the services provided")
            print("""
            Create new Volume Group
            Extend Volume Group
            """)
            speech.speak("What can i do for you?")

            vg = recog.voice_rec()
            vg = vg.lower()

            if "create" or 'make' in vg:
                speech.speak("give a name to volume group")
                vgn = input("Give name to the VG: ")

                speech.speak("enter name of physical volume")
                pvn = input("Enter the name of PV: ")
                os.system(f"vgcreate {vgn} {pvn}")

            elif "extend" or "increase" in vg:
                speech.speak("Enter the name of existing volume group")
                vgn = input("Enter the name of existing VG: ")

                speech.speak("Enter the name of physical volume")
                pvn = input("Enter the name of the PV: ")
                os.system(f"vgextend {vgn} {pvn}")

        elif "display" or "show" in x and "group" in x:
            speech.speak("Enter the name of existing volume group")
            vgn = input("Enter the name of VG: ")
            os.system(f"vgdisplay {vgn}")

        elif "manage" or "create" or "make" in x and "logical" in x:
            speech.speak("Here are the services provided")
            print("""
            Create new Logical Volume
            Extend Logical Volume
            Format the Logical Volume
            """)

            speech.speak("What can i do for you?")

            lv = recog.voice_rec()
            lv = lv.lower()

            if "create" or "make" in lv:
                speech.speak("enter size of logical volume")
                size = input("Enter size for your LV: ")

                speech.speak("give a name to logical volume")
                lvn = input("Give name to your LV: ")

                speech.speak("enter the name of volume group")
                vgn = input("Enter name of the VG: ")
                os.system(f"lvcreate --size {size} --name{lvn} {vgn}")

            elif "extend" or "increase" in lv:
                speech.speak("enter the name of logical")
                lvn = input("Enter the name of your LV: ")

                speech.speak("enter the name of volume group")
                vgn = input("Enter name of the VG: ")
                os.system(f"lvextend --size {size} /dev/{vgn}/{lvn}")

            elif "format" or "clear" in lv:
                speech.speak("enter the name of the volume group")
                vgn = input("Enter the name of VG:")

                speech.speak("enter the name of logical volume")
                lvn = input("Enter the name of LV:")

                os.system(f"mkfs.ext4  /dev/{vgn}/{lvn}")
                print("Partiton formatted....\n")

                speech.speak("Do you want to mount Logical volume")
                mout = input("Do you want to mount LV [Y/N]: ").upper()

                if mout == "Y":
                    speech.speak("enter the folder path")
                    path = input("Enter path of folder where you want to mount : ")
                    print("Creating directory")
                    os.system(f'mkdir {path}')
                    print("\nMounting Now ....\n")
                    mntout = os.system(f"mount /dev/{vgn}/{lvn} {path}")
                else:
                    exit()

        elif "display" or "show" in x and "logical" in x:
            speech.speak("listing logical volumes")
            os.system("lvdisplay")

        elif "exit" or "quit" or "back" in x:
            return

        else:
            print("Invalid request")
            speech.speak("invalid request")
        os.system("tput clear")