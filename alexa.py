class alexa:
    def __init__(self):
        self.intents = {}
        self.launch = None

    def route(event):
        if event['request']['type'] == "LaunchRequest":
            if launch is None:
                raise Exception("No launch function set. Use alexa.registerLaunch(function)")
                
            return speak(launch[0], endSession=False)
        
        chosenIntent = event['request']['intent']['name']
        if chosenIntent in intents:
            return speak(intents[chosenIntent][0], endSession=intents[chosenIntent][1])
        
    def registerIntent(intent, intentFunction):
        if not intent in intents:
            launch[intent] = intentFunction
            return True
        return False
    
    def registerLaunch(intentFunction):
        if not launch is None:
            launch = intentFunction
            return True
        return False

    
    def speak(text, endSession=True):
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