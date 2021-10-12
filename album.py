from song import Song

class Album:
    def __init__(self, title:str):
        self._title = title
        self._songs = []

    def addSongToAlbum(self, song:Song):
        self._songs.append(song)

    def getTotalLengthInSeconds(self) -> int:
        sumLength = 0
        for song in self._songs:
            sumLength = sumLength + song.getLengthInSeconds()
        return sumLength
