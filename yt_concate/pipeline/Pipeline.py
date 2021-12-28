# from .steps.step import Step, StepException
from yt_concate.pipeline.steps.Step import Step, StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
                print(data)
            except StepException as e:
                print("Exception ", e)
                break
