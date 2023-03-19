#!/bin/env python3
import icarus
import sys

if __name__ == '__main__':
    icarus.clean_build_directory()

    if len(sys.argv) == 1:
        print("Compiling all mods..")
        for mod in icarus.get_all_mods():
            print("Adding mod: " + mod)
            icarus.add_mod_dir(mod)
    else:
        for mod in sys.argv[1:]:
            if icarus.mod_exists(mod):
                print("Adding mod: " + mod)
                icarus.add_mod_dir(mod)
            else:
                print("Skipping invalid mod: " + mod)
