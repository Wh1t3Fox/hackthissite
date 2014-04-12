#!/usr/bin/env python

import socket
import requests
import random
import threading
import logging
import json
import sys
                 

class Bot():
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CONFIG = {
            'server': 'irc.freenode.net',
            'port': 6667,
            'channel': '#securitygeekguys',
            'nick': '_MastersBot_',
            'ident': random.randrange(1,100),
            'op': ['Wh1t3Fox'],
            'voice': ['tmschmitt']
    }
    COLORS = {
            'white': '\x030',
            'black': '\x031',
            'navy': '\x032',
            'green': '\x033',
            'red': '\x034',
            'maroon': '\x035',
            'purple': '\x036',
            'olive': '\x037',
            'yellow': '\x038',
            'lime': '\x039',
            'teal': '\x0310',
            'cyan': '\x0311',
            'blue': '\x0312',
            'pink': '\x0313',
            'grey': '\x0314',
            'silver': '\x0315'
    }
    
    
    def __init__(self):        
        logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', filename='ircbot.log', level=logging.DEBUG)
        self.thread = None
        self.login(self.CONFIG)
        self.main()
    
    
    def send_data(self, msg):
        self.SERVER.send(msg)
    
    
    def login(self, config):
        self.send_data('NICK %s\r\n' % config['nick'])
        self.send_data('USER %i 8 * :%s\r\n' % (config['ident'], config['nick']))
        self.send_data('JOIN %s\r\n' % config['channel'])
    
        
    def pong(self, txt):
        self.send_data('PONG :%s' % txt)
    
        
    def op_user(self, user):
        self.send_data('MODE %s +o %s\r\n' % (self.CONFIG['channel'], user))
    
    
    def deop_user(self, user):
        self.send_data('MODE %s -o %s\r\n' % (self.CONFIG['channel'], user))
    
    
    def give_voice(self, user):
        self.send_data('MODE %s +v %s\r\n' % (self.CONFIG['channel'], user))
    
    
    def remove_voice(self, user):
        self.send_data('MODE %s -v %s\r\n' % (self.CONFIG['channel'], user))
    
    
    def is_up(self, site):
        response = requests.get('http://www.isup.me/'+site).text
        if response.find("It's just you.") != -1:
            self.send_data("PRIVMSG %s :%s[+]%s IS UP\r\n" % (self.CONFIG['channel'], self.COLORS['blue'], site))
        else:
            self.send_data("PRIVMSG %s :%s[+]%s IS DOWN\r\n" % (self.CONFIG['channel'], self.COLORS['red'], site))
        
    
    
    def get_youtube_info(self, id):
        url = 'http://gdata.youtube.com/feeds/api/videos/%s?alt=json&v=2' % id
        json_string = requests.get(url).json()
        title = json_string['entry']['title']['$t']
        author = json_string['entry']['author'][0]['name']['$t']
        description = json_string['entry']['media$group']['media$description']['$t']
        self.send_data('PRIVMSG %s :%sTitle:%s\r\n' % (self.CONFIG['channel'], self.COLORS['red'], title))
        self.send_data('PRIVMSG %s :%sAuthor:%s\r\n' % (self.CONFIG['channel'], self.COLORS['red'], author))
        self.send_data('PRIVMSG %s :%sDescription:%s\r\n' % (self.CONFIG['channel'], self.COLORS['red'], description))
        
    
    
    def auto_message(self):
        self.thread = threading.Timer(300, self.auto_message)
        self.thread.start()
        self.send_data("PRIVMSG %s :%s[+]Type !commands to view the options\r\n" % (self.CONFIG['channel'], self.COLORS['lime']))
    
    
    def commands(self):
        self.send_data("PRIVMSG %s :%s[+]All commands start with '!'\r\n" % (self.CONFIG['channel'], self.COLORS['olive']))
        self.send_data("PRIVMSG %s :%s[+]isup to view a website status\r\n" % (self.CONFIG['channel'], self.COLORS['olive']))
    
    
    def main(self):
        self.auto_message()
        while True:
            try:
                data = self.SERVER.recv(1024)
                check = data.split(':')
                user = check[1].split('!')[0]
                logging.info(data)
                        
                if check[0].find('PING') != -1:
                    self.pong(check[1])
                elif check[1].find('JOIN') != -1 and user in self.CONFIG['op']:
                    self.op_user(user)
                elif check[1].find('JOIN') != -1 and user in self.CONFIG['voice']:
                    self.give_voice(user)
                elif check[2].find('!isup') != -1:
                    self.is_up(check[2][6:-2])
                elif data.find('!commands') != -1:
                    self.commands()
                elif data.find('youtube.com/watch?v=') != -1:
                    self.get_youtube_info(data[data.find('youtube')+20:-2])
            except IndexError:
                pass
            except KeyboardInterrupt:
                self.thread.cancel()
                sys.exit()
            except Exception, e:
                logging.warning(e)
            
            
bot = Bot()