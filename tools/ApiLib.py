import configparser
import requests

from datetime import datetime
from settings.config import StravaCredentials

config = configparser.ConfigParser()
config.read("settings/settings.txt")


class StravaApiLib:

    @staticmethod
    def RequestToken():

        payload = {
            'client_id': StravaCredentials.CLIENT_ID,
            'client_secret': StravaCredentials.CLIENT_SECRET,
            'refresh_token': StravaCredentials.REFRESH_TOKEN,
            'grant_type': StravaCredentials.GRANT_TYPE,
            'f': 'json'
        }
        print(" > Requesting Token...\n")
        res = requests.post(StravaCredentials.AUTH_URL, data=payload, verify=False)
        access_token = res.json()["access_token"]
        print("     > Access Token = {}\n".format(access_token))

        return access_token

    def GetActivities(self):

        token = self.RequestToken()

        page_not_empty = True
        header = {'Authorization': 'Bearer ' + token}
        param = {'per_page': 200, 'page': 1}
        if config["DATE"]["last_download_date"] != "":
            param["after"] = int(datetime.strptime(config["DATE"]["last_download_date"], "%Y-%m-%d").timestamp())

        data_l = []
        print(" > Starting download")
        while page_not_empty:
            response = requests.get(StravaCredentials.ACTIVITIES_URL, headers=header, params=param)

            if response.status_code == 200:

                if len(response.json()) > 0:
                    data_l += response.json()
                    param["page"] += 1

                else:
                    if param["page"] > 1:
                        print(f"""     > Downloaded {param['page'] - 1} pages stopping download and updating last
                              download date""")
                        config["DATE"]["last_download_date"] = datetime.now().strftime("%Y-%m-%d")
                        with open("settings/settings.txt", "w") as config_file:
                            config.write(config_file)
                        return data_l
                    if param["page"] == 1:
                        print("     > No new data")
                        return data_l

            else:
                print(f"     > API ERROR {response.status_code}")
                return []


class GoogleApiLib:
    a = ""
