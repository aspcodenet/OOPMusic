
class Album:
    def __init__(self, title:str):
        self._title = title
        self._songs = []

    def addSongToAlbum(self, song):
        self._songs.append(song)