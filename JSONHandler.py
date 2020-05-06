from os import path
import json

class JSONHandler:

    def __init__(self):
        self.index_path = "config/indexes.json"
        self.libpath = "config/root.json"

    def ifIndexedLibraries(self):
        return path.exists(self.index_path)

    def getLibs(self):
        with open(self.libpath) as jfile:
            data = json.load(jfile)
            return data['libraries']
    def getIndexNames(self):
        with open(self.index_path) as jfile:
            data = json.load(jfile)
            return data['list']

    def getNthIndex(self,n):
        with open(self.index_path) as jfile:
            data = json.load(jfile)
            return data['libs'][n-1]

    def writeIndexes(self,obj):
        with open(self.index_path,'w') as outfile:
            json.dump(obj,outfile,indent=4)
    
