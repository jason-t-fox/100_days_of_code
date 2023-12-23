import requests
import datetime

# create pixela user
user_endpoint = "https://pixe.la/v1/users"
username = "username"
token = "token"
headers = {"X-USER-TOKEN": token}
graphid = "testgraph1"
today = datetime.date.today().strftime("%Y%m%d")

create_user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
    }
#
# create_user_response = requests.post(url=create_user_endpoint, json=create_user_params)
# # print(create_user_response.text)

graph_endpoint = f"{user_endpoint}/{username}/graphs"

graph_params = {
    "id": graphid,
    "name": "testdata1",
    "unit": "miles",
    "type": "float",
    "color": "sora"
}

# create_graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(create_graph_response.text)

create_dot_endpoint = f"{user_endpoint}/{username}/graphs/{graphid}"

create_dot_params = {
    "date": today,
    "quantity": "5"
}

# create_dot = requests.post(url=create_dot_endpoint, json=create_dot_params, headers=headers)
# print(create_dot.text)

delete_graph = requests.delete(url=create_dot_endpoint, headers=headers)
print(delete_graph.text)

