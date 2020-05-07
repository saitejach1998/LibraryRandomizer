from prettytable import PrettyTable
from random import seed
from random import randint
import subprocess, os, platform
from pyfiglet import Figlet
import re

def make_menu(vlist):
    table = PrettyTable(['Index','Item'])
    indexes = [x for x in range(1 ,len(vlist)+1)]
    for x,y in zip(indexes,vlist):
        table.add_row(['{}'.format(str(x)),'{}'.format(y)])
    print(table)

def randomize_video(libobj):
    n = libobj['size']
    vlist = libobj['data']

    epno = randint(0,n-1)
    return vlist[epno]
def get_ep_se_str(path):

    regex =  re.match(r'.*[s|S](\d+)[e|E](\d+)', path)
    try:
         res_str = ",Season {} Episode {}".format(str(int(regex.groups()[0])),str(int(regex.groups()[1])))
    except:
         res_str = ''
    return res_str



def play_video(path,obj):



    name = obj['name']

    final_str = name + " " + get_ep_se_str(path)

    print('Playing {}...'.format(final_str))

    if platform.system() == 'Darwin':
        subprocess.call(('open', path))
    elif platform.system() == 'Windows':
        os.startfile(path)
    else:
        subprocess.call(('xdg-open', path))

def draw_figlet():
    f = Figlet()
    print(f.renderText("Randomizer"))
    print('\n')
