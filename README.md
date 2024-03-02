Icarus Quality-of-Life Mods
===========================
This is a collection of small mods that are designed to improve the experience, notably around time spent grinding,
in _Icarus_. As Icarus developers don't officially have mod support, these mods (alike all Icarus mods) need to be
updated whenever the devs release a game update.

I don't use a mod manager, however this script will merge the mods into the latest game schema ensuring that the mods
don't overwrite new content.

Among the changes, two are key:

* Increased _Electronics_ production 5-fold, drastically decreasing tier-4 grind
* Added the ability to craft _Workshop Repair Kits_ on-world, allowing you to maintain workshop items without spending
  mission credits or leaving the planet

New Frontiers Changes
=====================
_New Frontiers_ adds new tools providing curious perks, but otherwise aims not to make anything better than the core
game. Notably, the expansion also requires you to visit new biomes in order to expand.

The _Cold Steel Pickaxe_ creates an ore that provides the ores of other biomes, which negates the core tenant of the
_New Frontiers_ need to explore. As such, changes have been made (in the Degrind mod) to re-balance this:

* Frozen Ore no longer provides special ores (forcing exploration into other biomes)
* Cold Steel and Obsidian tools are equal to Platinum tools
* The Miasmic Pickaxe is now (by far) the most efficient pickaxe, but only once the noxious crust is cleansed

Degrind
-------
The _Degrind_ mod is designed to speed-up gameplay & remove excessive tedious elements. Notable focal points of this
mod are:

* Reduce effort to get to T4
* Remove restraints that force solo players to do a lot of back and forth

To build just the `degrind` mod:

    ./compile degrind

### Recipes:

* Stone building items leather reduced to 1
* Concrete mix now outputs 5 units
* Steel Rebar now outputs 25 units
* Electronics now outputs 5 units
* Epoxy (bone) now requires only 1 Crushed Bone
* Crushed Bone now requires only 1 Bone
* All tea/coffee drinks now only need 5 leaves
* Added a Workshop Repair Kit recipe for on-world Workshop item repairs, requires 5 composites and 5 carbon fiber,
  crafted at the Fabricator
* Added a Rope recipe from Fur, similar to the Leather recipe
* Basic lights only require 2 Iron
* Frozen Ore no longer provides Super Cooled Ice, Obsidian or Scoria, but will produce more Iron & Copper

### Items:

* Biofuel/Electric Radar no longer a backpack item
* Biofuel/Electric Extractor no longer a backpack item
* Reduced pill weight to 25g
* Increased all tonic durations to 900s
* Steel Screw stack size increased to 500
* Steel Rebar stack size increased to 200
* Animal Fat stack size increased to 100
* T4 Armor (composite, obsidian) provide movement speed boost stats, totalling in +50% movement speed
* All pickaxes now have increased mining radius

### Talents:

* Lucky Strike (insta-mining) probability increased to 5%/10%/15% depending on talent rank
* Peerless Lumberjack (insta-tree) probability increased to 25%/37%/50% depending on talent rank

### World:

* Increased ore deposit min/max volumes by 10x
* Reduced ore deposit mining time by half

Energy
------
The _Energy_ mod is designed to address the lack of batteries and the requirement that nearly everything is ALWAYS ON.
This mod makes biofuel easier to produce and increases the output of generators.

    ./compile energy

### Recipes:

* Changed Raw Meat -> Fuel to only require 1 raw meet (no sap) and produce 500 (up from 100) fuel units
* Added Fuel recipe for 1x Spoiled Meat -> 500 fuel

### Items:

* Removed the clogging mechanic from Water Wheels
* Increased Water Wheel power output to 5,000
* Increased Solar power output to 10,000
* Increased Wind Turbine power output to 5,000
* Increased Generator output to 15,000

Food
----
The _Food_ mod tidies up some quirks in the kitchen.

    ./compile food

### Recipes:

* Raw Meat can now also be crafted at the Kitchen Bench
* Tonics & Pills can now also be crafted at the Advanced Kitchen Bench
* Cooked Meats can now be crafted at all stoves
* Coffee/Tea can now be crafted at all stoves

### Items:

* Deep Freeze capacity doubled

Mounts
------
The _Mounts_ mod is aimed at making transport less vexing.

    ./compile mounts

### Mounts:

* Buffalo is now rideable when it has a Cargo Saddle or Cart attached
* Buffalo cart speed debuff removed
* Buffalo stamina regen increased 300%
* Increased cargo slots of all saddles (intended to aid in carrying of miasmics)

Compiling Mods
==============
Preparing Source Content
------------------------
First, you'll need the _UnrealPak_ tool to extract and repack the Unreal Engine `pak` files. The Icarus modding
community has created an archive of the best version with helpers
[here](https://drive.google.com/file/d/1f8J_2A0GgDIAU6Ekq7Ef6GELnpHpK8wT/view?usp=sharing).

Start by extracting the latest content from the game's `data.pak`:

* `Steam\steamapps\common\Icarus\Icarus\Content\Data\data.pak`
* drag this file into the `_Unpack.bat` file in _DRGPacker2_
* copy the generated `data` directory to the `source` directory in this repo (so you now have a `source/data/..`
  directory)

Compiling Mods
--------------
You can compile one, many or all mods with the same command:

    ./compile [modname] [modname..]

The mods are generated in order, if there is a conflict, the last one on the list will overwrite the former. Currently
there are no conflicts in included mods.

    # Complile all mods    
    ./compile

    # Equiv. to
    ./compile degrind energy food mounts

This will create a `data` directory in the `build` directory, use this to repack your mod `pak` file.

Creating The Mod File
---------------------
Edit `_Repack.bat` and change `Icarus\Content\*.*` to `Icarus\Content\data\*.*` as we're only creating "data"
modifications to the game.

* drag the generated `data` directory (in the `build` directory) to the `_Repack.bat` file
* rename the generated file to something appropriate, but it MUST end in `_P.pak`
* move it to the Icarus mods folder: `Steam\steamapps\common\Icarus\Icarus\Content\Paks\mods`

Launch the game!

VM Shared Folders Helpers
-------------------------
These helpers are assuming you're using an Linux VM guest under a Windows VM host. If you have a VMWare shared folder 
named `vm_shared`, use `./vm_mount` to mount it to `/mnt/vm_shared` and `./vm_export` to copy your build pak there.
