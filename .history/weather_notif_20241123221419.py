import asyncio
import warnings
import requests
from bs4 import BeautifulSoup
#from win10toast import ToastNotifier
from winotify import Notification
import telegram 


#n = ToastNotifier()

test = Notification(
    app_id="WEATHER",
    title="TITLE"
)

url = "https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/"

def get_weather_data(url):
    try:
       response = requests.get(url)
       response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching weather data: {e}"

#htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

    soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

    try:
        temp = soup.find("span", class_="CurrentConditions--tempValue--zUBSz")
        rain = soup.find("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
        temperature = temp.text if temp else "N/A"
        rain_chance = rain.text if rain else "N/A"
        return f"Current temperature: {temperature} in Casablanca Maarif\nChance of rain: {rain_chance}"
    except Exception as e:
        return f"Error parsing weather data: {e}"

def show_notification(title, message):
    notification = Notification(
        app_id="Weather App",
        title=title,
        msg=message,
        duration="long"
    )
    notification.show()

bot = telegram.Bot(token="7809941331:AAG0TluAsqqUda5sdx7e6PtbIlDsiIIpFuQ")

#def send_telegram_msg(id, msg):
    
#   bot.send_message(chat_id=id, text=msg)


# Main program
if __name__ == "__main__":
    weather_url = "https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google"
    weather_info = get_weather_data(weather_url)
    show_notification("Weather Update", weather_info)
    asyncio.run(bot.send_message(chat_id="1001186564", text="hello"))










"""
current_temp = soup.find("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--zUBSz")
print(current_temp)
chance_rain = soup.find_("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))
temp_rain = str(chance_rain)

result = "current_temp " + temp[128:-9] + " in casablanca maarif" + "\n" +temp_rain[131:-14]

#print(temp)
"""
