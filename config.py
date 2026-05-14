import os
from pathlib import Path

APP_DATA_DIR = None

def get_app_data_dir():
    global APP_DATA_DIR
    if APP_DATA_DIR is None:
        base = os.environ.get("LOCALAPPDATA")
        if not base:
            base = os.path.expanduser("~")
        path = os.path.join(base, "FocusLog")
        os.makedirs(path, exist_ok=True)
        APP_DATA_DIR = os.path.realpath(path)  # Resolve symlinks
    return APP_DATA_DIR

def safe_join(*parts):
    """Safely join path components within app data directory."""
    full_path = os.path.realpath(os.path.join(get_app_data_dir(), *parts))
    if not full_path.startswith(get_app_data_dir()):
        raise ValueError(f"Path traversal attempt detected: {full_path}")
    return full_path

# Application data files
APP_SETTINGS_FILE = safe_join("app_settings.json")
AUTO_EXCLUDE_FILE = safe_join("auto_excluded_apps.txt")
ACTIVE_SESSION_FILE = safe_join("active_session.json")
SESSIONS_DIR = safe_join("sessions")
CHAIN_FILE = safe_join("hash_chain.json")
LOG_FILE = safe_join("focuslog.log")

# Ensure sessions directory exists
os.makedirs(SESSIONS_DIR, exist_ok=True)
