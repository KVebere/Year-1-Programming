class Songs:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        output = f"Song({self.title}, {self.artist}, {self.duration})"
        return output
    
    def getDuration(self):
        return self.duration
    
    def getTitle(self):
        return self.title
    
    def getArtist(self):
        return self.artist
    
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def addSong(self, song):
        self.songs.append(song)
    
    def removeSong(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print("Song not in playlist!")
    
    def __str__(self):
        output = f"Playlist {self.name} with songs:\n"
        for song in self.songs:
            output += f"{song}\n"
        return output

class Spotify:
    def __init__(self):
        self.playlists = []
        self.mainPlaylists()
    
    def mainPlaylists(self):
        song1 = Songs("Bohemian Rhapsody", "Queen", 6.03)
        song2 = Songs("Stairway to Heaven", "Led Zeppelin", 8.02)
        song3 = Songs("Hotel California", "Eagles", 6.30)

        playlist1 = Playlist("Rock")
        playlist2 = Playlist("Pop")

        playlist1.addSong(song1)
        playlist1.addSong(song2)
        playlist2.addSong(song3)

        self.playlists.append(playlist1)
        self.playlists.append(playlist2)

    def addPlaylist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)

    def displayPlaylists(self):
        for playlist in self.playlists:
            print(playlist)
    
    def addSongToPlaylist(self, song, playlist):
        for p in self.playlists:
            if p.name == playlist:
                p.addSong(song)
                return
        print("Playlist not found!")
    
    def removeSongFromPlaylist(self, song, playlist):
        for p in self.playlists:
            if p.name == playlist:
                p.removeSong(song)
                return
        print("Playlist not found!")
    
def testSongs():
    song1 = Songs("Bohemian Rhapsody", "Queen", 6.03)
    song2 = Songs("Stairway to Heaven", "Led Zeppelin", 8.02)
    song3 = Songs("Hotel California", "Eagles", 6.30)
    print(song1)
    print(song2)
    print(song3)
    print(song1.getDuration())
    print(song2.getTitle())
    print(song3.getArtist())
#testSongs()
    
def testPlaylist():
    playlist = Playlist()
    song1 = Songs("Bohemian Rhapsody", "Queen", 6.03)
    song2 = Songs("Stairway to Heaven", "Led Zeppelin", 8.02)
    song3 = Songs("Hotel California", "Eagles", 6.30)
    playlist.addSong(song1)
    playlist.addSong(song2)
    playlist.addSong(song3)
    print(playlist)
    playlist.removeSong(song2)
    print(playlist)
#testPlaylist()
    
def testSpotify():
    spotify = Spotify()
    spotify.displayPlaylists()
    song4 = Songs("Yesterday", "The Beatles", 2.05)
    spotify.addSongToPlaylist(song4, "Rock")
    spotify.displayPlaylists()
    spotify.removeSongFromPlaylist(song4, "Rock")
    spotify.displayPlaylists()
    spotify.addPlaylist("Jazz")
    spotify.displayPlaylists()
testSpotify()

