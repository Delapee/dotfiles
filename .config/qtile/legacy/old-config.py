import datetime
import os

from libqtile import bar, layout, widget
from libqtile.config import (
    Click,
    Drag,
    DropDown,
    Group,
    Key,
    KeyChord,
    Match,
    ScratchPad,
    Screen,
)
from libqtile.lazy import lazy

mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"
terminal = "kitty"
home = os.path.expanduser("~")


# resize functions
def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


keys = [
    # Qtile
    Key([mod, shift], "r", lazy.restart(), desc="Restart Qtile"),
    # Essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    # Switch focus
    Key(
        [mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod], "Left", lazy.layout.left(), desc="Move focus left in current stack pane"
    ),
    Key(
        [mod],
        "Right",
        lazy.layout.right(),
        desc="Move focus right in current stack pane",
    ),
    Key(
        [mod],
        "x",
        lazy.next_screen(),
        desc="Move focus to next monitor",
    ),  # TODO find a better hotkey
    # Move windows position in current stack
    Key(
        [mod, shift],
        "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.move_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, shift],
        "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.move_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, shift],
        "Left",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, shift],
        "Right",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right(),
        desc="Move windows right in the current stack",
    ),
    # Flip layout
    Key([mod, control], "Down", lazy.layout.flip_down(), desc="Flip layout down"),
    Key([mod, control], "Up", lazy.layout.flip_up(), desc="Flip layout up"),
    Key(
        [mod, control],
        "Left",
        lazy.layout.flip_left(),
        lazy.layout.swap_column_left(),
        desc="Flip layout left",
    ),
    Key(
        [mod, control],
        "Right",
        lazy.layout.flip_right(),
        lazy.layout.swap_column_left(),
        desc="Flip layout right",
    ),
    # Toggle between layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, shift], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    # Window resizing
    Key([mod, alt], "Left", resize_left, desc="Resize window left"),
    Key([mod, alt], "Right", resize_right, desc="Resize window Right"),
    Key([mod, alt], "Up", resize_up, desc="Resize windows upward"),
    Key([mod, alt], "Down", resize_down, desc="Resize windows downward"),
    Key([mod, alt], "n", lazy.layout.normalize(), desc="Normalize window size ratios"),
    # Window states
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, shift], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "i",
        lazy.window.toggle_floating(),
        desc="Toggle floating mode for a window",
    ),
    # Floating mode
    # Key([mod] , "i", lazy.layout.grow(), desc="Increase window size"),
    # Key([mod, shift] , "i", lazy.layout.shrink(), desc="Decrease window size"),
    # Menus
    Key(
        [mod],
        "e",
        lazy.spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi"),
        desc="Launch Rofi (drun)",
    ),
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show run -theme ~/.config/rofi/launcher.rasi"),
        desc="Launch Rofi (run)",
    ),
    Key(
        [mod, shift],
        "e",
        lazy.spawn("" + home + "/.local/bin/power"),
        desc="Power Menu",
    ),
    Key(
        [mod, shift],
        "n",
        lazy.spawn("" + home + "/.local/bin/nmgui"),
        desc="Network Menu",
    ),
    # Program launches
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key(
        [mod, "control"],
        "b",
        lazy.spawn("google-chrome-stable"),
        desc="Launch Google Chrome",
    ),
    Key([mod], "f", lazy.spawn("nemo"), desc="Launch Nemo"),
    Key(
        [mod, "control"], "f", lazy.spawn(f"{terminal} -- ranger"), desc="Launch Ranger"
    ),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("term")),
    Key([mod, shift], "t", lazy.group["scratchpad"].dropdown_toggle("btop-term")),
    # Screenshots
    Key(
        [],
        "Print",
        lazy.spawn("" + home + "/.local/bin/prtscreen"),
        desc="Print Screen",
    ),
    Key(
        [mod],
        "Print",
        lazy.spawn("" + home + "/.local/bin/prtscreenregion"),
        desc="Print region of screen",
    ),
    Key(
        [mod, shift],
        "s",
        lazy.spawn("" + home + "/.local/bin/prtscreenregion"),
        desc="Print region of screen",
    ),
    # Audio
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.widget["pulsevolume"].increase_vol(),
        desc="Increase volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.widget["pulsevolume"].decrease_vol(),
        desc="Decrease volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.widget["pulsevolume"].mute(),
        desc="Toggle volume mute",
    ),
    # Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Play last audio",),
    # Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Play next audio"),
    # Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"),
    # # Key([mod], "F8", lazy.spawn("playerctl stop"), desc="Stop audio"),
    # Brightness
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Increase brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Decrease brightness",
    ),
    # Keychords
    KeyChord(
        [mod],
        "l",
        [
            Key(
                [mod],
                "d",
                lazy.spawn("discord --enable-gpu-rasterization"),
                desc="Launch Discord",
            ),
            Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
            Key(
                [],
                "t",
                lazy.spawn("cat /home/delape/.token | xclip -selection clipboard"),
                desc="Copy GitHub token into the clipboard",
            ),
        ],
        name="Launcher",
    ),
]

