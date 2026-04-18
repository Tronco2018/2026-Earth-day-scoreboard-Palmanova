FILE = "conf.yml"

class Config_interface:
    def __init__(self):
        self.filename = FILE
    
    def get_file(self):
        return open(self.filename, "r")

    def get_property(self, property: str):
        keys = []
        for l in self.get_file():
            l = l.strip()
            segments = l.split(":")
        
            if len(segments) < 2:
                continue
            segments[1] = segments[1].strip()
            key = segments[0].upper()
            if property.upper() == key:
                return segments[1]

            