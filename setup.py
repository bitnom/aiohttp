# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiohttp']

package_data = \
{'': ['*']}

install_requires = \
['aiosignal>=1.1.2',
 'async-timeout==4.0.0a3',
 'chardet>=2.0,<5.0',
 'frozenlist>=1.1.1',
 'multidict>=4.5,<7.0',
 'typing-extensions>=3.7.4',
 'yarl>=1.0,<2.0']

extras_require = \
{':python_version < "3.8"': ['asynctest==0.13.0'],
 'speedups': ['aiodns>=1.1', 'brotli', 'cchardet']}

setup_kwargs = {
    'name': 'aiohttp',
    'version': '4.0.1',
    'description': 'Async http client/server framework (asyncio)',
    'long_description': '==================================\nAsync http client/server framework\n==================================\n\n.. image:: https://raw.githubusercontent.com/aio-libs/aiohttp/master/docs/_static/aiohttp-icon-128x128.png\n   :height: 64px\n   :width: 64px\n   :alt: aiohttp logo\n\n|\n\n.. image:: https://github.com/aio-libs/aiohttp/workflows/CI/badge.svg\n   :target: https://github.com/aio-libs/aiohttp/actions?query=workflow%3ACI\n   :alt: GitHub Actions status for master branch\n\n.. image:: https://codecov.io/gh/aio-libs/aiohttp/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/aio-libs/aiohttp\n   :alt: codecov.io status for master branch\n\n.. image:: https://badge.fury.io/py/aiohttp.svg\n   :target: https://pypi.org/project/aiohttp\n   :alt: Latest PyPI package version\n\n.. image:: https://img.shields.io/pypi/dm/aiohttp\n   :target: https://pypistats.org/packages/aiohttp\n   :alt: Downloads count\n\n.. image:: https://readthedocs.org/projects/aiohttp/badge/?version=latest\n   :target: https://docs.aiohttp.org/\n   :alt: Latest Read The Docs\n\n.. image:: https://img.shields.io/discourse/status?server=https%3A%2F%2Faio-libs.discourse.group\n   :target: https://aio-libs.discourse.group\n   :alt: Discourse status\n\n.. image:: https://badges.gitter.im/Join%20Chat.svg\n   :target: https://gitter.im/aio-libs/Lobby\n   :alt: Chat on Gitter\n\n\nKey Features\n============\n\n- Supports both client and server side of HTTP protocol.\n- Supports both client and server Web-Sockets out-of-the-box and avoids\n  Callback Hell.\n- Provides Web-server with middlewares and plugable routing.\n\n\nGetting started\n===============\n\nClient\n------\n\nTo get something from the web:\n\n.. code-block:: python\n\n  import aiohttp\n  import asyncio\n\n  async def main():\n\n      async with aiohttp.ClientSession() as session:\n          async with session.get(\'http://python.org\') as response:\n\n              print("Status:", response.status)\n              print("Content-type:", response.headers[\'content-type\'])\n\n              html = await response.text()\n              print("Body:", html[:15], "...")\n\n  loop = asyncio.get_event_loop()\n  loop.run_until_complete(main())\n\nThis prints:\n\n.. code-block::\n\n    Status: 200\n    Content-type: text/html; charset=utf-8\n    Body: <!doctype html> ...\n\nComing from `requests <https://requests.readthedocs.io/>`_ ? Read `why we need so many lines <https://aiohttp.readthedocs.io/en/latest/http_request_lifecycle.html>`_.\n\nServer\n------\n\nAn example using a simple server:\n\n.. code-block:: python\n\n    # examples/server_simple.py\n    from aiohttp import web\n\n    async def handle(request):\n        name = request.match_info.get(\'name\', "Anonymous")\n        text = "Hello, " + name\n        return web.Response(text=text)\n\n    async def wshandle(request):\n        ws = web.WebSocketResponse()\n        await ws.prepare(request)\n\n        async for msg in ws:\n            if msg.type == web.WSMsgType.text:\n                await ws.send_str("Hello, {}".format(msg.data))\n            elif msg.type == web.WSMsgType.binary:\n                await ws.send_bytes(msg.data)\n            elif msg.type == web.WSMsgType.close:\n                break\n\n        return ws\n\n\n    app = web.Application()\n    app.add_routes([web.get(\'/\', handle),\n                    web.get(\'/echo\', wshandle),\n                    web.get(\'/{name}\', handle)])\n\n    if __name__ == \'__main__\':\n        web.run_app(app)\n\n\nDocumentation\n=============\n\nhttps://aiohttp.readthedocs.io/\n\n\nDemos\n=====\n\nhttps://github.com/aio-libs/aiohttp-demos\n\n\nExternal links\n==============\n\n* `Third party libraries\n  <http://aiohttp.readthedocs.io/en/latest/third_party.html>`_\n* `Built with aiohttp\n  <http://aiohttp.readthedocs.io/en/latest/built_with.html>`_\n* `Powered by aiohttp\n  <http://aiohttp.readthedocs.io/en/latest/powered_by.html>`_\n\nFeel free to make a Pull Request for adding your link to these pages!\n\n\nCommunication channels\n======================\n\n*aio-libs discourse group*: https://aio-libs.discourse.group\n\n*gitter chat* https://gitter.im/aio-libs/Lobby\n\nWe support `Stack Overflow\n<https://stackoverflow.com/questions/tagged/aiohttp>`_.\nPlease add *aiohttp* tag to your question there.\n\nRequirements\n============\n\n- Python >= 3.7\n- async-timeout_\n- attrs_\n- chardet_\n- multidict_\n- yarl_\n\nOptionally you may install the cChardet_ and aiodns_ libraries (highly\nrecommended for sake of speed).\n\n.. _chardet: https://pypi.python.org/pypi/chardet\n.. _aiodns: https://pypi.python.org/pypi/aiodns\n.. _attrs: https://github.com/python-attrs/attrs\n.. _multidict: https://pypi.python.org/pypi/multidict\n.. _yarl: https://pypi.python.org/pypi/yarl\n.. _async-timeout: https://pypi.python.org/pypi/async_timeout\n.. _cChardet: https://pypi.python.org/pypi/cchardet\n\nLicense\n=======\n\n``aiohttp`` is offered under the Apache 2 license.\n\n\nKeepsafe\n========\n\nThe aiohttp community would like to thank Keepsafe\n(https://www.getkeepsafe.com) for its support in the early days of\nthe project.\n\n\nSource code\n===========\n\nThe latest developer version is available in a GitHub repository:\nhttps://github.com/aio-libs/aiohttp\n\nBenchmarks\n==========\n\nIf you are interested in efficiency, the AsyncIO community maintains a\nlist of benchmarks on the official wiki:\nhttps://github.com/python/asyncio/wiki/Benchmarks\n',
    'author': 'Nikolay Kim',
    'author_email': 'fafhrd91@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aio-libs/aiohttp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
