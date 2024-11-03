from abc import ABC, abstractmethod

class IState(ABC):
    @abstractmethod
    def handle(self, context):
        pass

class GreenState(IState):
    def handle(self, context):
        print("Green light - Go!")
        context.state = YellowState()

class YellowState(IState):
    def handle(self, context):
        print("Yellow light - Prepare to stop!")
        context.state = RedState()

class RedState(IState):
    def handle(self, context):
        print("Red light - Stop!")
        print("Waiting 90 secs")
        context.state = GreenState()

class StateContext:
    def __init__(self):
        self.state = GreenState()

    def request(self):
        self.state.handle(self)


context = StateContext()
for _ in range(10):
    context.request()