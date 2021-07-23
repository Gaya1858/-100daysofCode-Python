import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME="gayathri1858"
TOKEN ="ghthryhgyhsidsdj"
GRAPH_ID="laya2020"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url =pixela_endpoint,json=user_parameters)
# print(response.text)

graph_config ={
    "id":GRAPH_ID,
    "name":"coding",
    "unit":"minutes",
    "type": "int",
    "color":"ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url =graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
print(pixel_creation_endpoint)

dt =datetime.datetime.now()


pixel_data ={
    "date":dt.strftime("%Y%m%d"),
    "quantity":"50",
}
print(dt.strftime("%Y%m%d"))
# responce =requests.post(url =pixel_creation_endpoint,json=pixel_data,headers=headers)
# print(responce.text)
update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{dt.strftime('%Y%m%d')}"

new_pixel_data ={
    "quantity":"300"
}
print(update_endpoint)
response =requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)
print(response.text)