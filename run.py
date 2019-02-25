import configparser
from socket import socket
from ircSocket import IRCSocket 


#importing irc settings 
config = configparser.ConfigParser()
config.read("config.ini")

HOST = config.get('irc','HOST')
PORT = config.getint('irc','PORT')
PASS = config.get('irc','PASS')
NICK = config.get('irc','NICK')
CHAN = config.get('irc','CHAN')

irc = IRCSocket(HOST,PORT,PASS,NICK)
irc.setup(socket())
irc.joinChannel(CHAN)

theBuffer = ""
running = True
while running:
    running = irc.parseBuffer(theBuffer)

print("success?")