from abc import ABC, abstractmethod

class ICommunication(ABC):
    @abstractmethod
    def ask(self, question: str) -> str:
        pass

    @abstractmethod
    def reply(self, answer: str) -> str:
        pass

class EnglishSpeaker(ICommunication):    
    def ask(self, question: str) -> str:
        return f"Question in English: {question}"

    def reply(self, answer: str) -> str:
        return f"Answer in English: {answer}"
    
class SpanishSpeaker:
    def pregunta(self, question: str) -> str:    
        return f"Pregunta en español: {question}"
    
    def respuesta(self, answer: str) -> str:
        return f"Respuesta en español: {answer}"
    
class Translator(ICommunication):
    def __init__(self, spanish_speaker: SpanishSpeaker):
        self._spanish_speaker = spanish_speaker

    def ask(self, question: str) -> str:
        return self._spanish_speaker.pregunta(question)

    def reply(self, answer: str) -> str:
        return self._spanish_speaker.respuesta(answer)
    
class CommunicationSystem:
        def start_conversation(self, communicator: ICommunication, question: str, answer: str):
            print(communicator.ask(question))
            print(communicator.reply(answer))

communication_system = CommunicationSystem() 
english_speaker = EnglishSpeaker()
communication_system.start_conversation(english_speaker, "How are you?", "I'm fine, thank you! ")           


spanish_speaker = SpanishSpeaker()
translator = Translator(spanish_speaker)
communication_system.start_conversation(translator, "¿Cómo estás?", "¡Estoy bien, gracias!")    