from yt_concate.pipeline.steps.Caption import Caption
from yt_concate.pipeline.steps.Step import Step, ProcessId


class SearchCaption(Step):
    def process(self, data, inputs):
        key = inputs[ProcessId.SEARCH_KEY]
        results = Caption.search(key, data)
        print(Caption.captionsToJson(results))
        return results
