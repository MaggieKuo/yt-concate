import json
from collections import namedtuple


class Caption:
    captions = []

    def __init__(self, ytId, time, caption):
        self.yt_id = ytId
        self.yt_time = time
        self.yt_caption = caption
        Caption.captions.append(self)

    @staticmethod
    def captionsToJson(captions):
        # return json.dumps(captions)
        return json.dumps(captions, default=lambda x: x.__dict__)

    @staticmethod
    def search(str, captions):
        return [caption for caption in captions if str in caption.yt_caption]

    @classmethod
    def readCaptions(cls, caption_file):
        with open(caption_file, 'r') as f:
            Caption.captions = json.loads(f.read(), object_hook=lambda d: namedtuple('Caption', d.keys())(*d.values()))
        f.close()
