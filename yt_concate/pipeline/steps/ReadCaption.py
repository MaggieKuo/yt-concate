import os

from yt_concate.pipeline.steps.Caption import Caption
from yt_concate.pipeline.steps.Step import Step, ProcessId
from yt_concate.settings import CAPTIONS_PATH, DOWNLOADS


class ReadCaption(Step):
    def process(self, d, inputs):
        # captions_file = os.path.join(DOWNLOADS, "captions_" + inputs[ProcessId.CHANNEL_ID] + ".txt")
        # if os.path.exists(captions_file):
        #     Caption.readCaptions(captions_file)
        #     return Caption.captions

        for caption_file in os.listdir(CAPTIONS_PATH):
            with open(os.path.join(CAPTIONS_PATH, caption_file), 'r') as f:
                hasTime = False
                for line in f:
                    d = line.strip()
                    if "-->" in d:
                        time = d
                        hasTime = True
                        continue
                    if hasTime:
                        # if d: captions[d] = time
                        if d: Caption(caption_file, time, d)
                        hasTime = False
            f.close()
        # with open(captions_file, 'w') as f:
        #     f.write(Caption.captionsToJson(Caption.captions))
        # f.close()
        return Caption.captions







