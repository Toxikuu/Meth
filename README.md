# Meth
Meth is a very simple drawing program written in python with pygame.
It supports a handful of colors, clearing, resizing the canvas, saving screenshots of the canvas, and erasing.
It does not support undoing, panning, fill bucket, and point resizing, to name a few.
I created it to do math problems on my computer (hence the name), but it can also be used for simple drawings.

## Compatibility
This program is not compatible with windows.
It was made for my personal use on linux, and as such, was only tested on my personal setup.
It may or may not work for you, but it's not a complicated program, so configuring it to work on your machine should be fairly trivial.

## Installation
Installation commands:
```console
$ git clone https://github.com/Toxikuu/Meth.git
$ cd Meth
$ chmod +x install.sh
$ ./install.sh
```

## Keybinds
Meth has some keybinds:
- c: clears the canvas
- s: takes a screenshot and saves it to the screenshots folder
- p: changes color to pink
- y: changes color to yellow
- r: changes color to red
- g: changes color to green
- b: changes color to blue
- w: changes color to white

## Colors
The colors default to a limited version of the catppuccin mocha pallate. 
They may be easily changed by editing the rgb color definitions on lines 13-19.

## Hackability
It should be fairly easy to add new colors or edit basic functionality.
Just follow the existing pattern.
Adding new features (such as panning or undoing) may require a greater understanding of pygame.
One option you may want to change is the framerate on line 93.
