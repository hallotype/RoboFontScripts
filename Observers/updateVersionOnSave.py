"""
It is an observer which means it run if a certain event happens. In this case: Font Will Save.

- Scripts look if ‘version’ is in font.lib, if not it adds it. If present: +=1
- Makes a glyphs called ‘version’ or clears it if already present, make the width 1000 
- Calculates a scale factor for the upcoming content.:
 - The word “ version “ (two spaces included) 
 - The integer in font.lib[‘version’]
- Mark the glyph some reddish colour

Things to be improved: if ‘space’, or any of the glyphs in the word ‘version’ and all the 
figures (0123456789) not present in font, it breaks.

Probably this has nothing to do with versioning and more a simple counter how much you saved the ufo :)

----

HalloType / Thom Janssen / 2020 

LICENSE: The Unlicense / Public Domain

"""


from mojo.events import addObserver, removeObserver
from lib.tools.notifications import PostNotification
from mojo.events import postEvent

event = "fontWillSave" 

class myObserver():
		
	def __init__(self):
		addObserver(self, "mainFunction", event)
		
	def mainFunction(self, info):
		f = CurrentFont()
		if 'version' not in f.lib:
		    f.lib['version'] = 0
		f.lib['version'] += 1
		if not 'version' in f:
		    f.newGlyph('version')
		g= f['version']
		g.clear()
		g.width = 1000

		# calc with of word ' version ', note two spaces
		word = " version "
		aw = 0 # advance width
		for l in word:
			aw += f[f.naked().unicodeData.glyphNameForUnicode(ord(l))].width
			#print aw
		# place ' version '
		aws = 0
		for l in word:
			c = f.naked().unicodeData.glyphNameForUnicode(ord(l))
			g.appendComponent(c, (aws, 660), (1000/aw,1000/aw))
			aws += f[c].width*(1000/aw)
		##
		##
		# same thing now the number
		word = str(f.lib['version'])
		aw = 0
		for l in word:
			aw += f[f.naked().unicodeData.glyphNameForUnicode(ord(l))].width
		aws = 0
		for l in word:
			c = f.naked().unicodeData.glyphNameForUnicode(ord(l))
			g.appendComponent(c, (aws, 0), (1000/aw,1000/aw))
			aws += f[c].width*(1000/aw)

		g.mark = (1.0, 0.23, 0.11,1)


myObserver()