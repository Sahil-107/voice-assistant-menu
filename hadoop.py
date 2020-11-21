import os
import speech
import recog

mainPrmt = """
    Download and install Hadoop
    Download and install Jdk
    Configure Data-node
    Configure Name-node
    Configure Client-node"""

def check(opt):
    if any(ele in opt for ele in do) and not any(ele in opt for ele in donot):
        return True
    return False

do = ["configure","run","start","open","launch","manage","configuration","excute"]
donot = ["don't","do not","no"]

def hadoop():
    while True:

        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("tput clear")
        print("Hadoop configuration and operations".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        speech.speak("here are the services provided")
        print(mainPrmt)
        speech.speak("What can i do for you?")
        opt = recog.voice_rec()
        opt = opt.lower()

        os.system("tput clear")
        if "download" or "install" in opt and "hadoop" in opt:
            speech.speak("downloading and installing hadoop")
            os.system(
                "wget https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm")
            os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
            speech.speak("hadoop installed")
            os.system("tput clear")

        elif "download" or "install" in opt and "jdk" or "java" in opt:
            speech.speak("downloading and installing java JDK")
            os.system(
                "wget 35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm")
            os.system("rpm -i jdk-8u171-linux-x64.rpm")
            speech.speak("jdk installed")
            os.system("tput clear")

        elif check(opt) and "data" in opt:
            while True:
                speech.speak("here are the services provided")
                print("""
                Setup Data-node
                Start Data-node
                Stop Data-node
                Format Data-node
                Go back""")

                speech.speak("What can i do for you?")
                d = recog.voice_rec()
                d = d.lower()

                if "setup" or "configure" in d and "data" or "node" in d:
                    speech.speak("please enter ip address of name node")
                    ip = input("Enter the IP address of Name-node")
                    speech.speak("please enter port number")
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
                    speech.speak("Hadoop Data node setup successful")

                elif "start" in d and "data" or "node" in d:
                    speech.speak("Starting data node")
                    os.system("hadoop-daemon.sh start datanode")
                    print("Data-node started..")
                    speech.speak("data node started")

                elif "data" or "node" in d and "stop" in d:
                    speech.speak("stopping data node")
                    os.system("hadoop-daemon.sh stop datanode")
                    print("Data-node stopped..")
                    speech.speak("data node stopped")

                elif "data" or "node" in d and "format" in d:
                    os.system("hadoop datanode -format")
                    print("Data-node formatted..")
                    speech.speak("data node formatted")

                elif "back" or "exit" or "stop" in d:
                    os.system("tput clear")
                    return

                else:
                    speech.speak("invalid command")
                    os.system("tput clear")
                    continue

                input("Press Enter to continue")

        elif check(opt) and "name" in opt:
            while True:
                speech.speak("here are the services provided")
                print("""
                Setup Name-node
                Start Name-node
                Stop Name-node
                Format Name-node
                Check report
                Go back""")

                speech.speak("What can i do for you?")
                n = recog.voice_rec()
                n = n.lower()

                if "setup" or "configure" in n and "name" or "node" in n:
                    speech.speak("enter IP address")
                    ip = input(
                        "Enter the IP (By default 0.0.0.0 will be added): ")
                    if len(ip) > 0:
                        pass
                    else:
                        ip = "0.0.0.0"
                    speech.speak("enter post number")
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
                    speech.speak("hadoop name node setup successful")

                elif "start" or "run" in n and "name" or "node" in n:
                    speech.speak("Starting name node")
                    os.system("hadoop-daemon.sh start namenode")
                    print("Name-node started")
                    speech.speak("name node started")

                elif "stop" or "pause" in n and "name" or "node" in n:
                    speech.speak("stopping name node")
                    os.system("hadoop-daemon.sh stop namenode")
                    print("Name-node stopped")
                    speech.speak("name node stopped")

                elif "format" or "clear" in n and "name" or "node" in n:
                    speech.speak("formatting name node")
                    os.system("hadoop namenode -format")
                    speech.speak("name node formatted")

                elif "admin" or "report" or "detail" in n:
                    speech.speak("here are the details")
                    os.system("hadoop dfsadmin -report")

                elif "exit" or "stop" or "back" in n:
                    os.system("tput clear")
                    return

                else:
                    speech.speak("invalid command")
                    os.system("tput clear")
                    continue
                
                input("Press Enter to continue")

        elif check(opt) and "client" in opt:
            while True:
                speech.speak("here are the services provided")
                print("""
                Setup Client-node
                Change block-size and Replication-factor
                See files in hadoop cluster
                Upload file in hadoop cluster
                Remove the file from hadoop
                Go back""")

                speech.speak("What can i do for you?")
                c = recog.voice_rec()
                c = c.lower()

                if "setup" or "start" in c and "client" in c:
                    ip = input("Enter the IP address of Name-node: ")
                    speech.speak("Enter ip address")
                    port = int(input("Enter the port number: "))
                    speech.speak("Enter port number")

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

                elif "replication" or "block" or "backup" in c:
                    speech.speak("Enter replication factor")
                    replication_factor = input("Enter the Replication-factor: ")
                    speech.speak("Enter block size in bytes")
                    block_size = input("Enter the block-size (in bytes): ")

                    datafile6 = f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{replication_factor}</value>\n</property>\n<property>\n<name>dfs.block.size</name>\n<value>{block_size}</value>\n</property>\n</configuration>\n"""

                    hdfsfile = open("/etc/hadoop/hdfs-site.xml", "w")
                    if hdfsfile:
                        print(
                            "hdfs-site.xml created succesfully ..... now writing in file.....\n")
                        hdfsfile.writelines(datafile6)
                        print(
                            "hdfs-site.xml written successfully..... now closing file")
                        hdfsfile.close()

                    speech.speak("replication factor and block size changed")

                elif "see" and "files" in c:
                    speech.speak("files in hadoop cluster are")
                    os.system("hadoop fs -ls /")

                elif "upload" or "put" in c:
                    speech.speak("Enter name of the file")
                    name = input("Enter the name of the file: ")
                    os.system(f"hadoop.fs -put {name} /")

                elif "remove" or "delete" in c:
                    speech.speak("Enter the name of the file you want to remove")
                    name = input(
                        "Enter the name of the file you want to remove: ")
                    os.system(f"hadoop.fs -rm /{name}")

                elif "exit" or "stop" or "back" in c:
                    os.system("tput clear")
                    return

                else:
                    speech.speak("invalid command")
                    os.system("tput clear")
                    continue

                input("Press Enter to continue")

        elif "exit" or "quit" or "back" in opt:
            return

        else:
            print("Invalid request")
            speech.speak("invalid request")
        os.system("tput clear")
