from yt_concate.pipeline.steps.Step import Step
from yt_concate.settings import DOWNLOADS, CAPTIONS_PATH, VIDEOS_PAHT
from yt_concate.Utils import Utils


class Preflight(Step):
    def process(self, data, inputs):
        print(Utils.createPath(DOWNLOADS))
        print(Utils.createPath(CAPTIONS_PATH))
        print(Utils.createPath(VIDEOS_PAHT))
