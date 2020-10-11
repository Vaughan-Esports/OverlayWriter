# OverlayWriter
Command line interface to edit text files for OBS/SLOBS overlays.

Currently designed directly for [Vaughan Esports'](https://vaughanesports.org) overlays.

## Features
- `w` - write to different files quickly
- `c` - clear different files quickly
- `s` - swap the names and/or scores for team 1 and 2
- `g` - get the names/scores of the teams and match

## Using Overlay Writer
### Setup
1. Clone this repo
2. In OBS/SLOBS select the `read from file` option for texts and select the appropriate file under the `textFiles` directory
3. Navigate to the directory in your terminal
4. Edit your overlay away!


### Example Usage
To change team 1's name to "The Better Team":  `ow w t1 "The Better Team"`

Run `ow --help` to see all commands and `ow {command} --help` to see sub commands.

## To-Do
- [ ] Ability to change paths to text files