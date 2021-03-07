
class Logger:
    BUFFER_SIZE = 100

    def __init__(self):
        self._buffer = []
        self._log_file = 'log.main.txt'

    def __enter__(self):
        with open(self._log_file, 'w') as f:
            f.write('')
        return self

    def log(self, msg):
        self._buffer.append(msg)
        if len(self._buffer) >= Logger.BUFFER_SIZE:
            self._flush()

    def _flush(self):
        with open(self._log_file, 'a') as f:
            f.writelines(self._buffer)
        self._buffer.clear()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._flush()


class ErrorLogger(Logger):
    def __init__(self):
        super().__init__()
        self._log_file = 'log.error.txt'
