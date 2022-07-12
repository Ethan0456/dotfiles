import os
import re
import socket
import subprocess
import psutil
import json
import keyboard

from typing import List  # noqa: F401
#from custom.bsp import Bsp as CustomBsp

from libqtile import bar, layout, widget, hook
#from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.config import (KeyChord,Key,Screen,Group,Drag,Click,ScratchPad,DropDown,Match,)
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command import lazy
from libqtile import qtile

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice
fox="firefox"
brave="brave-browser"
os.system('/home/ethan/.config/qtile/autostart.sh')
keys = [
         ### The essentials
        Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
        Key(["control", "shift"], "Return",
             lazy.spawn("variety -p"),
             desc='Launches previous'
             ),
        Key([mod], "k",
             lazy.spawn("key"),
             desc='Launches key'
             ),
        Key(["control"], "Return",
             lazy.spawn("variety -n"),
             desc='Launches varitey'
             ),
        Key(["mod1","shift"], "c",
             lazy.spawn("selector"),
             desc='Launches selector'
             ),
        Key(["mod1" ,"shift"], "v",
             lazy.spawn("dselector"),
             desc='Launches dselector'
             ),
        Key([mod], "w",
             lazy.spawn("wificon"),
             desc='Launches wificon'
             ),
        Key([mod], "s",
             lazy.spawn("ss"),
             desc='Launches screenshooter'
             ),
        Key([mod], "r",
            lazy.spawn("redshift -O 5000"),
            desc='Launched Redshift'
            ),
        Key([mod], "z",
             lazy.spawn("xrandr --output VGA1 --brightness 0.5"),
             desc='decrease brightness'
             ),
        Key([mod, "shift"], "z",
             lazy.spawn("xrandr --output VGA1 --brightness 1.0"),
             desc='increase brightness'
             ),
        Key([mod], "e",
            lazy.spawn("redshift -x"),
            desc='Launched Reset Redshift'
            ),
         Key([mod], "a",
            lazy.spawn("atril"),
            desc='Launches My Terminal'
            ),
        Key([mod], "p",
            lazy.spawn("sinkswitcher"),
            desc='Changes Sink'
            ),
   # playerctl commands 
        Key([mod, "mod1"], "p",
            lazy.spawn("playerctl -a play"),
            desc='Changes Sink'
            ),
        Key([mod, "mod1"], "t",
            lazy.spawn("playerctl -a play-pause"),
            desc='Changes Sink'
            ),
        Key([mod, "mod1"], "q",
            lazy.spawn("playerctl -a pause"),
            desc='Changes Sink'
            ),
        Key([mod, "mod1"], "s",
            lazy.spawn("playerctl -a stop"),
            desc='Changes Sink'
            ),

         Key([mod, "shift"], "d",
            lazy.spawn("rofi -show run -show-icons -display-drun ''"),
            desc='Launches rofi run'
            ),
        Key([mod], "d",
             lazy.spawn("rofi -show drun -show-icons -disp;ay-drun ''"),
             desc='Run Launcher'
             ),
        Key([mod], "c",
             lazy.spawn("code"),
             desc='Run vscode'
             ),
	 Key([mod], "o",
             lazy.spawn("opera"),
             desc='Run opera'
             ),
	Key([mod], "t",
             lazy.spawn("thunar"),
             desc='Run thunar'
             ),
	Key([mod, "shift"], "n",
             lazy.spawn("nitrogen"),
             desc='Run nitro'
             ),
	 Key([mod], "b",
             lazy.spawn(brave),
             desc='Run brave'
             ),
        Key([mod, "shift"], "b",
            lazy.spawn("brave --incognito"),
            desc='Run brave incognito'
            ),
         Key([mod], "v",
             #lazy.spawn("dmenu_run -p 'Run: '"),
             lazy.spawn(fox),
             desc='Run firefox'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "o",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod], "b", lazy.hide_show_bar(), desc="Hides the bar"),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         # ### Switch focus to specific monitor (out of three)
         # Key([mod], "w",
         #     lazy.to_screen(0),
         #     desc='Keyboard focus to monitor 1'
         #     ),
         # Key([mod], "e",
         #     lazy.to_screen(1),
         #     desc='Keyboard focus to monitor 2'
         #     ),
         # Key([mod], "r",
         #     lazy.to_screen(2),
         #     desc='Keyboard focus to monitor 3'
         #     ),
         # Switch focus of monitors
         # Key([mod], "period",
         #     lazy.next_screen(),
         #     desc='Move focus to next monitor'
         #     ),
         # Key([mod], "comma",
         #     lazy.prev_screen(),
         #     desc='Move focus to prev monitor'
         #     ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         # KeyChord(["control"],"e", [
         #     Key([], "e",
         #         lazy.spawn("emacsclient -c -a 'emacs'"),
         #         desc='Launch Emacs'
         #         ),
         #     Key([], "b",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
         #         desc='Launch ibuffer inside Emacs'
         #         ),
         #     Key([], "d",
         #         lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
         #         desc='Launch dired inside Emacs'
         #         ),
        #      Key([], "i",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
        #          desc='Launch erc inside Emacs'
        #          ),
        #      Key([], "m",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
        #          desc='Launch mu4e inside Emacs'
        #          ),
        #      Key([], "n",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
        #          desc='Launch elfeed inside Emacs'
        #          ),
        #      Key([], "s",
        #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
        #          desc='Launch the eshell inside Emacs'
        #          ),
             # Key([], "v",
             #     lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
             #     desc='Launch vterm inside Emacs'
             #     )]),
        #  ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         # KeyChord([mod ,"shift"], "p", [
         #     Key([], "e",
         #         lazy.spawn("./dmscripts/dm-confedit"),
         #         desc='Choose a config file to edit'
         #         ),
         #     Key([], "i",
         #         lazy.spawn("./dmscripts/dm-maim"),
         #         desc='Take screenshots via dmenu'
         #         ),
         #     Key([], "k",
         #         lazy.spawn("./dmscripts/dm-kill"),
         #         desc='Kill processes via dmenu'
         #         ),
         #     Key([], "l",
         #         lazy.spawn("./dmscripts/dm-logout"),
         #         desc='A logout menu'
         #         ),
         #     Key([], "m",
         #         lazy.spawn("./dmscripts/dm-man"),
         #         desc='Search manpages in dmenu'
         #         ),
         #     Key([], "o",
         #         lazy.spawn("./dmscripts/dm-bookman"),
         #         desc='Search your qutebrowser bookmarks and quickmarks'
         #         ),
         #     Key([], "r",
         #         lazy.spawn("./dmscripts/dm-reddit"),
         #         desc='Search reddit via dmenu'
         #         ),
         #     Key([], "s",
         #         lazy.spawn("./dmscripts/dm-websearch"),
         #         desc='Search various search engines via dmenu'
         #         ),
         #     Key([], "p",
         #         lazy.spawn("passmenu"),
         #         desc='Retrieve passwords with dmenu'
         #         )
         # ])
]

