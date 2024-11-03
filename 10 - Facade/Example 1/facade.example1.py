class DvdPlayer:
    def on(self):
        print("DVD Player turned on")

    def play_movie(self, movie):
        print(f"Playing movie '{movie}'")

    def off(self):
        print("DVD Player turned off")

class Projector:
    def on(self):
        print("Projector turned on")

    def off(self):
        print("Projector turned off")

class Speakers:
    def on(self):
        print("Speakers turned on")
    
    def off(self):
        print("Speakers turned off")


class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, speakers):    
        self.dvd_player = dvd_player
        self.projector = projector
        self.speakers = speakers

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.projector.on()
        self.speakers.on()
        self.dvd_player.on()
        self.dvd_player.play_movie(movie)
    
    def end_movie(self):
        print("Shutting movie theater down...")
        self.projector.off()
        self.speakers.off()
        self.dvd_player.off()

dvd_player = DvdPlayer()
projector = Projector()
speakers = Speakers()

home_theater = HomeTheaterFacade(dvd_player, projector, speakers)
home_theater.watch_movie("Inception")

print("Wait two hours")

home_theater.end_movie()