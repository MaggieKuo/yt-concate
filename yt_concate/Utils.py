import os

from yt_concate.settings import DOWNLOADS, CAPTIONS_PATH, VIDEOS_PAHT


class Utils:
    @staticmethod
    def getVedioIdByUrl(yt_url):
        return yt_url.replace("https://www.youtube.com/watch?v=", "")

    @staticmethod
    def getFileName(yt_url, path_name):
        return os.path.join(path_name, f'{Utils.getVedioIdByUrl(yt_url)}.txt')

    @staticmethod
    def createPath(path_name):
        if not os.path.exists(path_name):
            os.makedirs(path_name, exist_ok=True)
        return os.path.exists(path_name)

