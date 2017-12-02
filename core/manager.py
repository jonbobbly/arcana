import os
import json

class ResourceManager():
    def __init__(self):
        self.arcana = []
        self.areas = []
        self.items = []
        self.moves = []
        self.npcs = []

        self.load_arcana()
        self.load_areas()
        self.load_items()
        self.load_moves()
        self.load_npcs()

    def load_arcana(self):
        arcana_list = os.listdir("data/arcana")
        for item in arcana_list:
            self.arcana.append( json.load(open("data/arcana/" + item)) )

    def load_areas(self):
        area_list = os.listdir("data/areas")
        for item in area_list:
            self.areas.append( json.load(open("data/areas/" + item)) )

    def load_items(self):
        item_list = os.listdir("data/items")
        for item in item_list:
            self.items.append( json.load(open("data/items/"+item)) )

    def load_moves(self):
        move_list = os.listdir("data/moves")
        for item in move_list:
            self.items.append( json.load(open("data/moves/"+item)) )

    def load_npcs(self):
        npc_list = os.listdir("data/npcs")
        for item in npc_list:
            self.items.append( json.load(open("data/npcs/"+item)) )
