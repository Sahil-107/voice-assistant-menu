import os

webserverval = '''
    Press 1 to install HTTPD
    Press 2 to start Webserver
    Press 3 to restart Webserver
    Press 4 to stop Webserver
    Press b to go back to main menu
    enter your choice: '''


def webServer(sshIp=""):
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("tput clear")
        print("Webserver actions".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        x = input(webserverval)
        os.system("tput clear")

        if x == "1":
            os.system(f"{sshIp} dnf install httpd")
        elif x == "2":
            os.system(f"{sshIp} systemctl enable --now httpd")
            print("Web server started")
        elif x == "3":
            os.system(f"{sshIp} systemctl restart httpd")
            print("Web server restarted")
        elif x == "4":
            os.system(f"{sshIp} systemctl stop httpd")
            print("Web server stopped")
        elif x == "b":
            return
        input("\npress any key to continue")
