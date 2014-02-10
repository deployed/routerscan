routerscan
**********

This repository contains simple scanners developed for http://fajny.net.pl

It's not about attacking, but rather identifying affected home routers.
After detecting, steps like firewalling or reconfiguration should be taken
in order to protect clients against various vulnerabilities.

We will put here more checks if new attacks are discovered.

rom0rpscan (rom-0/rpFWUpload.html)
==================================

Simple scan for rom-0/rpFWUpload.html vulnerabilities found on popular home routers like:

* TD-W8951ND
* TD-W8961ND
* TD-W8901G
* TD-8816
* D-Link DSL-2640R
* ADSL Modem
* AirLive WT-2000ARM
* Pentagram Cerberus P 6331-42
* ZTE ZXV10 W300

Attack allows to decode firmware, discover password and as a consequence
modify DNS servers and e.g. redirect to fake bank website.

More info:

#) https://github.com/MrNasro/zynos-attacker/
#) http://niebezpiecznik.pl/post/dziura-w-routerach-z-firmwarem-zyxel-a-m-in-tp-link/ (Polish)

Installation
------------

Just install requirements::

    pip install -r requirements.txt

Example Usage
-------------

::

    python rom0rpscan.py `cat ip_adresses|xargs` > scan.log

As this tool is intended for ISP, not for attackers, assumption has been made
that list of hosts to scan is well known.
