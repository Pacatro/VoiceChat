"""
    The bot recive a command as input and try to do the action dictated by the command.
    
    For example: 'Open YouTube'
    
    This command is formed by a verb (Open) and a subject (YouTube).
    The Bot will do the instruction that says the verb.
"""

import webbrowser as wb
import os
import subprocess

class Bot:
    _VERB: str
    _SUBJECT: str
    
    def __init__(self, order: str) -> bool:
        div_order = order.split()
        self._VERB = div_order[0].lower()
        self._SUBJECT = div_order[1].lower().replace('.', '')
        
        if self._VERB == "" or self._SUBJECT == "":
            print("Can't get a verb or subject")
            print("Verb:", self._VERB + "\n" + "Subject:", self._SUBJECT)
            
    def open_orders(self):
        if(self._VERB == "open"):
            subprocess.call(self._SUBJECT)