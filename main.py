from WeatherDataFetcher import WeatherDataFetcher
from ParseWeaherData import ParseWeatherData
from UserInterface import UserInterface

def main():
    while True:
        search_city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if search_city.lower() == 'exit':
            break
        else:
            WeatherDataFetcher(search_city).fetch_weather_data()
            ParseWeatherData(search_city).parse_data()
            UserInterface(search_city).display_forecast()
            print("\n")

main()

'''
Our refactored code is way more modular by making ParseWeatherData and WeatherDataFetcher there own classes instead of the unctions they originally were. 
I also created the class UserInterface that combines get_deatiled_forecast and display_weather functions which were redundant and both printed the results of the parse_weather_data function if data was available.
I first import all three classes from their modules as each will be called in our main menu while loop. Then I define the function that houses our while loop. In it I take the user input for search_city and if the user returns "exit
we break the loop. Otherwise I instantiate an object for weather data fetcher using the user's search city and call the fetch_weather_data method. I then instantiate a ParseWeatherData object with the same input and call the parse_data method.
Finally I instantiate a UserInterface object with the same search_city and call the display_forecast method. I then print one empty line break to make the terminal easier for the user to read.

The only thing I may have changed additionally is I may have eliminated the UserInterface class and wrapped ParseWeatherData's parse_data method in a print statement for both it's if and else statements. I ultimately decided against this as I was aleady combining two functions
into one to make this class and did not want to deviate from the assignment's instructions so much. If I were to have built this code from scratch or weren't trying t satisfy the assignment's requirements I would have probably only ran this program using my first two classes to refactor
it further and make the code even more efficient.
'''