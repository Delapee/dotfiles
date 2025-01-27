from libqtile import bar

from core.widgets import (
    gen_battery,
    gen_clock,
    gen_cpu,
    gen_gap,
    gen_groupbox,
    gen_layout,
    gen_memory,
    gen_net,
    gen_os_icon,
    gen_spacer,
    gen_temperature,
    gen_textBox,
    gen_volume,
)
from utils import color, config

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    padding=2,
    background=color["bg"],
)
extension_defaults = widget_defaults.copy()


def create_bar():
    """Create top bar, defined as function to allow duplication in other monitors"""
    return bar.Bar(
        [
            gen_os_icon(),
            gen_gap(),
            *gen_groupbox(),
            gen_gap(),
            gen_layout(),
            gen_spacer(),
            gen_clock(),
            gen_spacer(),
            gen_net(),
            gen_gap(),
            gen_cpu(),
            gen_textBox(" - "),
            gen_temperature(),
            gen_gap(),
            gen_memory(),
            gen_gap(),
            gen_volume(),
            gen_gap(),
            gen_battery(),
        ],
        30,
        margin=[0, 6, 2, 2],
        border_width=[0, 0, 0, 0],
        border_color=color["fg"],
    )


main_screen_bar = create_bar()

if config["two_monitors"]:
    secondary_screen_bar = create_bar()
