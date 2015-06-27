import urllib2
from lyricpage import LyricPage

l = LyricPage(urllib2.urlopen("http://www.azlyrics.com/lyrics/slipknot/duality.html").read())
print l.author, " ", l.song
