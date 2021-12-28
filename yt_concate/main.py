from yt_concate.pipeline.steps.DownloadCaption import DownloadCaption
from yt_concate.pipeline.steps.GetVideoList import GetVideoList, ProcessId
from pipeline.Pipeline import Pipeline

# CHANNEL_ID = "UCTqPBBnP2T57kmiPQ87986g"
# CHANNEL_ID = "UCEsXQiaKHZFXNhf9axB1m_w"
from yt_concate.pipeline.steps.Preflight import Preflight

CHANNEL_ID = "UCP7uiEZIqci43m22KDl0sNw"


def main():
    inputs = {
        ProcessId.CHANNEL_ID: CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaption()
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
