import os

mainPrmt = """
    Enter 1 to download and install hadoop
    Enter 2 to download and install jdk
    Enter 3 to configure Data-node
    Enter 4 to configure Name-node
    Enter 5 to configure Client-node
    Enter b to go back to main menu
    Enter your choice here: """


def hadoop():
    while True:

        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("tput clear")
        print("Hadoop configuration and operations".center(size.columns))
        os.system("tput setaf 7; tput setab 0")
        x = input(mainPrmt)
        os.system("tput clear")
        if x == "1":
            os.system(
                "wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
            os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
            input("press any key to continue")
            os.system("tput clear")

        elif x == "2":
            os.system(
                "wget 35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm")
            os.system("rpm -i jdk-8u171-linux-x64.rpm")
            input("press any key to continue")
            os.system("tput clear")

        elif x == "3":
            y = 1
            while y == 1:
                print("Enter 1 to setup Data-node")
                print("Enter 2 to start Data-node")
                print("Enter 3 to stop Data-node")
                print("Enter 4 to format Data-node")
                print("Enter b to go back to Hadoop menu")

                d = input("enter your choice here: ")

                if d == "1":
                    ip = input("Enter the IP address of Name-node")
                    port = int(input("Enter the port number"))

                    datafile1 = """<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/datanode</value>\n</property>\n</configuration>\n"""

                    datafile2 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""

                    hdfsfile = open("/etc/hadoop/hdfs-site.xml", "w")
                    os.system("mkdir /datanode")
                    if hdfsfile:
                        print(
                            "hdfs-site.xml created succesfully ..... now writing in file.....\n")
                        hdfsfile.writelines(datafile1)
                        print(
                            "hdfs-site.xml written successfully..... now closing file")
                        hdfsfile.close()

                    corefile = open("/etc/hadoop/core-site.xml", "w")
                    if corefile:
                        print(
                            "core-site.xml created succesfully ..... now writing in file.....\n")
                        corefile.writelines(datafile2)
                        print(
                            "core-site.xml written successfully..... now closing file")
                        corefile.close()

                    print("Hadoop Data-node setup successful")

                elif d == "2":
                    os.system("hadoop-daemon.sh start datanode")
                    print("Data-node started..")

                elif d == "3":
                    os.system("hadoop-daemon.sh stop datanode")
                    print("Data-node stopped..")

                elif d == "4":
                    os.system("hadoop datanode -format")
                    print("Data-node formatted..")

                elif d == "b":
                    y = 0
                if d != "b":
                    input("press any key to continue")
                    os.system("tput clear")

        elif x == "4":
            y = 1
            while y == 1:
                print("Press 1 to setup Name-node")
                print("Press 2 to start Name-node")
                print("Press 3 to stop Name-node")
                print("Press 4 to format Name-node")
                print("Press 5 to check report")
                print("Press b to go back to Hadoop menu")

                n = input("Enter your choice here: ")

                if n == "1":
                    ip = input(
                        "Enter the IP (By default 0.0.0.0 will be added): ")
                    if len(ip) > 0:
                        pass
                    else:
                        ip = "0.0.0.0"

                    port = int(input("Enter the port number: "))

                    datafile3 = """<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/namenode</value>\n</property>\n</configuration>\n"""

                    datafile4 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""

                    hdfsfile = open("/etc/hadoop/hdfs-site.xml", "w")
                    os.system("mkdir /natanode")
                    if hdfsfile:
                        print(
                            "hdfs-site.xml created succesfully ..... now writing in file.....\n")
                        hdfsfile.writelines(datafile3)
                        print(
                            "hdfs-site.xml written successfully..... now closing file")
                        hdfsfile.close()

                    corefile = open("/etc/hadoop/core-site.xml", "w")
                    if corefile:
                        print(
                            "core-site.xml created succesfully ..... now writing in file.....\n")
                        corefile.writelines(datafile4)
                        print(
                            "core-site.xml written successfully..... now closing file")
                        corefile.close()

                    print("Hadoop Name-node setup successful")

                elif n == "2":
                    os.system("hadoop-daemon.sh start namenode")
                    print("Name-node started")

                elif n == "3":
                    os.system("hadoop-daemon.sh stop namenode")
                    print("Name-node stopped")

                elif n == "4":
                    os.system("hadoop namenode -format")

                elif n == "5":
                    os.system("hadoop dfsadmin -report")

                elif n == "b":
                    y = 0
                if n != "b":
                    input("press any key to continue")
                    os.system("tput clear")

        elif x == "5":
            y = 1
            while y == 1:
                print("Enter 1 to setup Client-node")
                print("Enter 2 to change block-size and replication-factor")
                print("Enter 3 to see the files in hadoop cluster")
                print("Enter 4 upload the file in hadoop cluster")
                print("Enter 5 to remove the file from hadoop")
                print("Enter 6 to see a file in hadoop cluster")
                print("Enter b to go back to Hadoop menu")

                c = input("Enter your choice here: ")

                if c == "1":
                    ip = input("Enter the IP address of Name-node: ")
                    port = int(input("Enter the port number: "))

                    datafile5 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{ip}:{port}</value>\n</property>\n</configuration>\n"""

                    corefile = open("/etc/hadoop/core-site.xml", "w")
                    if corefile:
                        print(
                            "core-site.xml created succesfully ..... now writing in file.....\n")
                        corefile.writelines(datafile5)
                        print(
                            "core-site.xml written successfully..... now closing file")
                        corefile.close()

                    print("Hadoop Client-node setup successful")

                elif c == "2":
                    replication_factor = input(
                        "Enter the Replication-factor: ")
                    block_size = input("Enter the block-size in bytes: ")

                    datafile6 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{replication_factor}</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>{block_size}</value>\n</property>\n</configuration>\n"""

                    hdfsfile = open("/etc/hadoop/hdfs-site.xml", "w")
                    if hdfsfile:
                        print(
                            "hdfs-site.xml created succesfully ..... now writing in file.....\n")
                        hdfsfile.writelines(datafile6)
                        print(
                            "hdfs-site.xml written successfully..... now closing file")
                        hdfsfile.close()

                elif c == "3":
                    os.system("hadoop fs -ls /")

                elif c == "4":
                    name = input("Enter the name of the file: ")
                    os.system(f"hadoop.fs -put {name} /")

                elif c == "5":
                    name = input(
                        "Enter the name of the file you want to remove: ")
                    os.system(f"hadoop.fs -rm /{name}")

                elif c == "6":
                    name = input(
                        "Enter the name of the file you want to see: ")
                    os.system(f"hadoop.fs -cat /{name}")

                elif c == "b":
                    y = 0
                if c != "b":
                    input("press any key to continue")
                    os.system("tput clear")

        elif x == "b":
            return

        else:
            print("Invalid request")
        os.system("tput clear")
