from alexa import alexa
al = alexa() # Instantiate the module

def hello(text):
    return [text, True] # [speech response, end session?]


al.registerLaunch(lambda: hello("Welcome to Test Skill!"))
al.registerIntent("testIntent", lambda: hello("testIntent running"))

def lambda_handler(event, context):
    return al.route(event)
    


###### Simulations below, stop here for production use ######

# Simulates a launch request (Alexa, open Skill)
launchrequest = {'request':{'type':'LaunchRequest'}}
print(lambda_handler(launchrequest, None))

# Simulates an intent request (Alexa, ask Skill for testIntent)
intentrequest = {'request':{'type':'IntentRequest', 'intent':{'name':'testIntent'}}}
print(lambda_handler(intentrequest, None))