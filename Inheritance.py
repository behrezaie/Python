#!/usr/bin/env python3

class Song:
    def __init__(self, **kwargs):
        if 'style' in kwargs: self._style = kwargs['style']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'composer' in kwargs: self._composer = kwargs['composer']
        if 'instruments' in kwargs: self._instruments = kwargs['instruments']
        if 'duration' in kwargs: self._duration = kwargs['duration']
        
    def style(self, s = None):
        if s: self._style = s
        try: return self._style
        except AttributeError: return None
    
    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None
        
    def composer(self, c = None):
        if c: self._composer = c
        try: return self._composer
        except AttributeError: return None
        
    def instruments(self, i = None):
        if i: self._instruments = i
        try: return self._instruments
        except AttributeError: return None
        
    def duration(self, d = None):
        if d: self._duration = d
        try: return self._duration
        except AttributeError: return None

    def __str__(self):
        return "{:<20} | By {:<20} | Duration: {:<5} | Instrument(s): {:<20} | Style: {:<10}".format(self.name(), self.composer(), self.duration(), self.instruments(), self.style())
    
    
    
class Jazz(Song):
    def __init__(self, **kwargs):
        self._style = 'Jazz'
        if 'style' in kwargs: del kwargs['style']
        super().__init__(**kwargs)
        
    def __str__(self):
        return "{:<20} | By {:<20} | Duration: {:<5} | Instrument(s): {:<20} | Style: ***{}***".format(self.name(), self.composer(), self.duration(), self.instruments(), self.style())
        
        
        
def main():
    song1 = Song(style = 'Pop', name = 'The Rain Must Fall', composer = 'Yanni', duration = '7m26s', instruments = 'Piano-Violin')
    song2 = Jazz(name = 'Crave', composer = 'Jelly Roll Morton', duration = '3m45s', instruments = 'Piano')
    song3 = Jazz(name = 'My Funny Valentine', composer = 'Richard Rodgers', duration = '3m2s', instruments = 'Piano')
    print(song1)
    print(song2)
    print(song3)
    
if __name__ == '__main__': main()