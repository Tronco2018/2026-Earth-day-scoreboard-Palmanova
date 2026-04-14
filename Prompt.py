from prompt_toolkit import PromptSession
import threading
import time
from Logger import Logger
from Command_handler import Command_handler

session = PromptSession()
cmd_hdlr = Command_handler()

class Prompt:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            cmd = session.prompt(">")
            if cmd == "exit":
                self.stop()
                break
            cmd_hdlr.handle(cmd, session)
            

    def stop(self):
        self.running = False
