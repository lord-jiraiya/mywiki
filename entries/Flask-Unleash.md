# Flask-Unleash























* [Documentation](https://unleash.github.io/Flask-Unleash/)







* [Changelog](https://github.com/Unleash/Flask-Unleash/blob/master/docs/changelog.md)















## Pre-requisites















To try out Flask-Unleash, you'll need an instance of the [Unleash](http://github.com/unleash/unleash) server.  You can either use:







* Spin up a stack in Docker Compose using [unleash-docker](https://github.com/Unleash/unleash-docker)







* Check out the demo at [Unleash-Hosted](https://www.unleash-hosted.com/)















## Quickstart







Install Flask-Unleash using pip.















```python







pip install Flask-Unleash







```















Next, add Flask-Unleash to your code.



```Python

from flask import Flask



from flask_unleash import Unleash

app = Flask(__name__)

app.config["UNLEASH_URL"] = "http://localhost:4242/api"

app.config["UNLEASH_APP_NAME"] = "demoapp"



unleash = Unleash(app)

```

Now you can use the client to check feature flags

```Python

flag_value_1 = unleash.client.is_enabled("simple-feature")