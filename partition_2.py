import os

partition="""
Enter 1 to List Partitions
Enter 2 to Create Partition
Enter 3 to Delete Partiton
Enter 4 to Mount the Partition
Enter 5 to Format the Partitiion
Enter b to go back to menu
""" 

def static_part():
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()
        os.system("tput setaf 6; tput setab 0")
        os.system("clear")
        print("Partitions".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        x=input(partition)

        if x == '1':
            os.system("fdisk -l")

        elif x=='2':
            device = input("Enter the Device name: ")
            p_type = input("Which typr of partition you want to create? [p(Primary)/e(Extended)]: ").lower()
            number=input("Enter the partition number (leave empty for default): ")
            start=input("Enter the First sector (leave empty for default): ")
            end=input("Enter the Last sector (leave empty for default): ")
            os.system(f"printf 'n\n{p_type}\n{number}\n{start}\n{end}\nw\n' | fdisk {device}")

        elif x=='3':
            device = input("Enter the Device name: ")
            os.system(f"printf 'd\nw\n' | fdisk {device}")

        elif x=='4':
            device = input("Enter the Device name: ")
            path=input("Enter the Directory path: ")
            os.system(f"mount {device} {path}")
            print(f"{device} mounted to {path} directory.")
                
        elif x=='5':
            device = input("Enter the Device name: ")
            os.system(f"mkfs.ext4 {device}")

        elif x=='b':
            exit()
        else:
            print("Invalid request")
        input("Press any key to continue")