import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

DOWNLOADS = "downloads"
VIDEOS_PAHT = os.path.join(DOWNLOADS, "videos")
CAPTIONS_PATH = os.path.join(DOWNLOADS, "captions")
