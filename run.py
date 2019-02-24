import configparser

#importing irc settings 
config = configparser.ConfigParser()
config.read("config.ini")
HOST = config.get('irc','HOST')
PORT = config.getint('irc','PORT')
PASS = config.get('irc','PASS')
NICK = config.get('irc','NICK')
CHAN = config.get('irc','CHAN')

