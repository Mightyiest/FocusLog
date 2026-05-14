import os

def get_app_data_dir():
    base = os.environ.get("LOCALAPPDATA")
    if not base:
        base = os.path.expanduser("~")
    path = os.path.join(base, "FocusLog")
    os.makedirs(path, mode=0o700, exist_ok=True)
    return path
