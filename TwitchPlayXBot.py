import socket
import pyautogui
import threading

SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
BOT = "xxxxxxxxxx" #nombre del bot
CHANNEL = "XxXxXoXxXxX" #Canal de twitch, no son necesarias mayúsculas
OWNER = "XxXxXxXwXxXxXxX" #acá me dormí, pero el señor al que le copié el codigo pone lo mismo que el canal
message = ""
irc = socket.socket()
irc.connect((SERVER, PORT))
irc.send(("PASS " + PASS + "\n" +
          "NICK " + BOT + "\n" +
          "JOIN #" + CHANNEL + "\n").encode())

def gamecontrol():
    global message

    while True:                 #Acá abajo se van poniendo los controles digamos
        if "1" in message.lower():
            pyautogui.keyDown('1')
            message = ""
            pyautogui.keyUp('1')

        elif "2" in message.lower():
            pyautogui.keyDown('2')
            message = ""
            pyautogui.keyUp ('2')

        elif "3" in message.lower():
            pyautogui.keyDown('3')
            message = ""
            pyautogui.keyUp ('3')

        elif "4" in message.lower():
            pyautogui.keyDown('4')
            message = ""
            pyautogui.keyUp ('4')

        elif "5" in message.lower():
             pyautogui.keyDown('5')
             message = ""
             pyautogui.keyUp ('5')

        elif "6" in message.lower():
             pyautogui.keyDown('6')
             message = ""
             pyautogui.keyUp ('6')

        elif "7" in message.lower():
             pyautogui.keyDown('7')
             message = ""
             pyautogui.keyUp ('7')

        elif "8" in message.lower():
             pyautogui.keyDown('8')
             message = ""
             pyautogui.keyUp('8')

        elif "9" in message.lower():
             pyautogui.keyDown('9')
             message = ""
             pyautogui.keyUp('9')

        elif "0" in message.lower():
             pyautogui.keyDown('0')
             message = ""
             pyautogui.keyUp('0')

        elif "q" in message.lower():
             pyautogui.keyDown('1')
             pyautogui.keyDown('2')
             message = ""
             pyautogui.keyUp('1')
             pyautogui.keyUp('2')

        elif "w" in message.lower():
             pyautogui.keyDown('2')
             pyautogui.keyDown('3')
             message = ""
             pyautogui.keyUp('3')
             pyautogui.keyUp('4')

        elif "e" in message.lower():
            pyautogui.keyDown('4')
            pyautogui.keyDown('5')
            message = ""
            pyautogui.keyUp('5')
            pyautogui.keyUp('6')

        elif "r" in message.lower():
            pyautogui.keyDown('6')
            pyautogui.keyDown('7')
            message = ""
            pyautogui.keyUp('7')
            pyautogui.keyUp('8')

        elif "t" in message.lower():
            pyautogui.keyDown('8')
            pyautogui.keyDown('9')
            message = ""
            pyautogui.keyUp('8')
            pyautogui.keyUp('9')

        elif "y" in message.lower():
            pyautogui.keyDown('9')
            pyautogui.keyDown('0')
            message = ""
            pyautogui.keyUp('9')
            pyautogui.keyUp('0')

        else:
             pass



def twitch():
    def joinchat():
        Loading = True
        while Loading:
            readbuffer_join = irc.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            for line in readbuffer_join.split("\n")[0:-1]:
                print(line)
                Loading = loadingComplete(line)

    def loadingComplete(line):
        if ("End of /NAMES list" in line):
            print("bot has joined " + CHANNEL + "'s Channel!")
            sendMessage(irc, "chat room joined")
            return False
        else:
            return True

    def sendMessage(irc, message):
        messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
        irc.send((messageTemp + "\n").encode())

    def getUser(line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    def getMessage(line):
        global message
        try:
            message = (line.split(":", 2))[2]
        except:
            message = ""
        return message

    def Console(line):
        if "PRIVMSG" in line:
            return False
        else:
            return True

    joinchat()

    while True:
        try:
            readbuffer = irc.recv(1024).decode()
        except:
            readbuffer = ""
        for line in readbuffer.split("\r\n"):
            if line == "":
                continue
            elif "PING" in line and Console(line):
                msgg = "PONG tmi.twitch.tv\r\n".encode()
                irc.send(msgg)
                print(msgg)
                continue
            else:
                print(line)
                user = getUser(line)
                message = getMessage(line)
                print(user + " : " + message)
if __name__=='__main__':
    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gamecontrol)
    t2.start()
