import os
import pandas as pd
import json
import requests

from tools.ApiLib import StravaApiLib

api_lib = StravaApiLib()
response = api_lib.GetActivities()
res_df = pd.DataFrame(response)
# google_api guide https://www.datacamp.com/tutorial/how-to-analyze-data-in-google-sheets-with-python-a-step-by-step-guide