# -- Workspace --

workspace_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

workspaces = [
    {"name": workspace_names[0], "key": "1", "matches": [], "lay": "bsp"},
    {
        "name": workspace_names[1],
        "key": "2",
        "matches": [Match(wm_class="code-oss")],
        "lay": "columns",
    },
    {
        "name": workspace_names[2],
        "key": "3",
        "matches": [Match(wm_class="firefox")],
        "lay": "bsp",
    },
    {
        "name": workspace_names[3],
        "key": "4",
        "matches": [Match(wm_class="google-chrome")],
        "lay": "bsp",
    },
    {
        "name": workspace_names[4],
        "key": "5",
        "matches": [Match(wm_class="discord")],
        "lay": "bsp",
    },
    {
        "name": workspace_names[5],
        "key": "6",
        "matches": [Match(wm_class="Spotify")],
        "lay": "bsp",
    },
    {
        "name": workspace_names[6],
        "key": "7",
        "matches": [Match(wm_class="nemo")],
        "lay": "bsp",
    },
    {"name": workspace_names[7], "key": "8", "matches": [], "lay": "bsp"},
    {"name": workspace_names[7], "key": "9", "matches": [], "lay": "bsp"},
]

groups = []

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=workspace["lay"]))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, shift],
            workspace["key"],
            *(
                lazy.window.togroup(workspace["name"]),
                lazy.group[workspace["name"]].toscreen(toggle=True),
            ),
            desc="Move focused window to another group",
        )
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "kitty",
                opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "btop-term",
                "kitty btop",
                opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
        ],
    )
)

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def _date_fmt() -> str:
    date = datetime.datetime.now()

    day = date.strftime("%d")
    weekday_number = int(date.strftime("%w"))
    month_number = int(date.strftime("%m"))

    return "{}, {} {}".format(days[weekday_number], months[month_number - 1], day)


def _parse_window_name(text):
    """Simplifies the names of a few windows, to be displayed in the bar"""
    target_names = ["Mozilla Firefox", "Discord", "Google Chrome", "Code - OSS"]

    try:
        return next(filter(lambda name: name in text, target_names), text)
    except TypeError:
        return text


def widgets():
    return bar.Bar(
        [
            widget.CurrentLayout(),
            widget.GroupBox(),
            widget.WindowName(
                empty_group_string="Desktop",
                max_chars=40,
                parse_text=_parse_window_name,
            ),
            widget.Spacer(),
            widget.Clock(format="%H:%M - {}".format(_date_fmt())),
            widget.Spacer(),
            widget.PulseVolume(
                fmt="Vol: {}",
                limit_max_volume=True,
                step=1,
            ),
            widget.Battery(),
        ],
        30,
        margin=[2, 0, 0, 0],
        border_width=[0, 0, 0, 0],
        border_color="#88C0D0",
    )


screens = [
    Screen(
        wallpaper=home + "/.config/qtile/img/wallpapers/gun.jpg",
        wallpaper_mode="fill",
        top=bar.Gap(2),
        bottom=widgets(),
        left=bar.Gap(2),
        right=bar.Gap(2),
    ),
]

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
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
