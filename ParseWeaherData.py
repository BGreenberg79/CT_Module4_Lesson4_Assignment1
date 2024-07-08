from WeatherDataFetcher import WeatherDataFetcher

class ParseWeatherData(WeatherDataFetcher):
    def __init__(self, search_city):
        super().__init__(search_city)

    def parse_data(self):
        if self.search_city not in self.weather_data.keys():
            return "Weather data not available"
        else:
            city = self.weather_data[self.search_city]["city"]
            temperature = self.weather_data[self.search_city]["temperature"]
            condition = self.weather_data[self.search_city]["condition"]
            humidity = self.weather_data[self.search_city]["humidity"]
            return f"Weather in {city}: {temperature} degrees\t{condition}\nHumidity: {humidity}%"

'''
The ParseWeatherData class does the heavy lifting for our program. It instatiates from it's parent class WeatherDataFetcher user the built in super method referencing both the WeatherDataFetcher object
it inherits and the search city it inherits. In the parse_data method if the search city is not in the list of outer keys from its inherited self.weather_data dictionary it returns a message that Weather data is not available.
In the else block we then assign variables for city, temperature, condition, and humidity by referencing the inherited dictionaries value locations using the syntax self.weather_data[self.search_city]["inner_key"]
Once those four variables have been assigned an f-string formats them in the print statement we return. This f-string will be inherited in our next class UserInterface that will print this message.
'''