import requests

from src.api_methods import endpoints


def access_activity_data(access_token:str, params:dict=None) -> dict:
    headers:dict = {'Authorization': f'Authorization: Bearer {access_token}'}
    if not params:
        response:dict = requests.get(endpoints.activites_endpoint, headers=headers)
    response:dict = requests.get(endpoints.activites_endpoint, headers=headers, params=params)
    response.raise_for_status()
    activity_data = response.json()
    return activity_data

def access_athlete_data(access_token:str, params:dict=None) -> dict:
    headers:dict = {'Authorization': f'Authorization: Bearer {access_token}'}
    if not params:
        response:dict = requests.get(endpoints.athlete_endpoint, headers=headers)
    response:dict = requests.get(endpoints.athlete_endpoint, headers=headers, params=params)
    response.raise_for_status()
    athlete_data = response.json()
    return athlete_data

# def access_activity_splits(activity_id, access_token:str, params:dict=None) -> dict:
#     # Format the URL with the activity ID
#     url = endpoints.splits_endpoint.format(activity_id=activity_id)
#     headers:dict = {'Authorization': f'Authorization: Bearer {access_token}'}
#     if not params:
#         response:dict = requests.get(url, headers=headers)
#     response:dict = requests.get(url, headers=headers, params=params)
#     response.raise_for_status()
#     split_data = response.json()
#     return split_data