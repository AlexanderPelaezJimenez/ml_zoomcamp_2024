import requests

url = "http://localhost:9696/predict"
client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()

print('Client:', client)
print('Subscription probability:', response['subscription_probability'])