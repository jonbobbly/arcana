import json

class GameMenuItem():
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

class GameMenu():
    def __init__(self, menufile):
        self.data = json.load( open('data/ui/'+menufile) )

    def list_titles(self, pad):
        pad.erase()
        row = 0
        for item in self.data["items"]:
            pad.addstr(row, 0, item["name"])
            row += 1

    def menu_title(self):
        return self.data["title"]

    def num_items(self):
        return len(self.data["items"])

    def get_desc(self, num):
        return self.data["items"][num]["desc"]

    def get_action(self, num):
        return self.data["items"][num]["action"]

    def get_item(self, num):
        return self.data["items"][num]

