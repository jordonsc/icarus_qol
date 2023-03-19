import os
import json
import shutil
from . import path, schema


def clean_build_directory():
    files = os.listdir(os.path.join(path.build_root))
    for file in files:
        if file == ".gitkeep":
            continue

        fn = os.path.join(path.build_root, file)
        if os.path.isfile(fn):
            os.remove(fn)
        elif os.path.isdir(fn):
            shutil.rmtree(fn)


def get_all_mods():
    mods = []
    for file in os.listdir(os.path.join(path.mods_root)):
        mod_path = os.path.join(path.mods_root, file)
        if os.path.isdir(mod_path):
            mods.append(file)

    return mods


def mod_exists(mod) -> bool:
    """
    Check if a mod name is a real directory in the mods_root.
    """
    mod_dir = os.path.join(path.mods_root, mod)
    return os.path.exists(mod_dir) and os.path.isdir(mod_dir)


def add_mod_dir(mod, pathline=None):
    """
    Processes all files in a directory, adding their contents to contents of the build directory.
    """
    if pathline is None:
        pathline = []

    files = os.listdir(os.path.join(path.mods_root, mod, *pathline))
    for file in files:
        mod_file = os.path.join(path.mods_root, mod, *pathline, file)
        if os.path.isfile(mod_file):
            # Process this file
            add_mod_file(mod, [*pathline, file])
        elif os.path.isdir(mod_file):
            # Recurse into the next directory
            add_mod_dir(mod, [*pathline, file])


def add_mod_file(mod, pathline):
    """
    Merges a mod file with the existing build file (or source file, if no build file exists yet) and writes it back
    to the build directory.
    """
    mod_fn = os.path.join(path.mods_root, mod, *pathline)
    source_fn = os.path.join(path.source_root, *pathline)
    build_fn = os.path.join(path.build_root, *pathline)

    print(" - {}".format(os.path.join(*pathline)))

    with open(mod_fn) as fp:
        data = json.load(fp)

    # If the file exists in the build directory, we'll merge that file with the mod file
    # If it does not exist in the build directory, we'll look for the original file in the source directory
    # If neither file exists (mod is adding a new file), we just write the new file
    src = {}
    if os.path.exists(build_fn):
        with open(build_fn) as fp:
            src = json.load(fp)
    elif os.path.exists(source_fn):
        with open(source_fn) as fp:
            src = json.load(fp)

    schema.merge_dict(src, data)

    os.makedirs(os.path.join(path.build_root, *pathline[0:-1]), exist_ok=True)
    with open(build_fn, "w") as fp:
        json.dump(src, fp, indent=4)
