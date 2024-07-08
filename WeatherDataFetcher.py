class WeatherDataFetcher:

    def __init__(self, search_city):
        self.search_city = search_city
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def fetch_weather_data(self):
        if self.search_city in self.weather_data.keys():
            print(f"Fetching weather data for {self.search_city}...")
        return self.weather_data.get(self.search_city)

'''
When refactoring the original code, the first class I built was WeatherDataFetcher. When instantiating the class I knew the only necessary instance variable would be the city our function searhes for.
I also decided that this would be where we would house our sample data in dictionary format as our next metho would need to reference it using the built in .get() method
In the fetch_weather_data method if the search city is in our nested library we print a message saying that we are fetching the data and return the outer value (the nested dictionary) through the built in .get() method. 
This return is then used in the ParseWeatherData class
'''