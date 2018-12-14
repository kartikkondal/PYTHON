class Flight:
    def __init__(self,engine):
        self.engine = engine

    def StartEngine(self):
        self.engine.start()

class AirbusEngine:

    def start(self):
        print("Airbus Engine starting ")

class BoingEngine:

    def start(self):
        print("Boing Engine starting ")


AirbusEngine1 = AirbusEngine()
Flight1 = Flight(AirbusEngine1)
Flight1.StartEngine()
