from yt_concate.pipeline.steps.get_video_list import GetVideoList, ProcessId
from pipeline.pipeline import Pipeline

CHANNEL_ID = "UCTqPBBnP2T57kmiPQ87986g"


def main():
    inputs = {
        ProcessId.CHANNEL_ID: CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]
    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
