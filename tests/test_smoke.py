from __future__ import annotations

import subprocess
import sys
import time
import uuid
from pathlib import Path


def test_system_log():
    tag = f"std-nslog-smoke-{uuid.uuid4()}"

    result = subprocess.run(
        [sys.executable, Path(__file__).parent / "smoke.py", tag],
        capture_output=True,
        text=True,
        check=False,
    )

    # Assert that the smoke test ran without error.
    assert result.returncode == 0

    # Nothing the script `print()`ed should have reached stdio
    assert result.stdout == "", (
        f"unexpected bytes on subprocess stdout: {result.stdout!r}"
    )
    assert result.stderr == "", (
        f"unexpected bytes on subprocess stderr: {result.stderr!r}"
    )

    # Give the unified logging subsystem a moment to commit the writes,
    # then extract the last 10s of system logs.
    time.sleep(2)

    log = subprocess.check_output(
        ["log", "show", "--last", "10s", "--info"],
        text=True,
    )

    missing = [
        msg
        for msg in [
            "hello from std-nslog smoke test",
            "this is stderr",
            "explicit info",
            "explicit error",
            "string with an À embedded null",
        ]
        if f"{tag} {msg}" not in log
    ]

    assert not missing, (
        "Expected message(s) not found in `log show` output: "
        + ", ".join(repr(m) for m in missing)
    )
