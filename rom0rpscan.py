#!/usr/bin/env python
import sys
import requests
from requests.exceptions import ConnectionError, Timeout

"""
This script scans given ips for rom-0/rpFWUpload.html vulnerabilities.
For more details see README.
"""

dangerous_files = ["rom-0", "rpFWUpload.html"]

found_hosts = []
hosts = sys.argv[1:]

if not hosts:
    print("Usage: {0} <<ip addresses list>>".format(sys.argv[0]))
    sys.exit(0)

for host in hosts:
    for f in dangerous_files:
        url = 'http://{0}/{1}'.format(host, f)

        print("Trying {0}".format(url))

        try:
            response = requests.get(url, allow_redirects=False, timeout=1)
        except (ConnectionError, Timeout):
            break  # no need to check other files if we can't connect
        else:
            if response.status_code < 300:
                print(">>> Router {0} is possibly vulnerable! File: {1}".format(host, f))
                found_hosts.append(host)

print("Found {0} possibly vulnerable routers".format(len(found_hosts)))
for host in found_hosts:
    print(host)
