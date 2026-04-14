from Logger import Logger
import json
import os

class Command_handler:
    def __init_(self):  
        self.prompt = ""

    def check_file(self):
        if not os.path.exists("scores.json"):
            with open("scores.json", "w") as file:
                file.write("[]")

    def handle(self, cmd, prompt):
        cmds = cmd.split(" ")
        self.prompt = prompt
        if cmds[0] == "h" or cmds[0] == "help":
            self.help()
        if cmds[0] == "n":
            self.new_team()
        if cmds[0] == "s":
            self.score_modifier()
        if cmds[0] == "i":
            self.show_score()
        if cmds[0] == "l":
            self.list_teams()

    # Commands
    def help(self):
        print("Commands:\n- n: New team\n- s: Score modifier (+/- the score of a team)\n- i: See the score of a team\n- l: lists the teams\n- h: seek help\n- exit: exit the program")
    
    def new_team(self):
        self.check_file()

        file = open("scores.json", "r")
        if file:
            data = ""
            with file as f:
                data = json.load(f)
            nome = ""
            while nome == "":
                nome = self.prompt.prompt("(name)>")
                if any(x["name"] == nome for x in data):
                    Logger.error("Squadra gia' esistente!")
                    nome = ""           

            data.append({"name":nome, "score":0})
            file.close()
            with open("scores.json", "w") as f:
                json.dump(data, f, indent=4)
        
        else:
            nome = ""
            while nome == "":
                nome = self.prompt.prompt("(name)>")

            with open("scores.json", "w") as f:
                json.dump({nome, 0}, f, indent=4)
    
    def score_modifier(self):
        self.check_file()
        with open("scores.json", "r") as f:
            data = json.load(f)
        
        found = False

        nome = ""
        score = 0

        nome = self.prompt.prompt("(name)>")
        score = self.prompt.prompt("(score +/-)>")

        for element in data:
            if element["name"] == nome:
                element["score"] += int(score)
                found = True
        
        if not found:
            Logger.error("Team not found")
        else:
            with open("scores.json", "w") as f:
                json.dump(data, f, indent=4)

    def show_score(self):
        self.check_file()
        with open("scores.json", "r") as f:
            data = json.load(f)

        found = False

        nome = ""

        nome = self.prompt.prompt("(name)>")

        for element in data:
            if element["name"] == nome:
                print(f"Score:{element["score"]}")
                found = True
        
        if not found:
            Logger.warn("Team not found")
    def list_teams(self):
        self.check_file()
        with open("scores.json", "r") as f:
            data = json.load(f)
        i = 0
        for element in data:
            if i < 2:
                print(f"{element["name"]}({element["score"]}) ", end="")
                i += 1
            else:
                print(f"{element["name"]}({element["score"]}) ")
                i = 0

        print("")