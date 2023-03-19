import os

app_root = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", ".."))
build_root = os.path.realpath(os.path.join(app_root, "build"))
source_root = os.path.realpath(os.path.join(app_root, "source"))
mods_root = os.path.realpath(os.path.join(app_root, "mods"))
