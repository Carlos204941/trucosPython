from datetime import datetime

class EventLogger:
    _instance = None
    _event_logs = []

    def __new__(cls):
       if cls._instance is None:
          cls._instance = super(EventLogger, cls).__new__(cls)
       return cls._instance
    
    def log_event(self, event_message):
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")
        self._event_logs.append(f"{timestamp}: {event_message}")

    def display_logs(self):
         for log in self._event_logs:
               print(log)

logger = EventLogger()    
logger.log_event("Starting app.")
logger.log_event("Executing Task 1.")

logger2 = EventLogger()
logger2.log_event("Finish execution of Task 1.")
logger2.log_event("Ending app.")

logger3 = EventLogger()
logger3.display_logs()

