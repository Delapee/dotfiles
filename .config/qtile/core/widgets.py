import datetime

from libqtile import widget

from utils import ICON_DIR, WORKSPACE_NAMES, color, config

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

group_box_settings = {
    "active": color["fg"],
    "block_highlight_text_color": color["fg"],
    "this_current_screen_border": color["fg"],
    "this_screen_border": color["fg"],
    "urgent_border": color["red"],
    "background": color["bg"],
    "other_current_screen_border": color["bg"],
    "other_screen_border": color["bg"],
    "highlight_color": color["darkgray"],
    "inactive": color["gray"],
    "foreground": color["white"],
    "borderwidth": 2,
    "disable_drag": True,
    # "fontsize": 18,
    "highlight_method": "line",
    "padding_x": 5,
    "padding_y": 8,
    "rounded": False,
}


def date_fmt() -> str:
    date = datetime.datetime.now()

    day = date.strftime("%d")
    weekday_number = int(date.strftime("%w"))
    month_number = int(date.strftime("%m"))

    return "{}, {} {}".format(days[weekday_number], months[month_number - 1], day)


def parse_window_name(text):
    "Simplifies the names of a few windows, to be displayed in the bar"
    if "Code - OSS" in text:
        return "VS Code"

    target_names = ["Mozilla Firefox", "Discord", "Google Chrome"]
    try:
        return next(filter(lambda name: name in text, target_names), text)
    except TypeError:
        return text


# Widgets
def gen_gap():
    return widget.Sep(
        foreground=color["fg"],
        padding=15,
        linewidth=2,
        size_percent=55,
        background=color["bg"],
    )


def gen_os_icon():
    return widget.TextBox(
        text="󰣇",
        fontsize=22,
        padding=6,
    )


def gen_layout() -> widget:
    return widget.CurrentLayoutIcon(
        custom_icon_paths=[ICON_DIR],
        scale=0.65,
        use_mask=True,
    )


def gen_groupbox():
    return (
        widget.GroupBox(
            font="Font Awesome",
            visible_groups=[*WORKSPACE_NAMES[:2]],
            **group_box_settings,
        ),
        widget.GroupBox(
            font="Awesome 6 Brands",
            visible_groups=[*WORKSPACE_NAMES[2:6]],
            **group_box_settings,
        ),
        widget.GroupBox(
            font="Font Awesome",
            visible_groups=[*WORKSPACE_NAMES[6:]],
            **group_box_settings,
        ),
    )


# NOT USING
def gen_windowName():
    return widget.WindowName(
        empty_group_string="Desktop",
        max_chars=40,
        parse_text=parse_window_name,
    )


def gen_spacer():
    return widget.Spacer()


def gen_clock():
    return widget.Clock(format="%H:%M - {}".format(date_fmt()))


def gen_volume():
    return widget.PulseVolume(
        fmt="Vol: {}",
        limit_max_volume=True,
        step=1,
    )


def gen_battery():
    return widget.Battery(format="{percent:2.0%} {hour:d}:{min:02d}")


def gen_net():
    return widget.Net(
        interface=config["network"],
        format="{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}",
        update_interval=5,
    )


def gen_cpu():
    return widget.CPU(format="CPU: {load_percent}%")


def gen_memory():
    return widget.Memory(
        format="RAM:{MemUsed: .2f}{mm}/{MemTotal:.0f}{mm}", measure_mem="G"
    )


def gen_temperature():
    return widget.ThermalZone(
        format="{temp}°C", format_crit="{temp}°C", high=80, crit=100
    )


def gen_textBox(msg: str):
    return widget.TextBox(text=f"{msg}")
