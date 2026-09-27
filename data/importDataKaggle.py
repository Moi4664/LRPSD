import kaggle
from dotenv import load_dotenv
import os

load_dotenv()

KAGGLE_API_TOKEN = os.getenv("KAGGLE_API_TOKEN")

if(not KAGGLE_API_TOKEN):
    raise ValueError("The kaggle api token was not found please go to : https://www.kaggle.com/docs/api#authentication")

dataset = "samartalwar/sleep-debt-and-screen-time-late-night-phone-habits"


kaggle.api.dataset_download_files(
    dataset=dataset,
    path="data",
    unzip=True
)

