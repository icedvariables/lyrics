import urllib2
from lyricpage import LyricPage
import pprint

l = LyricPage(urllib2.urlopen("http://www.azlyrics.com/lyrics/eminem/rapgod.html").read())
print l.song, "by", l.author, "\n"
pprint.pprint(l.lyrics.blocks)
