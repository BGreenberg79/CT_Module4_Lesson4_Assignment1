from ParseWeaherData import ParseWeatherData

class UserInterface(ParseWeatherData):
    def __init__(self, search_city):
        super().__init__(search_city)

    def display_forecast(self):
        print(ParseWeatherData(self.search_city).parse_data())

'''
UserInterface inherits ParseWeatherData and instantiates using the super keyword. It's only method is display_forecast which prints the f-string that ParseWeatherData's parse_data method produces for each search city we run through it.
'''