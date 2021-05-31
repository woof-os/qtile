import json
import os

with open("{}/.config/qtile/config/settings.json".format(os.getenv("HOME"))) as file:
    conf = json.load(file)


def display_settings():
    for i in conf:
        print("\n\n")
        print(i)
        print("****")
        for s in conf[i]:
            print(f"{s} : {conf[i][s]}")


def change_setting(main: str, prop: str, val: str):
    conf[main][prop] = val
    file = open("{}/.config/qtile/config/settings.json".format(os.getenv("HOME")), 'w')
    json.dump(conf, fp=file)
    file.close()


display_settings();

# while True:
#     prop_in = input("What head setting do you want to change? ")
#     prop = input(f"What sub setting of {prop_in} do you want to change? ")
#     val = input("What value do you want to set it to? ")
#     change_setting(prop_in, prop, val)
