import os
import speech
import recog

webserverval = '''
    Install HTTPD
    Start Webserver
    Restart Webserver
    Stop Webserver'''


def webServer(sshIp=""):
    while True:
        os.system("tput clear")
        size = os.get_terminal_size()

        os.system("tput setaf 6; tput setab 0")
        os.system("tput clear")
        print("Webserver actions".center(size.columns))
        os.system("tput setaf 7; tput setab 0")

        speech.speak("here are the services provided")
        print(webserverval)
        speech.speak("What can i do for you?")
        opt = recog.voice_rec()
        opt = opt.lower()

        if "install" or "download" in opt:
            speech.speak("installing web server")
            os.system(f"{sshIp} dnf install httpd")

        elif "start" or "launch" in opt:
            speech.speak("starting web server")
            os.system(f"{sshIp} systemctl enable --now httpd")
            print("Web server started")

        elif "restart" or "again" in opt:
            speech.speak("restarting web server")
            os.system(f"{sshIp} systemctl restart httpd")
            print("Web server restarted")

        elif "stop" or "pause" in opt and "server" or "web" in opt:
            speech.speak("stopping web server")
            os.system(f"{sshIp} systemctl stop httpd")
            print("Web server stopped")

        elif "exit" or "quit" or "back" in opt:
            return

        else:
            print("Invalid request")
            speech.speak("invalid request")
        os.system("tput clear")