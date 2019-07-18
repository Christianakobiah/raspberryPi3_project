import pyowm
 
owm = pyowm.OWM('b9a9f811fca03685c33f46a1390d4597')
observation = owm.weather_at_place('Ghana,kumasi')
w = observation.get_weather()
 
print(w.get_wind()['speed'])
print(w.get_humidity())
print(w.get_temperature()['temp_min'])

#a = w.get_temperature()
#print(a)
#
#print(a['temp_min'])
