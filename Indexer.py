import json
import glob
import os
from JSONHandler import JSONHandler
class Indexer:

    def __init__ (self,paths):
        self.paths = paths


    def index(self):
        jhandler = JSONHandler()
        alldata = {}
        alldata['libs'] = []
        alldata['list'] = []
        leafs = self.get_leafs()

        for leaf in leafs:
            leafobj = self.makeleafobj(leaf)
            alldata['libs'].append(leafobj)
            alldata['list'].append(leafobj['name'])

        jhandler.writeIndexes(alldata)
        return len(alldata['list'])


    def makeleafobj(self,leaf):
        libdata = self.indexLeaf(leaf)
        libsize = len(libdata)
        libname = leaf.split('\\')[-2]
        obj = {
        'name' : libname,
        'size': libsize,
        'data': libdata
        }
        return obj

    def get_leafs(self):
        leafs = []
        for path in self.paths:
            leafs = leafs + [f for f in glob.glob(path + "/*/")]
        return leafs


    def read_json(self,path):
        with open('path') as json_file:
            return json.load(json_file)

    def indexLeaf(self,path):
        exts = ['mkv','mp4']
        files = []
        for ext in exts:

            files = files + glob.glob(r''+os.path.join(path,'**/*.{}'.format(ext)),recursive=True)

            #print(os.path.join(path,'*.{}'.format(ext)))
        return files
