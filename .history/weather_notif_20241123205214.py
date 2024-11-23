import requests
from bs4 import BeautifulSoup
#from win10toast import ToastNotifier
from winotify import Notification


#n = ToastNotifier()

test = Notification(
    app_id="WEATHER",
    title="TITLE"
)


def getdata(url):

    r = requests.get(url)

    return r.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

soup = BeautifulSoup(htmldata, 'html.parser')

#print(soup.prettify())

current_temp = soup.find_all("span", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--zUBSz")
print(current_temp)
chance_rain = soup.find_all("div", class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))
temp_rain = str(chance_rain)

result = "current_temp " + temp[128:-9] + " in casablanca maarif" + "\n" +temp_rain[131:-14]

#print(temp)

test.msg = result
test.show()