########################
# Define colors ########
########################
#Pywal Colors
colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
ColorZ=(colordict['colors']['color0'])
ColorA=(colordict['colors']['color1'])
ColorB=(colordict['colors']['color2'])
ColorC=(colordict['colors']['color3'])
ColorD=(colordict['colors']['color4'])
ColorE=(colordict['colors']['color5'])
ColorF=(colordict['colors']['color6'])
ColorG=(colordict['colors']['color7'])
ColorH=(colordict['colors']['color8'])
ColorI=(colordict['colors']['color9'])
colors= [   "#000000",                      #panel background
            "#000000",                      #
            "#00ff00",                      #groupnames - active
            "#ffffff",                      #groupnames - inactive
            "#ff6700",                      #groupnames - underline
            ["#ff0000","#000000"],          #net color
            ["#ff6700","#000000"],          #memory color
            ["#ffff00","#000000"],          #capslock color
            ["#00ff00","#000000"],          #volume color
            ["#00c300","#000000"],          #layout color
            ["#00d6ff","#000000"],          #CapslockIndicator
            ["#0000BF","#000000"]]          #date-time color


group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("VBOX", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("MUS", {'layout': 'monadtall'}),
               ("VID", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'floating'})]


### Widget Dark or Light Foreground Code ###
def theme(color):
    if color < "#7a7a7a":
        color_foreground = "#ffffff"
    else:
        color_foreground = "#000000"
    return color_foreground


groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 1, 
                "margin": 8,
                "border_focus": "ffffff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.Verticmod1ile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "#1c1f24",
         active_bg = ColorF,
         active_fg = theme("#000000"),
         inactive_bg = ColorG,
         inactive_fg = "000000",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 150,
         ),
    layout.Floating(**layout_theme)
]


layout_theme = {
    "border_width": 3,
    "margin": 9,
    "border_focus": ColorC,
    "border_normal": ColorZ,
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

# ls = [ColorA,ColorB,ColorC,ColorD,ColorE,ColorF,ColorG,ColorH,ColorI]
# global common_forground
# def theme():
#     common_forground = "#000000"
#     for i in ls:
#         if (i < "#7f7f7f"):
#             common_forground = "#ffffff"




##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize = 12,
    padding = 2,
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
            #   widget.Sep(
            #            linewidth = 0,
            #            padding = 6,
            #            ),
             widget.Image(
                     filename = "/home/ethan/.config/qtile/icons/triangle1.png",
                      scale = "False",
                      margin_x = 2,
                      margin_y = 2,
                      mouse_callbacks = {'Button3': lambda: qtile.cmd_spawn(myTerm),'Button1' : lambda: qtile.cmd_spawn("rofi -show drun")},
                     ),
             widget.Sep(
                       linewidth = 0,
                       padding = 6,
                      foreground = theme("#000000")
                       ),
              widget.GroupBox(
                       font = "Fira Code Bold",
                       fontsize = 9, 
                       margin_y = 4,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[3],
                       rounded = False,
                       disable_drag=True,
                       highlight_color = "#00ff6700",#colors[4],
                       highlight_method = "line",
                       this_current_screen_border = colors[6][0],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6][0],
                       other_screen_border = colors[4],
                      foreground = theme("#000000")
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "JetBrains Mono Nerd Font",
                       padding = 10,
                      foreground = theme("#000000")
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                      foreground = theme("#000000")
                       ),
              widget.WindowName(
                      foreground = "00000000",
                       padding = 0
                       ),
              widget.Systray(
                       padding = 5,
                       icon_size = 20
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                      foreground = theme("#000000")
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
            widget.Image(
                     filename = "~/.config/qtile/icons/speed1.png",
                      scale = "False",
                      margin_x = 3,
                      margin_y = 3
                    #   mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                     ),
             widget.Net(
                       interface = "eno1",
                       format = '{down} ↓↑ {up}',
                      foreground = theme("#000000"),
                       padding = 5
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
             widget.Image(
                     filename = "~/.config/qtile/icons/memory.png",
                      scale = "False",
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                     ),
              widget.Memory(
                      foreground = theme("#000000"),
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
               widget.Image(
                     filename = "~/.config/qtile/icons/cpu1.png",
                      scale = "False",
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(brave + 'https://wazirx.com')},
                     ),
              widget.ThermalSensor(
                      foreground = theme("#000000"),
                       padding = 5
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
             widget.Image(
                     filename = "~/.config/qtile/icons/volume.png",
                      scale = "False",
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + 'pavucontrol')},
                     ),
              widget.Volume(
                       limit_max_volume = True, 
                      foreground = theme("#000000"),
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                      foreground = theme("#000000"),
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                      foreground = theme("#000000"),
                       padding = 5
                       ),
            widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
            widget.Image(
                     filename = "~/.config/qtile/icons/capslock2on.png",
                      scale = "False",
                      #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
                     ),
              widget.CapsNumLockIndicator(
                      foreground = theme("#000000")
                       ),
             widget.Sep(
                       linewidth = 0,
                       padding = 20,
                      foreground = theme("#000000")
                       ),
             widget.Image(
                     filename = "~/.config/qtile/icons/calender.png",
                      scale = "False",
                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(brave + 'google calender')},
                     ),
              widget.Clock(
                      foreground = theme("#000000"),
                       format = "%A, %B %d - %H:%M %p"
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1, size=20, background = "#00000026")),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1, size=17)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
