from socket import socket

class IRCSocket:
    def __init__(self,host,port,auth,name):
        self.host = host
        self.port = port
        self.auth = auth
        self.name = name

    def setup(self,skt):
        self.skt = skt
        skt.connect((self.host,self.port))
        skt.send(("".join(("PASS ", self.auth, "\r\n"))).encode('utf-8'))
        skt.send(("".join(("NICK ", self.name, "\r\n"))).encode('utf-8'))
        print("setup complete")
    
    def joinChannel(self, channel):
        self.skt.send(("".join(("JOIN ", channel, "\r\n"))).encode('utf-8'))
        self.sendMessage("I have arrived Kappa", channel)
        self.initBuffer()
        print("Joined {0}".format(channel))

    def sendMessage(self, message, channel):
        self.skt.send(("".join(("PRIVMSG ", channel, " :", message, "\r\n"))).encode('utf-8'))
        print("Message sent")
    
    def initBuffer(self):
        readBuffer = ""
        hasLines = True
        while hasLines:    
            readBuffer += self.skt.recv(1024).decode('utf-8')
            temp_buffer = readBuffer.split("\n")
            readBuffer = temp_buffer.pop()

            for line in temp_buffer:
                print(line)
                if "End of /NAMES list" in line:
                    hasLines = False
                    print("joining finished")
    
    def parseBuffer(self, readBuffer):
        readBuffer += self.skt.recv(1024).decode('utf-8')
        temp_buffer = readBuffer.split("\n")
        readBuffer = temp_buffer.pop()
        for line in temp_buffer:
            print(line)
            if "!shutdown" in line: 
                return False
        return True

