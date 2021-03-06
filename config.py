import googlemaps


class Config:
    def __init__(self):
        with open("app/keys.txt") as file:
            for line in file:
                api_type, key = line.split()
                api_type = api_type.lower()
                if api_type == "google":
                    self.google_key = key
                elif api_type == "storm_glass":
                    self.storm_glass_key = key
