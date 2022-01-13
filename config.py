import os
import json
import subprocess
from datetime import datetime

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import qtile
from libqtile import hook

with open("{}/.config/qtile/config/settings.json".format(os.getenv("HOME"))) as file:
    settings = json.load(file)

looks: dict = settings["looks"]
display: dict = settings["display"]

with open("{}/.config/qtile/config/colors.json".format(os.getenv("HOME"))) as file:
    colors_json = json.load(file)

colors = colors_json
wallpaper = looks["wallpaper"]

mod = "mod4"
terminal = "kitty"
browser = "brave"
file_manager = "pcmanfm"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using rofi",
    ),
    Key([mod], "t", lazy.spawncmd(), desc="Spawn a command using a prompt"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch web browser"),
    Key([mod], "c", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key(
        [mod], "v", lazy.spawn("rofi -show window"), desc="Show active windows in rofi"
    ),
    Key([mod], "f", lazy.spawn("flameshot gui"), desc="Open flameshot gui"),
    Key([mod], "s", lazy.spawn("scrot"), desc="Take full screen ss using scrot"),
    Key([mod], "d", lazy.spawn(f"notify-send '{datetime.now()}'"), desc="Show date and time"),
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1+shift+group letter = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

group_names = [
    ("code", {"layout": "bsp"}),
    ("wifi", {"layout": "max"}),
    ("box", {"layout": "zoomy"}),
    ("book", {"layout": "max"}),
    ("comment", {"layout": "max"}),
    ("gamepad", {"layout": "max"}),
    ("tv", {"layout": "max"}),
    ("coffee", {"layout": "floating"}),
    ("bone", {"layout": "monadtall"}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layout_theme = {
    "border_width": 1,
    "margin": 2,
    #     "border_focus": colors["color1"],
    #     "border_normal": colors["color2"],
    "border_focus": colors["border_focus"],
    "border_normal": colors["border_normal"],
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font="Fira Sans Medium",
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

power_widgets: list = [
    widget.Sep(
        linewidth=0,
        padding=8,
        background=colors["seperator"],
        foreground=colors["color2fg"],
    ),
    widget.TextBox(
        text="Shutdown",
        background=colors["color2"],
        foreground=colors["color2fg"],
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("shutdown now")},
    ),
    widget.TextBox(
        text="|", background=colors["color2"], foreground=colors["color2fg"]
    ),
    widget.TextBox(
        text="Reboot",
        background=colors["color2"],
        foreground=colors["color2fg"],
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("reboot")},
    ),
]

widgets_list: list = [
#     ### Run ###
#     widget.Sep(linewidth=0, padding=6, background=colors["start"]),
#     widget.Image(
#         filename="~/.config/qtile/config/manjaro.png",
#         margin=5,
#         background=colors["start"],
#         mouse_callbacks={"Button1": lambda: os.system("rofi -show drun")},
#     ),
#     widget.Sep(linewidth=0, padding=6, background=colors["start"]),
    ### Groups ###
    widget.Sep(linewidth=0, padding=6, background=colors["groups_bg"]),
    widget.GroupBox(
        font=looks["caret_font"],
        borderwidth=3,
        active=colors["active"],
        inactive=colors["inactive"],
        rounded=False,
        highlight_method="line",
        highlight_color=colors["groups_bg"],
        this_current_screen_border=colors["current_screen_tab"],
        this_screen_border=colors["color1"],
        other_screen_border=colors["bg"],
        foreground=colors["fg"],
        background=colors["groups_bg"],
    ),
    widget.Sep(padding=6, linewidth=0, background=colors["seperator"]),
    widget.Prompt(
        foreground=colors["active"],
        background=colors["groups_bg"],
        font="Jetbrains Mono",
        prompt="Woof: "
    ),
    widget.Sep(padding=6, linewidth=0, background=colors["seperator"]),
    widget.Spacer(),
    ### Systray ###
    widget.Systray(background=colors["systray"], padding=10),
    widget.Sep(linewidth=0, padding=6, background=colors["systray"]),

    ### Volume ###
    widget.Sep(padding=9, linewidth=0, background=colors["color3"]),
    widget.TextBox(
        text="volume-off",
        font="Font Awesome 5 Free Solid",
        foreground=colors["color3fg"],
        background=colors["color3"],
        fontsize=14,
        padding=0,
    ),
    widget.Volume(foreground=colors["color3fg"], background=colors["color3"]),
    widget.Sep(padding=6, linewidth=0, background=colors["color3"]),
    # widget.Sep(padding=12, linewidth=0, background=colors["seperator"]),
    ### Clock ###
    widget.Sep(padding=6, linewidth=0, background=colors["color1"]),
    widget.TextBox(
        foreground=colors["color1fg"],
        background=colors["color1"],
        text="calendar-alt",
        font="Font Awesome 5 Free Solid",
        #        Uncomment the below snippet to enable calendar as a notification if dunst uses monospace font.
        #        mouse_callbacks={
        #            "Button1": lambda: os.system(' notify-send "$(cal)" -i ICON ')
        #        },
    ),
    widget.Clock(
        foreground=colors["color1fg"],
        background=colors["color1"],
        format="%D",
    ),
    widget.Sep(padding=6, linewidth=0, background=colors["color3"]),
    widget.TextBox(
        foreground=colors["color5fg"],
        background=colors["color5"],
        text="clock",
        font="Font Awesome 5 Free Solid",
        #        Uncomment the below snippet to enable calendar as a notification if dunst uses monospace font.
        #        mouse_callbacks={
        #            "Button1": lambda: os.system(' notify-send "$(cal)" -i ICON ')
        #        },
    ),
    widget.Clock(
            foreground=colors["color5fg"],
            background=colors["color5"],
            format="%A - %H:%M"
    ),
    widget.Sep(padding=6, linewidth=0, background=colors["color1"]),
    # widget.Sep(padding=6, linewidth=0, background=colors["seperator"]),

]

# bar_margin = [int(layout_theme["margin"]/2), layout_theme["margin"], 0, layout_theme["margin"]]
bar_margin = 0

screen = Screen(
#     wallpaper=wallpaper,
#     wallpaper_mode="fill",
    top=bar.Bar(
       widgets_list,
       int(looks["panel-size"]),
       background=colors["bg"],
       opacity=float(looks["panel-opacity"]),
       margin=bar_margin,
   ),
)

screens = [screen]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_type="utility"),
        Match(wm_type="notification"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pomotroid"),
        Match(wm_class="cmatrixterm"),
        Match(title="Farge"),
        Match(wm_class="org.gnome.Nautilus"),
        Match(wm_class="feh"),
        Match(wm_class="plank"),
        Match(wm_class="gnome-calculator"),
        Match(wm_class="blueberry"),
        Match(wm_class="protonvpn"),
    ]
)


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

@hook.subscribe.startup
def runner():
    home = os.path.expanduser("~")
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])
    subprocess.Popen(["xwallpaper", "--zoom", wallpaper])

floating_types = ["notification", "toolbar", "splash", "dialog", "dock"]

@lazy.function
def float_to_front(qtile):
    """
    Bring all floating windows of the group to front
    """
    global floating_windows
    floating_windows = []
    for window in qtile.currentGroup.windows:
        if window.floating:
            window.cmd_bring_to_front()
            floating_windows.append(window)
    floating_windows[-1].cmd_focus()

@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, "parent"):
        window.parent.minimized = False


wmname = "LG3D"
