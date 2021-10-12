from song import Song
from album import Album

al = Album("Thriller")

song1 = Song("Billie Jean", 129 )
al.addSongToAlbum(song1)

song2 = Song("Beat it", 55 )
al.addSongToAlbum(song2)

print(song1.getLengthInSeconds())
#### a b c e f 
letter = "t"

if song1.doesStartOnLetter(letter):
    print(song1.getTitle())    