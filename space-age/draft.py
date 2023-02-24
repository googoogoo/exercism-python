class SpaceAge:

    orbits = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 29.447498,
        "neptune": 29.447498
    }

    secs_in_year = 31557600

    def __init__(self, seconds) -> None:
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / secs_in_year, 2)

    def on_earth_not_rounded(self):
        return self.seconds / secs_in_year

    def on_mercury(self):
        return round(self.on_earth_not_rounded()/ 0.2408467, 2)

    def on_venus(self):
        return round(self.on_earth_not_rounded()/ 0.61519726, 2)

    def on_mars(self):
        return round(self.on_earth_not_rounded()/ 1.8808158, 2)

    def on_jupiter(self):
        return round(self.on_earth_not_rounded()/ 11.862615, 2)

    def on_saturn(self):
        return round(self.on_earth_not_rounded()/ 29.447498, 2)

    def on_uranus(self):
        return round(self.on_earth_not_rounded()/ 84.016846, 2)

    def on_neptune(self):
        return round(self.on_earth_not_rounded()/ 164.79132)
