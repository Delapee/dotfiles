from subprocess import PIPE, Popen


def get_qtile_dir(home: str, xdg: str) -> str:
    try:
        open(f"{home}/{xdg}/config.py", "r").close()
        return f"{home}/{xdg}"
    except FileNotFoundError:
        process = Popen(
            ["pwd"],
            stdout=PIPE,
            text=True,
        )
        return process.communicate()[0].strip()
