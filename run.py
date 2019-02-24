import configparser
import socket

#importing irc settings 
config = configparser.ConfigParser()
config.read("config.ini")

HOST = config.get('irc','HOST')
PORT = config.getint('irc','PORT')
PASS = config.get('irc','PASS')
NICK = config.get('irc','NICK')
CHAN = config.get('irc','CHAN')

def ircMessage(message):
    irc.send(("".join(("PRIVMSG ", CHAN, " :", message, "\r\n"))).encode('utf-8'))

irc = socket.socket()
irc.connect((HOST,PORT))
irc.send(("".join(("PASS ", PASS, "\r\n"))).encode('utf-8'))
irc.send(("".join(("NICK ", NICK, "\r\n"))).encode('utf-8'))
irc.send(("".join(("JOIN ", CHAN, "\r\n"))).encode('utf-8'))

ircMessage("Bot has connected.")