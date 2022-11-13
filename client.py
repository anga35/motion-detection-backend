import requests

url='http://127.0.0.1:8000/api/all-captures/'
file={'captured_frame':open("C:/Users/Dayod/OneDrive/Pictures/my_pic.jpg",'rb')}
response=requests.get(url)
print(response.json())