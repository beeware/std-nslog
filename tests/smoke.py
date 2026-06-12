"""
std-nslog smoke test driver.

This file is a *helper* for `test_smoke.py`, not a test itself.
It imports nslog, and outputs some known strings to the console.
"""

import sys

import nslog


def main(tag) -> None:
    # Importing nslog should have replaced both standard streams with
    # NSLogWriter instances; if it didn't, nothing else here is meaningful.
    assert isinstance(sys.stdout, nslog.NSLogWriter), (
        f"sys.stdout was not replaced by NSLogWriter (got {type(sys.stdout)!r})"
    )
    assert isinstance(sys.stderr, nslog.NSLogWriter), (
        f"sys.stderr was not replaced by NSLogWriter (got {type(sys.stderr)!r})"
    )

    # Exercise stdout, stderr, and direct nslog() calls at multiple log
    # levels. Each line is tagged so the CI verifier can pick them out of
    # the unified log unambiguously.
    print(f"{tag} hello from std-nslog smoke test")
    print(f"{tag} this is stderr", file=sys.stderr)
    nslog.nslog(f"{tag} explicit info", level=nslog.OS_LOG_TYPE_INFO)
    nslog.nslog(f"{tag} explicit error", level=nslog.OS_LOG_TYPE_ERROR)

    print(f"{tag} string with an \x00 embedded null")

    # NSLogWriter buffers partial lines until a newline arrives; flush
    # explicitly so nothing is dropped before the unified-log query runs.
    sys.stdout.flush()
    sys.stderr.flush()


if __name__ == "__main__":
    main(sys.argv[1])
