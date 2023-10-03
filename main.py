### Excutez la commande pip install phonenumbers opencage folium
import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumbers = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumbers, 'fr')
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'fr'))

from opencage.geocoder import OpenCageGeocode

# 1. Vous devez vous rendre sur le opencagedata.com
# 2. Créer votre compte ensuite copier le clé de l'api
# 3. Coler ça au niveau de key = ''
key = 'e7eac780bee44ebca58aacaf2cbc6d39'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(Location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("myLocation.html")


