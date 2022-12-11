import eel
import pyowm

owm = pyowm.OWM("5acb6fedb8ae72398660679b82f41f8a")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    
    observation = mgr.weather_at_place(city)
    w = observation.weather
    
    temp = w.temperature('celsius')['temp']

    return "B городе - " + city + " сейчас "  + str(temp) + " градусов!"

eel.init("web")
eel.start("main.html", size=(700, 700))

