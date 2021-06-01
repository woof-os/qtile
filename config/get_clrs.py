import pywal
import json
import os

with open(os.getenv('HOME') + '/.config/qtile/config/settings.json', 'r') as file:
    f = json.load(file)
    wal = f['looks']['wallpaper']
    os.system('wal -i' + str(f['looks']['wallpaper']))

img = pywal.image.get(str(wal).replace('~', os.getenv('HOME')))
clrs = pywal.colors.get(img)

with open(os.getenv('HOME') + '/.config/qtile/config/colors.json', 'w') as file:
    json.dump(clrs, file)