import requests
import os

from tools.config import Credentials

class ApiLib:

    def RequestToken(self):
        payload = {
            'client_id': Credentials.CLIENT_ID,
            'client_secret': Credentials.CLIENT_SECRET,
            'refresh_token': Credentials.REFRESH_TOKEN,
            'grant_type': Credentials.GRANT_TYPE,
            'f': 'json'
        }
        print("Requesting Token...\n")
        res = requests.post(Credentials.AUTH_URL, data=payload, verify=False)
        access_token = res.json()["access_token"]
        print("Access Token = {}\n".format(access_token))

        return access_token

    def GetActivities(self, token):
        header = {'Authorization': 'Bearer ' + token}
        param = {'per_page': 200, 'page': 1}
        response = requests.get(Credentials.ACTIVITIES_URL, headers=header, params=param)
        return response