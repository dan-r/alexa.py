# alexa.py
`alexa.py` is a simple, frills-free framework for Alexa Skills in Python. Starting to write [skills](https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Dalexa-skills&field-keywords=Dan.ms), I found that all the frameworks out there were either a) Written for nodejs or b) far too complex for my needs.

Just throw `alexa.py` in your project folder, import and instantiate it.

```
from alexa import alexa
al = alexa()
```

Then you can register the launch event (Alexa, open skill): `al.registerLaunch(lambda: functionname(argument))` and your custom intents `al.registerIntent("intentName", lambda: functionname(argument))`.

Lastly, put `al.route(event)` in your handler function (if you're using Lambda it'll default to `lambda_handler`).