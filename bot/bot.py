#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:51:22 2019

@author: Charlie & Alfie
"""
from datetime import date
import socket, string, calendar, datetime, random

# Variables specificying server details
SERVER = "localhost"
PORT = 6667
CHANNEL = "#test"


# Open the socket
IRCSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
def connect():
    IRCSocket.connect((SERVER, PORT))
    
# Hardcoded to join the channel #test
def join():
    IRCSocket.send("JOIN #test\n".encode())

# Listen to the server
def listen():
    while (True):
        buffer = IRCSocket.recv(1024)
        message = buffer.decode()

        # Check for user commands
        if ("!day" in message):
            today = date.today()
            IRCSocket.send(("PRIVMSG #test :The day today is - " + calendar.day_name[today.weekday()] + "\n").encode())
        
        elif ("!time" in message):
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            IRCSocket.send(("PRIVMSG #test :The time right now is - " + time + "\n").encode())

        # If the bot gets a private message
        elif ("PRIVMSG Bot" in message):

            # Array of random facts
            arrayFacts = [
                 "German chocolate cake is named after a guy named Sam German, not the country.",
                 "Almost as many people were killed by guillotine in Nazi Germany as in the French Revolution.",
                 "The creature that kills the most people every year isn't snakes, sharks, or even other humans — it's the mosquito.",
                 "The Sun City Poms is a cheerleading squad in Arizona that only people 55 or older can join.",
                 "There's an island in Japan you can visit that's inhabited only by friendly bunnies."             
                 ]

            # Identify the Nickname segment of the message
            start = ':'
            end = '!'

            # Get Nickname
            message = message[message.find(start)+len(start):message.rfind(end)]

            # Send the message with a random fact to the user
            IRCSocket.send(("PRIVMSG "+ message +" :Did you know - "+ arrayFacts[random.randint(0,4)] + "\n").encode())

        # Print to console
        print (buffer)
        
#Send login data (customizable)
def login():
    IRCSocket.send("USER bot networksbot server bot\n".encode())
    IRCSocket.send("NICK Bot\n".encode())
    #send_data("NICK " + nickname)
  
connect()
login()
join()
listen()