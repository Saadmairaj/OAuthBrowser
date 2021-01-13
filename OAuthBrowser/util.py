import threading


def threaded(fn):
    """To use as decorator to make a function call threaded."""
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn,
                                  args=args,
                                  kwargs=kwargs,
                                  daemon=True)
        thread.start()
        thread.join()
        return thread
    return wrapper
