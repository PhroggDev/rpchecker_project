## Site Connectivity checker from tutorial at [RealPython-dot-COM](https://realpython.com/site-connectivity-checker-python/)

### Description
This project from [RealPython](https://realpython.com/site-connectivity-checker-python) checks for connectivity either __*synchronously*__ or __*asynchronously*__.  It takes a list of target URLs, either passed as cli arguments or from a file with each URL on it's own line, and attempts to connect using *http* or *https* (port 80 and/or port 443). Success or failure of each connect attempt is then output using print.

This package has a single third-party dependency, *__aiohttp__*, for the asynchronous check and most functionality relies on the Python Standard Library.

#### To Be Done
I'm sure I'll be returning to this project sooner rather than later as it still needs tests implemented. Everywhere I look I am admonished or advised to adopt a __TDD__ (*test driven development*) mindset. Which of course makes a lot of sense.

### Files
* `__init__.py` enables this code as a Python package
* `__main__.py` is an entry-point script for the app
* `checker.py` provides the app's core functionality
* `cli.py` provides the cli for the app

#### Features to Add
Some features the article suggests would be *new and exciting* coding concepts to learn and explore.
* **Timing Support**: Measure the response time of each target queried.
* **Check-scheduling support**: Schedule multiple rounds of connectivity checks. Either for sites that are down at initial check or for some other reason a regular check needs to be done.
