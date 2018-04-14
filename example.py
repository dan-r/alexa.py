from alexa import alexa
al = alexa() # Instantiate the module

def hello(text):
    return [text, True] # [speech response, end session?]
    
def lambda_handler(event, context):
    al.registerLaunch(lambda: hello("Welcome to Test Skill!"))
    al.registerIntent("testIntent", lambda: hello("testIntent running"))
    
    return al.route(event)
    
launchrequest = {'request':{'type':'LaunchRequest'}}
intentrequest = {'request':{'type':'IntentRequest', 'intent':{'name':'testIntent'}}}
print(lambda_handler(launchrequest, None))
print(lambda_handler(intentrequest, None))