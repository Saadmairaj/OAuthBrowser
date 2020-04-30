import subprocess


class Browser_wrapper:
    """Only for OSX.

    ### Args:
        1. window_geometry = (x, y, w, h)"""

    def __init__(self, **options):
        super().__init__()
        browser = options['browser']
        self._options = options
        self._cmd_to_open = """-e 'tell app "%s" to open location "{url}"'""" % (
            browser)
        self._cmd_to_open_new = """-e 'tell app "%s" to make new document with properties {{URL:"{url}"}}'""" % (
            browser)
        self._cmd_to_resize = """-e 'tell app "%s" to set bounds of window 1 to {{{x},{y},{w},{h}}}'""" % (
            browser)
        self._cmd_to_close = """-e 'tell app "%s" to close current tab of front window'""" % (
            browser)
        self._cmd_to_close_window = """-e 'tell app "%s" to close front window'""" % (
            browser)
        self._cmd_to_quit = """-e 'tell app "%s" to close every tab of front window'""" % (
            browser)
        self._cmd_force_quit = """-e 'tell app "%s" to quit front window'""" % (
            browser)
        self._cmd_get_active_urls = """-e 'tell app "%s" to get the URL of every tab of every window'""" % (
            browser)
        self._cmd_get_current_url = """-e 'tell app "%s" to get the URL of current tab of window 1'""" % (
            browser)
        self._cmd_to_activate = """-e 'tell app "%s" to activate'""" % (
            browser)
        self._cmd_get_bounds = """-e 'tell app "%s" to get bounds of front window'""" % (
            browser)
        self._cmd_get_source = ""

    def get_window_bounds(self):
        "Returns bounds of the current window."
        cmd = "osascript {}".format(self._cmd_get_bounds)
        return self._run_command(cmd).stdout

    def get_all_urls(self):
        "Returns the list of all the active urls."
        cmd = "osascript {}".format(self._cmd_get_active_urls)
        out = self._run_command().stdout
        if str(out).endswith('\n'):
            out = out[:-2]
        return out.split(', ')

    def get_current_url(self):
        "Returns current active url."
        cmd = "osascript {}".format(self._cmd_get_current_url)
        out = self._run_command(cmd).stdout
        return out.split()[0]

    def open_new_window(self, url):
        "Opens browser in a new window if one already exists and gets the given url."
        x, y, w, h = self._set_window_size()
        cmd = "osascript {} {} {}".format(
            self._cmd_to_open_new.format(url=url),
            self._cmd_to_resize.format(x=x, y=y, w=w, h=h),
            self._cmd_to_activate)
        try:
            return self._run_command(cmd)
        except subprocess.CalledProcessError:
            return self.open(url)

    def open(self, url):
        "Opens browser and get the given url."
        cmd = "osascript {} {}".format(
            self._cmd_to_open.format(url=url),
            self._cmd_to_activate)
        return self._run_command(cmd)

    def quit(self):
        "Quits the current active window."
        cmd = "osascript {}".format(self._cmd_to_quit)
        return self._run_command(cmd)

    def force_quit(self):
        "Quits the application. (All windows and tabs)"
        cmd = "osascript {}".format(self._cmd_force_quit)
        return self._run_command(cmd)

    def close_current_tab(self):
        "Close the current active tab."
        cmd = "osascript {}".format(self._cmd_to_close)
        return self._run_command(cmd)

    def get_source_code(self):
        "Fetches source code the current tab of current window."
        source_code = self._run_command_Popen(
            self._cmd_get_source, ['osascript', '-'])
        return source_code[0]

    def _set_window_size(self):
        "Internal funtion."
        x, y, w, h = self._options.get('window_geometry', (0, 0, 700, 900))
        w += x
        h += y
        return x, y, w, h

    def _run_command(self, cmd):
        "Internal function."
        return subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='UTF-8',
            universal_newlines=True)

    def _run_command_Popen(self, cmd, args):
        "Internal function."
        p = subprocess.Popen(args,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             universal_newlines=True,
                             shell=True)
        stdout, stderr = p.communicate(cmd)
        return stdout, stderr, p.returncode


class Chrome(Browser_wrapper):
    browser = "Google Chrome"

    def __init__(self, **options):
        options['browser'] = self.browser
        super().__init__(**options)
        self._cmd_get_current_url = """-e 'tell app "Google Chrome" to get URL of active tab of front window'"""
        self._cmd_get_source = """
                tell application "Google Chrome"
                    delay 2
                    set source to execute front window's active tab javascript "document.documentElement.outerHTML"
                end tell
                """
        self._cmd_to_close = """-e 'tell app "Google Chrome" to close active tab of front window'"""


class Safari(Browser_wrapper):
    browser = "Safari"

    def __init__(self, **options):
        options['browser'] = self.browser
        super().__init__(**options)
        self._cmd_get_source = '''
                tell application "Safari"
                    set mySources to source of current tab of front window
                end tell'''
