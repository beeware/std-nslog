# Changelog

## 1.0.3 (November 25 2022)

* Ensure that user-provided strings are escaped when output to the log. This
  could cause segfaults if the user-provided string contained `"%s"` (or other
  C-style formatting placeholders).

## 1.0.2 (November 17 2022)

* Corrected a bug where printing a blank line would cause the previous line
  to be duplicated in the log.

## 1.0.1 (April 7 2022)

* Removed the exception handling shim; this can now be handled by the iOS and
  macOS stub apps.

## 1.0.0 (Feb 28 2022)

Initial release
