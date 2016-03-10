# -*- coding: utf-8 -*-



import urllib2 
import urllib
import json

key = "39c4e5aceb68dafb76cddbdfdecf5520"
#pernw tis suntetagmenes
x = input("Geografiko platos?: ")
y = input("geografiko mhkos?:")
#metatroph tou float number h int pou tha eiselthei stis suntetagmenes se string
x = str(x)
y = str(y)
#phgenw kai pernw ta data apo to site
url = str("http://api.openweathermap.org/data/2.5/weather?lat=" + x +"&lon="+ y + "&APPID=" + key + "")
#basikes metatropes ne json gia na parw ta dedomena
result = urllib2.urlopen(url)
content = result.read()
data = json.loads(content.decode('utf8'))
term = "rain"
print (data)
temp = data['main']['temp'] - 273
weathernow = data['weather'][0]['description']
print (data ['main']['temp'])
print (data['weather'][0]['description'])
#ta statment gia ths epiloges
if weathernow == term :
 print(" i am singing in the rain")
elif temp > 20 :
 print("nice")
elif temp < 5 :
 print("brrr")