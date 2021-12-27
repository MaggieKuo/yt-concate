import urllib.request
import json

from yt_concate.pipeline.steps.step import Step, ProcessId
from yt_concate.settings import GOOGLE_API_KEY


class GetVideoList():
    def process(self, data, inputs):
        channel_id = inputs[ProcessId.CHANNEL_ID]
        api_key = GOOGLE_API_KEY

        headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 '
                                 'Firefox/95.0'}
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                           channel_id)
        print(first_url)

        video_links = []
        url = first_url
        while True:
            # try:
            req = urllib.request.Request(url=url, headers=headers)
            inp = urllib.request.urlopen(req)
            resp = json.load(inp)
            # except KeyError:
            #     raise StepException

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])
            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        return video_links
