import os.path

from pytube import YouTube

from yt_concate.Utils import Utils
from yt_concate.pipeline.steps.Step import Step
from yt_concate.settings import CAPTIONS_PATH


class DownloadCaption(Step):
    def process(self, data, inputs):
        for url in data:
            file_path = Utils.getFileName(url, CAPTIONS_PATH)
            if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                continue

            yt = YouTube(url)
            print(yt.captions)
            try:
                caption = yt.captions['a.en']
            except KeyError:
                try:
                    caption = yt.captions['en-US']
                except KeyError:
                    try:
                        caption = yt.captions['en']
                    except:
                        continue

            # print(caption.url)
            srt = caption.generate_srt_captions()
            text_file = open(file_path, "w", encoding='utf-8')
            text_file.write(srt)
            text_file.close()


