# Changelog

## 2.0.0 (In development)

* The shim now writes to Apple's unified logging system (`os_log`) instead of the deprecated `NSLog` API. Output written to `stdout` and `stderr` appears in Console.app and `log stream` as before, but is now tagged with the `OS_LOG_TYPE_DEFAULT` and `OS_LOG_TYPE_ERROR` levels respectively, so the two streams can be filtered separately.
* The `encoding` attribute on the writer is now `"utf-8"` (previously `"utf-16-le"` / `"utf-16-be"`), reflecting the underlying API.

## 1.0.3 (November 25 2022)

* Ensure that user-provided strings are escaped when output to the log. This could cause segfaults if the user-provided string contained `"%s"` (or other C-style formatting placeholders).

## 1.0.2 (November 17 2022)

* Corrected a bug where printing a blank line would cause the previous line to be duplicated in the log.

## 1.0.1 (April 7 2022)

* Removed the exception handling shim; this can now be handled by the iOS and macOS stub apps.

## 1.0.0 (Feb 28 2022)

Initial release
