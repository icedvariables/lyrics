from bs4 import BeautifulSoup

class LyricPage:
    def __init__(self, data):
        parsed = BeautifulSoup(data)

        self.title = parsed.title.text

        author, song = self.title.split("-")
        self.author = author.lower().replace("lyrics", "").strip()
        self.song = song.strip()

        self.lyrics = parsed.find("div", {"class":"", "id":""}) # The div containing the actual lyrics is the only div with no class or id
