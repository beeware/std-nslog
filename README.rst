.. image:: http://beeware.org/static/images/defaultlogo.png
    :width: 72px
    :target: https://beeware.org/

std-nslog
=========

.. image:: https://img.shields.io/pypi/pyversions/std-nslog.svg
   :target: https://pypi.python.org/pypi/std-nslog
   :alt: Python Versions

.. image:: https://img.shields.io/pypi/v/std-nslog.svg
   :target: https://pypi.python.org/pypi/std-nslog
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/status/std-nslog.svg
   :target: https://pypi.python.org/pypi/std-nslog
   :alt: Maturity

.. image:: https://img.shields.io/pypi/l/std-nslog.svg
   :target: https://github.com/beeware/std-nslog/blob/master/LICENSE
   :alt: BSD License

.. image:: https://img.shields.io/discord/836455665257021440?label=Discord%20Chat&logo=discord&style=plastic
   :target: https://beeware.org/bee/chat/
   :alt: Discord server

std-nslog is a shim that redirects stderr/stdout to the Apple System Log (NSLog).
This can be useful when deploying Python code as a standalone app on macOS or
iOS.

Usage
-----

std-nslog primary exists as a utility for std-nslog deployments. You shouldn't ever need
to install it yourself. However, just in case...

To install std-nslog::

    $ pip install std-nslog

Then, in your code, ``import nslog``. This will install the shim. The file
only needs to be imported once; preferably as early as possible in the

Once installed, all output written to stdout and stderr will be redirected to the Apple
System Log.

Why no pun?
-----------

While an obscure joke referencing apples and logs might be amusing, it would make
no sense when it appeared in a std-nslog requirements file.

Community
---------

gblub is part of the `BeeWare suite`_. You can talk to the community through:

* `@pybeeware on Twitter <https://twitter.com/pybeeware>`__

* `Discord <https://beeware.org/bee/chat/>`__

We foster a welcoming and respectful community as described in our
`BeeWare Community Code of Conduct`_.

Contributing
------------

If you experience problems with std-nslog, `log them on GitHub`_. If you
want to contribute code, please `fork the code`_ and `submit a pull request`_.

.. _BeeWare suite: http://beeware.org
.. _BeeWare Community Code of Conduct: http://beeware.org/community/behavior/
.. _log them on Github: https://github.com/beeware/std-nslog/issues
.. _fork the code: https://github.com/beeware/std-nslog
.. _submit a pull request: https://github.com/beeware/std-nslog/pulls
