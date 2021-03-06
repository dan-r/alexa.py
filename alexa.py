class alexa:
    def __init__(self):
        self.intents = {} # Stores which functions run for intents
        self.launch = None # Stores the LaunchRequest function (open skill)

    def route(self, event):
        # Catches launch request
        if event['request']['type'] == "LaunchRequest":
            if self.launch is None: # Raises an error if the function isnt set
                raise Exception("No launch function set. Use alexa.registerLaunch(function)")
                
            runLaunch = self.launch()
            if isinstance(runLaunch, list):
                return self.speak(runLaunch[0], endSession=False) # Endsession forced to False - as per Amazon Submission guidelines
            else:
                return self.speak(runLaunch, endSession=False)
        
        chosenIntent = event['request']['intent']['name'] # Gets the intent name
        if chosenIntent in self.intents: # If we know this intent
            runIntent = self.intents[chosenIntent]() # Run the intent
            
            if isinstance(runIntent, list): # If a list is given then endSession depending on the second parameter (index 1)
                return self.speak(runIntent[0], endSession=runIntent[1]) # Return the speech
            else: # If a string is returned, end the session after responding by default
                return self.speak(runIntent, endSession=True)
                
        else:
            return self.speak("Sorry, I didn't understand that", endSession=True) # If we dont know this intent
        
    def registerIntent(self, intent, intentFunction):
        if not intent in self.intents: # If this intent isnt already registered
            self.intents[intent] = intentFunction # Store function for this intent
            return True
        return False
    
    def registerLaunch(self, intentFunction):
        if self.launch is None: # If the launch intent hasnt been set
            self.launch = intentFunction
            return True
        return False

    
    def speak(self, text, endSession=True):
        # Returns a speech to the Echo
        return {
            'version': '1.0',
            'response': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': text,
                },
                'shouldEndSession': endSession # True = Session ends instantly, False = Alexa waits for another input
            }
        }