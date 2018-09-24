
What's this lib?
================

This lib provided rotate proxy ip from free proxy list (for this moment):
* `free proxy list <https://free-proxy-list.net/>`_
* `sslproxies list <https://www.sslproxies.org/>`_


Downloading from code
_____________________

To download the latest source code enter the following command:

.. code-block:: bash

    git clone 


Usage
-----

.. code-block:: python

    from freeproxies import FreeProxies

    proxies = FreeProxies()
    print('elite', proxies.elite)
    print('anonymous', proxies.anonymous)
    print('random', proxies.random)
    print('transparent', proxies.transparent)


Notes
-----
Inspired by this blog's article:
* `How To Rotate Proxies and IP Addresses using Python 3 <https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/>`_
