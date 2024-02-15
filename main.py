import os
import pandas as pd
import json
import requests

from tools.apiLib import ApiLib

api_lib = ApiLib()
token = api_lib.RequestToken()


response = api_lib.GetActivities(token)

res_df = pd.DataFrame(response.json())

