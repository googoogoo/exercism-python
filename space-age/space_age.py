class SpaceAge:

    def __init__(self, seconds) -> None:
        self.seconds = seconds

    secs_in_year = 31557600

    orbits = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def on_earth(self):
        return round(self.seconds / self.secs_in_year, 2)

    def on_earth_not_rounded(self):
        return self.seconds / self.secs_in_year

    def on_mercury(self):
        return round(self.on_earth_not_rounded()/ self.orbits["mercury"], 2)

    def on_venus(self):
        return round(self.on_earth_not_rounded()/ self.orbits["venus"], 2)

    def on_mars(self):
        return round(self.on_earth_not_rounded()/ self.orbits["mars"], 2)

    def on_jupiter(self):
        return round(self.on_earth_not_rounded()/ self.orbits["jupiter"], 2)

    def on_saturn(self):
        return round(self.on_earth_not_rounded()/ self.orbits["saturn"], 2)

    def on_uranus(self):
        return round(self.on_earth_not_rounded()/ self.orbits["uranus"], 2)

    def on_neptune(self):
        return round(self.on_earth_not_rounded()/ self.orbits["neptune"], 2)