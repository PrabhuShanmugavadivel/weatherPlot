from matplotlib import pyplot as plt 
from lib.weather import weather
from pprint import pprint
import pandas as pd
import json

#yahoo URL
url = "https://weather-ydn-yql.media.yahoo.com/forecastrss"

#creating object
app = weather(url)

def get_weather(location):
    #getting temperature, humidity and forecast details
    weatherHash = {}
    forecast = app.get_forcastrss(location)
    # pprint(forecast)
    for key, value in forecast['current_observation']['atmosphere'].items():
        if 'humidity' in key:
            weatherHash['humidity'] = value
    for key, value in forecast['current_observation']['condition'].items():
        if 'temperature' in key:
            weatherHash['temperature'] = value

    day = [ sub['day'] for sub in forecast['forecasts'] ]
    high = [ sub['high'] for sub in forecast['forecasts'] ]
    low = [ sub['low'] for sub in forecast['forecasts'] ]

    #dumping into pandas dataframe
    df1 = pd.DataFrame(list(zip(day, high, low)), columns = ['day', 'high', 'low'])
    df2 = pd.DataFrame(weatherHash, index = [0])
    report = df1.join(df2)
    report.sort_values(by='day')
    # print(report)
    
    #using matplotlib to plot graph
    plt.title("Temperature anomalies")
    plt.xlabel("no. of days")
    plt.ylabel("Temperature in Fahrenhiet")
    ax = plt.gca()
    report.plot(kind = 'line', x = 'day', y = 'high', ax = ax)
    report.plot(kind = 'line', x = 'day', y = 'low', color = 'red', ax = ax)
    report.plot(kind = 'bar', x = 'day', y = 'humidity', color = 'green', ax = ax)
    report.plot(kind = 'bar', x = 'day', y = 'temperature', color = 'red', ax = ax)
    plt.show()
    
if __name__ == "__main__":
    get_weather(input("Specify Locaion:"))

    
