# alexa.py
`alexa.py` is a simple, frills-free framework for Alexa Skills in Python. Starting to write [skills](https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Dalexa-skills&field-keywords=Dan.ms), I found that all the frameworks out there were either a) Written for nodejs or b) far too complex for my needs.

Just throw `alexa.py` in your project folder, import and instantiate it.

```
from alexa import alexa
al = alexa()
```

Then you can register the launch event (Alexa, open skill): `al.registerLaunch(lambda: functionname(argument))` and your intents `al.registerIntent("intentName", lambda: functionname(argument))`.
It's worth handling `AMAZON.CancelIntent`, `AMAZON.StopIntent` and `AMAZON.HelpIntent` if you intend to publish the skill.

Lastly, put `al.route(event)` in your handler function (if you're using Lambda it'll default to `lambda_handler`).

The response of registered functions should follow the format of `[response text, end session?]`. If a string is returned, the session will end after the response by default.

There's an example of what I just explained in `example.py`, any questions or issues drop me and email (or use the contact form on my site).