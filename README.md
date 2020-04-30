# OAuthBrowser

This module will let you authenticate [OAuth 2.0](https://oauth.net/2/) via system browser and get response URL. Currently supporting **Google Chrome** and **Safari** browsers. Built with *applescript* and [*osascript*](https://ss64.com/osx/osascript.html), only works on Mac OSX. 

A lot more can be done with **OAuthBrowser** like getting source code without getting automation detection from websites.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [OAuthBrowser](https://pypi.org/project/OAuthBrowser/).

```bash
pip install OAuthBrowser
```

Or install the latest repo from here.

```bash
pip install git+https://github.com/Saadmairaj/OAuthBrowser#egg=OAuthBrowser
```

## Usage

Usage is very simple

1. Pass authentication URL.
2. Apply `Wait` class to wait for the browser to redirect.
3. Fetch URL.
4. Close browser.

```python
from OAuthBrowser import Safari, Wait
from urllib.parse import urlparse, parse_qs

URL = """https://accounts.google.com/signin/oauth/oauthchooseaccount?
scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.metadata.readonly&
state=state_parameter_passthrough_value&
redirect_uri=https%3A%2F%2Foauth2.example.com%2Fcode&
access_type=offline&
response_type=code&
client_id=583306224539-atbcaa8ne8g85e8kc006o6vmq99qiid0.apps.googleusercontent.com&
o2v=2&as=CDdm3G6Zd1UOG9o_gWXzQQ&flowName=GeneralOAuthFlow"""

# Initialise browser
browser = Safari(window_geometry=(100, 22, 400, 690))
# Pass Authentication URL
browser.open_new_window(URL)
# Initialise Wait
wait = Wait(browser)
# Wait till query "code" is present in the URL.
wait.until_present_query('code')
# Fetch the url
response_url = urlparse(browser.get_current_url())
code = parse_qs(response_url.query).get('code')[0]
print("\nCode: %s\n" % code)
# Close the browser
browser.quit()
```

## Demonstration

```bash
python -m OAuthBrowser
```

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method of this repository before making a change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/Saadmairaj/OAuthBrowser/blob/master/LICENSE.txt)