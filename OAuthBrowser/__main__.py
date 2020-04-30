"Demonstration of OAuthBrowser"

from OAuthBrowser import *
from urllib.parse import urlparse, parse_qs

url = """https://accounts.google.com/signin/oauth/oauthchooseaccount?
scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fdrive.metadata.readonly&
state=state_parameter_passthrough_value&
redirect_uri=https%3A%2F%2Foauth2.example.com%2Fcode&
access_type=offline&
response_type=code&
client_id=583306224539-atbcaa8ne8g85e8kc006o6vmq99qiid0.apps.googleusercontent.com&
o2v=2&as=CDdm3G6Zd1UOG9o_gWXzQQ&flowName=GeneralOAuthFlow"""


def test(url):
    web = Safari(window_geometry=(100, 22, 400, 680))
    # opens new window of safari and directs to the url.
    web.open_new_window(url)
    # Wait class
    wait = Wait(web)
    # wait till query code is present in the url.
    wait.until_present_query("code")
    # fetchs the code from the url.
    code = parse_qs(urlparse(web.get_current_url()).query)
    # quits the browser.
    web.quit()
    return code.get('code')[0]


print("\nCode: %s\n" % test(url))
