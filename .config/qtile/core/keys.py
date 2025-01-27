from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from utils import HOME, config

mod = "mod4"
control = "control"
shift = "shift"
alt = "mod1"
terminal = config["terminal"]


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
    Key([mod], "Tab", lazy.screen.toggle_group()),
    Key([mod, alt], "x", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, alt, shift], "x", lazy.prev_layout(), desc="Toggle last layout"),
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
        lazy.spawn("rofi -show drun"),
        desc="Launch Rofi (drun)",
    ),
    Key(
        [mod],
        "r",
        lazy.spawn("rofi -show run"),
        desc="Launch Rofi (run)",
    ),
    Key(
        [mod, shift],
        "e",
        lazy.spawn("" + HOME + "/.local/bin/power"),
        desc="Power Menu",
    ),
    Key(
        [mod, shift],
        "n",
        lazy.spawn("" + HOME + "/.local/bin/nmgui"),
        desc="Network Menu",
    ),
    # Program launches
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key(
        [mod, "control"],
        "b",
        lazy.spawn("brave"),
        # lazy.spawn("google-chrome-stable"),
        desc="Launch Google Chrome",
    ),
    Key([mod], "f", lazy.spawn("nemo"), desc="Launch Nemo"),
    Key(
        [mod, "control"], "f", lazy.spawn(f"{terminal} -- ranger"), desc="Launch Ranger"
    ),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("terminal")),
    Key([mod, shift], "t", lazy.group["scratchpad"].dropdown_toggle("btop")),
    # Screenshots
    Key(
        [],
        "Print",
        lazy.spawn("" + HOME + "/.local/bin/prtscreen"),
        desc="Print Screen",
    ),
    Key(
        [mod],
        "Print",
        lazy.spawn("" + HOME + "/.local/bin/prtscreenregion"),
        desc="Print region of screen",
    ),
    Key(
        [mod, shift],
        "s",
        lazy.spawn("" + HOME + "/.local/bin/prtscreenregion"),
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
