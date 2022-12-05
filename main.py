import time
from pynput import keyboard
import os
from helicopter import Helicopter as Hel
import json
from map import Map
from clouds import Clouds
s = "🛩🌩🌧🔥🌲🌊🟩🚑🔲"


TIME_SLEEP = 0.05
TREE_UPDATE = 35
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_H, MAP_W = 10, 20
hel = Hel(MAP_W, MAP_H)
n = Map(MAP_W, MAP_H)
c = Clouds(MAP_H, MAP_W)




tick = 1

MOVES = {'w': (-1, 0), 'a': (0, -1), 's': (1, 0), 'd': (0, 1)}
def process(key):
    global hel, c, n, tick
    x = key.char.lower()
    if x in MOVES.keys():
        print('ok')
        dx, dy = MOVES[x][0], MOVES[x][1]
        hel.move(dx, dy)
    elif x == 'f':
        print('kskjdkdmkjfnf')
        data = {'helicopter': hel.export_data(), 'clouds': c.export_data(), 'map': n.export_data(), 'tick': tick }
        with open('loader.json', 'w') as file:
            json.dump(data, file)
    elif x == 'g':
        with open('loader.json', 'r') as file:
            data = json.load(file)
            tick =data['tick'] or 1
            hel.import_data(data['helicopter'])
            n.import_date(data['map'])
            c.import_date(data['clouds'])


listener = keyboard.Listener(
    on_press=None,
    on_release=process)
listener.start()

while True:
    os.system('clear')
    print('Tick',  tick)
    n.process_helicopter(hel, c)
    hel.print_menu()
    n.print_map(hel, c)
    tick += 1
    time.sleep(TIME_SLEEP)
    if tick % TREE_UPDATE == 0:
        n.generate_tree()
    if tick % FIRE_UPDATE == 0:
        n.fire_update()
    if tick % CLOUDS_UPDATE == 0:
        c.update_couds()