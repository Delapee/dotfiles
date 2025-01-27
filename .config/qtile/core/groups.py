from libqtile.config import DropDown, Group, Key, Match, ScratchPad
from libqtile.lazy import lazy

from core.keys import keys, mod, shift
from utils import WORKSPACE_NAMES, config

workspaces = [
    {"name": WORKSPACE_NAMES[0], "key": "1", "matches": [], "lay": "bsp"},
    {
        "name": WORKSPACE_NAMES[1],
        "key": "2",
        "matches": [Match(wm_class="code-oss")],
        "lay": "columns",
    },
    {
        "name": WORKSPACE_NAMES[2],
        "key": "3",
        "matches": [Match(wm_class="firefox")],
        "lay": "bsp",
    },
    {
        "name": WORKSPACE_NAMES[3],
        "key": "4",
        "matches": [Match(wm_class="brave")],
        "lay": "bsp",
    },
    {
        "name": WORKSPACE_NAMES[4],
        "key": "5",
        "matches": [Match(wm_class="discord")],
        "lay": "bsp",
    },
    {
        "name": WORKSPACE_NAMES[5],
        "key": "6",
        "matches": [Match(wm_class="Spotify")],
        "lay": "bsp",
    },
    {
        "name": WORKSPACE_NAMES[6],
        "key": "7",
        "matches": [Match(wm_class="nemo")],
        "lay": "bsp",
    },
    {"name": WORKSPACE_NAMES[7], "key": "8", "matches": [], "lay": "bsp"},
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

terminal = config["terminal"]

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "terminal",
                f"{terminal}",
                opacity=1,
                x=0.1,
                y=0.15,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=True,
            ),
            DropDown(
                "btop",
                f"{terminal} btop",
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
