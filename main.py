# Requiem bot for IRC written in Python 3

import sys
import socket
import string

import topics
import random
import time
import threading

SERVER = "irc.rizon.net"
CHANNEL = "#" + sys.argv[1]
NICK = sys.argv[2]
OWNER = "dude1"
OWNERVHOST = "singing.a.sad.song"
# Your vhost is unique so this way only you (identified) may be able to part and join channels.
INTRO = "Every hour it gives you a literary topic to think about your meaningless life."
channelsJoined = [CHANNEL, ]

def join_channel(channel):
	ircsock.send(bytes("JOIN "+ channel +"\n", "UTF-8"))
	ircsock.send(bytes("PRIVMSG "+ channel +" :"+ INTRO +"\n", "UTF-8"))

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((SERVER, 6667))
ircsock.send(bytes("USER "+ NICK +" "+ NICK +" "+ NICK +" :connected\n", "UTF-8"))
ircsock.send(bytes("NICK "+ NICK +"\n", "UTF-8"))
# ircsock.send(bytes("NICKSERV :IDENTIFY %s\r\n" % password, "UTF-8"))

time.sleep(2)
join_channel(CHANNEL)


# Bot functions
def send_to_channel_normal(message, channel):
	ircsock.send(bytes("PRIVMSG "+ channel +" :"+ message +"\n", "UTF-8"))

def send_to_channel_bold(message, channel):
	ircsock.send(bytes("PRIVMSG "+ channel +" :""\u0002"+message +"\n", "UTF-8"))

def send_to_channel_cursive(message, channel):
	ircsock.send(bytes("PRIVMSG "+ channel +" :""\u001D"+message +"\n", "UTF-8"))

def part(channel):
	ircsock.send(bytes("PART "+ channel +"\n", "UTF-8"))


def get_time(delay):
	timeNow = [time.strftime("%H"), time.strftime("%M"), time.strftime("%S")]
	time.sleep(delay)
	return(timeNow)


def timer():
	while True:
		currentTime = get_time(30)
	
		if(currentTime[1] == "00"):
			topicName = random.choice(list(topics.topics.keys()))
			topicTran = topics.topics[topicName][0]
			topicDesc = topics.topics[topicName][1]

			for channel in channelsJoined:
				send_to_channel_bold(topicName, channel)
				send_to_channel_cursive(topicTran, channel)
				send_to_channel_normal(topicDesc, channel)

			time.sleep(60)

def ircBuffer():
	readbuffer = ""

	while True:

		readbuffer = readbuffer+ircsock.recv(1024).decode("UTF-8")
		temp = str.split(readbuffer, "\n")
		readbuffer=temp.pop( )

		try:
			for line in temp:
				line = str.rstrip(line)
				line = str.split(line)
			print(line)

			channel = ""
			
			try:
				for char in line[2]:
					if(char != ":"):
						channel += char	
			except:
				pass

			if(line[0] == "PING"):
				ircsock.send(bytes("PONG %s\r\n" % line[1], "UTF-8"))

			if(line[3] == ":!!topic"):
				topicName = random.choice(list(topics.topics.keys()))
				topicTran = topics.topics[topicName][0]
				topicDesc = topics.topics[topicName][1]

				send_to_channel_bold(topicName, channel)
				send_to_channel_cursive(topicTran, channel)
				send_to_channel_normal(topicDesc, channel)

			if(line[3] in (":!!" + word for word in topics.first_word)):
# checks if the message starts with !! if it does checks if the next words is in a list of first words, is a valid phrase in topics
				size = len(line)
# some topics are longer so this makes sure you get all the words
				index = 3
# starts at the fourth element, first element (0) is the username, second (1) is PRIVMSG, third (2) is the channel and fourth is the first word (:!!firstword)
				phrase = ""
				while (index < size):
					phrase += line[index] + " "
					index += 1
				phrase = phrase.replace(":!!","")
				phrase = phrase.capitalize()
				phrase = phrase.rstrip()

				sender = ""
				for char in line[0]:
					if(char == "!"):
						break
					if(char != ":"):
						sender += char
				if(sender != NICK):				
					topicName = phrase
					topicTran = topics.topics[topicName][0]
					topicDesc = topics.topics[topicName][1]

					send_to_channel_bold(topicName, channel)
					send_to_channel_cursive(topicTran, channel)
					send_to_channel_normal(topicDesc, channel)

			if(line[3] == ":!!help"):
				message = "Every hour it gives a random phrase so you think about your meaningless life, do !!topic to get one right this moment. Also you can do !!name of topic to get an explanation on that one (ej: !!carpe diem)."
				send_to_channel_normal(message, channel)

			if(line[3] == ":!!quit") and (line[4] == NICK):
				sender = line[0].split("@")[1]
				if(sender == OWNERVHOST):
					part(channel)

			if(line[3] == ":!!join") and (line[4] == NICK):
				sender = line[0].split("@")[1]
				if(sender == OWNERVHOST):
					channelToJoin = ""
					for char in line[4]:
						channelToJoin += char
					join_channel(channelToJoin)
					channelsJoined.append(channelToJoin)
		except:
			continue

t1 = threading.Thread(target = timer)
t2 = threading.Thread(target = ircBuffer)

t1.start()
t2.start()
