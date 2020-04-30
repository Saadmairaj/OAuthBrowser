import time
import subprocess
from OAuthBrowser.util import threaded
from urllib.parse import urlparse, parse_qs


class Wait:
    """
    Wait class for web brower.
    """

    def __init__(self, browser, pause_time=0.7):
        """Waits until an event occurs.

        Arguments:
            browser {[type]} -- give the browser class instance.

        Keyword Arguments:
            pause_time {float} -- time interval to check for event. (default: {0.7})
        """
        super().__init__()
        self.browser = browser
        self.pause_time = pause_time

    @threaded
    def until_url_netloc_changes(self):
        "Waits till netloc stays same."
        url = urlparse(self.browser.get_current_url())
        while url.netloc == urlparse(self.browser.get_current_url()).netloc:
            time.sleep(self.pause_time)

    @threaded
    def until_url_changes_times(self, count):
        "Waits till given number of times the url changes."
        url = urlparse(self.browser.get_current_url())
        while count > 0:
            if url != urlparse(self.browser.get_current_url()):
                url = urlparse(self.browser.get_current_url())
                count -= 1
            time.sleep(self.pause_time)

    @threaded
    def until_url_match(self, url):
        "Waits till given url matches with the current url."
        current_url = urlparse(self.browser.get_current_url())
        while urlparse(url) != current_url:
            time.sleep(self.pause_time)

    @threaded
    def until_timeout(self, seconds):
        "Waits for given seconds."
        time.sleep(seconds)

    @threaded
    def until_closed(self):
        "Waits until the window is closed."
        cmd = """on is_running(appName)
                    tell application "System Events" to (name of processes) contains appName
                end is_running
                set isRunning to is_running("%s")""" % (self.browser.browser)
        while True:
            p = subprocess.Popen(["osascript", "-"],
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stdin=subprocess.PIPE,
                                 universal_newlines=True, )
            stdout, stderr = p.communicate(cmd)
            if "false" in stdout:
                break
            time.sleep(self.pause_time)
        return stdout, stderr, p.returncode

    @threaded
    def until_inactive_timeout(self, seconds):
        "Waits on each url for given seconds till timer is 0. \
        If the url changes before timer goes 0 then timer will reset."
        timer = seconds
        current_url = urlparse(self.browser.get_current_url())
        while timer > 0:
            if current_url != urlparse(self.browser.get_current_url()):
                current_url = urlparse(self.browser.get_current_url())
                timer = seconds
            else:
                timer -= 1
            time.sleep(1)

    @threaded
    def until_present_query(self, item):
        "Waits till activation code page comes."
        while True:
            time.sleep(self.pause_time)
            cur_url = urlparse(self.browser.get_current_url())
            query = parse_qs(cur_url.query)
            if item in query.keys():
                break
