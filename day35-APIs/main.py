'''
ISS location API
'''
import requests
#--------------------------------------------------------------------
# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response) ###<Response [200]>  response code
# #print(response.status_code) ## just 200
#
# if(response.status_code == 404):
#     raise Exception ("Resource doesn't exist")
#
# response.raise_for_status()
# data =response.json()["iss_position"]["longitude"]
# longitute =response.json()["iss_position"]["longitude"]
# latitude =response.json()["iss_position"]["latitude"]
# print(data)
#----------------------------------------------------------------------------

'''
APi parameters
https://api.sunrise-sunset.org/json.
'''
import datetime as dt
MY_LAT = 40.712776 # Your latitude
MY_LONG = -74.005974# Your longitude
parameters ={
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data =response.json()
sunrise =data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
time_now =dt.datetime.now()
print(time_now)