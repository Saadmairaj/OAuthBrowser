"""
This module will let you authenticate OAuth 2.0 via system browser and get response URL. 
Currently supporting Google Chrome and Safari browsers. Built with applescript and osascript, 
only works on Mac OSX. A lot more can be done with OAuthBrowser like getting source code 
without getting automation detection from sites..

Read more about OAuthBrowser in detail on
https://github.com/Saadmairaj/OAuthBrowser/tree/master/OAuthBrowser.
"""

from OAuthBrowser.wait import Wait
from OAuthBrowser.util import threaded
from OAuthBrowser.browser import Safari, Chrome
