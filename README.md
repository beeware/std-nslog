[<img src="http://beeware.org/static/images/defaultlogo.png" width="72px" alt="Generic BeeWare Logo">](https://beeware.org/)

# std-nslog

[![Python Versions](https://img.shields.io/pypi/pyversions/std-nslog.svg)](https://pypi.python.org/pypi/std-nslog)
[![PyPI Version](https://img.shields.io/pypi/v/std-nslog.svg)](https://pypi.python.org/pypi/std-nslog)
[![Maturity](https://img.shields.io/pypi/status/std-nslog.svg)](https://pypi.python.org/pypi/std-nslog)
[![BSD License](https://img.shields.io/pypi/l/std-nslog.svg)](https://github.com/beeware/std-nslog/blob/main/LICENSE)
[![Discord server](https://img.shields.io/discord/836455665257021440?label=Discord%20Chat&logo=discord&style=plastic)](https://beeware.org/bee/chat/)

std-nslog is a shim that redirects stderr/stdout to the Apple System Log
(NSLog). This can be useful when deploying Python code as a standalone
app on macOS or iOS.

## Usage

std-nslog primary exists as a utility for briefcase deployments. You
shouldn't ever need to install it yourself. However, just in case...

To install std-nslog:

    $ pip install std-nslog

Then, in your code, `import nslog`. This will install the shim. The file
only needs to be imported once; preferably as early as possible in the
Python application code.

Once installed, all output written to stdout and stderr will be
redirected to the Apple System Log.

## Why no pun?

While an obscure joke referencing apples and logs might be amusing, it
would make no sense when it appeared in a Briefcase requirements file.

## Community

std-nslog is part of the [BeeWare suite](http://beeware.org). You can talk
to the community through:

- [@pybeeware on Twitter](https://twitter.com/pybeeware)
- [Discord](https://beeware.org/bee/chat/)

We foster a welcoming and respectful community as described in our [BeeWare
Community Code of Conduct](http://beeware.org/community/behavior/).

## Contributing

If you experience problems with std-nslog, [log them on
GitHub](https://github.com/beeware/std-nslog/issues). If you want to contribute
code, please [fork the code](https://github.com/beeware/std-nslog) and [submit a
pull request](https://github.com/beeware/std-nslog/pulls).
