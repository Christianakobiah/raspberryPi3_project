#from geopy.geocoders import Nominatim
#geolocator = Nominatim(user_agent="twitter")
#location = geolocator.geocode("175 5th Avenue NYC")
#print(location.address)
#print((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)
#print(location.raw)
#
#from geopy.geocoders import Nominatim
#geolocator = Nominatim(user_agent="instagram")
#location = geolocator.reverse("52.509669, 13.376294")
#print(location.address)
#print((location.latitude, location.longitude))
#(52.5094982, 13.3765983)
#print(location.raw)

from geopy.distance import great_circle
Ghana = (7.9465, -1.0232)
hungary = (47.1612, 19.5058)
print(great_circle(Ghana, hungary).miles)

