# OverlayWriter
Command line interface to edit text files for OBS/SLOBS overlays.

Currently designed directly for [Vaughan Esport's](https://vaughanesports.org) overlays.

## Features
- `set` - overwrites current values in the files
- `clear` - clears the files
- `set` - swaps the names and/or scores for team 1 and 2
- `get` - returns the names/scores of the teams and match

## Using Overlay Writer
### Setup
1. Clone this repo
2. In OBS/SLOBS select the `read from file` option for texts and select the appropriate file under the `textFiles` directory
3. Navigate to the directory in your terminal
4. Install requirements using `pip install -r requirements.txt`
5. Edit your overlay away!

**Tip:** Use the `custom extents` checkbox in the properties of text sources to center the text on your overlay at all times


### Example Usage
To change team 1's name to "The Better Team":  `ow set t1 The Better Team`

Run `ow --help` to see all commands and `ow {command} --help` to see sub commands.


## Configuration
### File Paths
All paths to the text files are found in `config.py`

Simply change the desired relative path to your desired path for the file.

### Console Colours
All console colours are set in `config.py`

Simply change the name of the colours in the square brackets.

List of colours [here](https://rich.readthedocs.io/en/latest/appendix/colors.html?highlight=colors)