class alexa:
    def __init__(self):
        self.intents = {}
        self.launch = None

    def route(self, event):
        if event['request']['type'] == "LaunchRequest":
            if self.launch is None:
                raise Exception("No launch function set. Use alexa.registerLaunch(function)")
                
            return self.speak(self.launch()[0], endSession=False)
        
        chosenIntent = event['request']['intent']['name']
        if chosenIntent in self.intents:
            runIntent = self.intents[chosenIntent]()
            return self.speak(runIntent[0], endSession=runIntent[1])
        
    def registerIntent(self, intent, intentFunction):
        if not intent in self.intents:
            self.intents[intent] = intentFunction
            return True
        return False
    
    def registerLaunch(self, intentFunction):
        if self.launch is None:
            self.launch = intentFunction
            return True
        return False

    
    def speak(self, text, endSession=True):
        #Returns a speech to the Echo
        return {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': text,
                },
                'shouldEndSession': endSession
            }
        }