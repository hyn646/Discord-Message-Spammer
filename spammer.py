import requests

# Read content, authorization, channel URL, and count from files
with open('content.txt', 'r') as file:
    content = file.read().strip()

with open('authorization.txt', 'r') as file:
    authorization = file.read().strip()

with open('channel.txt', 'r') as file:
    channel_url = file.read().strip()

with open('count.txt', 'r') as file:
    count = int(file.read().strip())  # Convert the count to an integer

# Prepare the payload and headers
payload = {
    'content': content
}

headers = {
    'Authorization': authorization
}

# Send POST requests and print the message sent
for i in range(count):
    response = requests.post(channel_url, data=payload, headers=headers)
    print(f' (Hyn Spammer) Sent Message {i+1}')
