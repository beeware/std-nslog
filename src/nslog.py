# Python writes all console output to stdout/stderr. However, in production,
# macOS/iOS devices don't record stdout/stderr; only the Apple System Log
# is preserved.
#
# This handler redirects sys.stdout and sys.stderr to the Apple System Log
# by writing to Apple's unified logging system (os_log) via a small native
# extension module, and monkeypatching that wrapper over sys.stdout and
# sys.stderr.

import io
import sys

import _oslog_shim

# os_log_type_t values, re-exported from the native module so callers can
# pass them to ``nslog()`` without importing the shim themselves.
OS_LOG_TYPE_DEFAULT = _oslog_shim.OS_LOG_TYPE_DEFAULT
OS_LOG_TYPE_INFO = _oslog_shim.OS_LOG_TYPE_INFO
OS_LOG_TYPE_DEBUG = _oslog_shim.OS_LOG_TYPE_DEBUG
OS_LOG_TYPE_ERROR = _oslog_shim.OS_LOG_TYPE_ERROR
OS_LOG_TYPE_FAULT = _oslog_shim.OS_LOG_TYPE_FAULT


def nslog(s, level=OS_LOG_TYPE_DEFAULT):
    """Log the given Python [`str`][] to the unified system log.

    :param s: the message to log.
    :param level: an `OS_LOG_TYPE_*` constant selecting the log level.
        Defaults to `OS_LOG_TYPE_DEFAULT`.
    """
    # os_log accepts UTF-8 C strings; embedded NULs would truncate the
    # visible message, so strip them defensively.
    _oslog_shim.emit(level, s.replace("\x00", "").encode("utf-8"))


class NSLogWriter(io.TextIOBase):
    """An output-only text stream that writes to the unified system log.

    Writes are buffered and flushed one log entry per newline-terminated
    line, matching the behavior of the original NSLog-backed implementation.
    """

    def __init__(self, level):
        super().__init__()
        self._level = level
        self.buf = ""

    def write(self, s):
        self.buf += s
        lines = self.buf.split("\n")
        for line in lines[:-1]:
            nslog(line, self._level)
        self.buf = lines[-1]
        return len(s)

    def flush(self):
        # os_log entries are always whole lines; if there is partial
        # un-newlined output buffered, emit it now so it isn't lost on
        # interpreter shutdown.
        if self.buf:
            nslog(self.buf, self._level)
            self.buf = ""

    @property
    def encoding(self):
        return "utf-8"


# Replace stdout and stderr with NSLogWriters. stderr is tagged at the
# error level so it can be filtered separately in Console.app; this is
# a behavioral improvement over the legacy implementation, which merged
# both streams onto a single writer.
sys.stdout = NSLogWriter(OS_LOG_TYPE_DEFAULT)
sys.stderr = NSLogWriter(OS_LOG_TYPE_ERROR)
