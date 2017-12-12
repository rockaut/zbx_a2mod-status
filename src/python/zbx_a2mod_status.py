#!/usr/bin/env python3
"""
Zabbix apache2 httpd mod_status
"""

#
# official description of mod_status https://httpd.apache.org/docs/2.4/mod/mod_status.html
# good description of mod_status https://www.datadoghq.com/blog/collect-apache-performance-metrics/
#

__author__ = "Markus Fischbacher<fischbacher.markus@gmail.com>"
__version__ = "0.1.0"
__license__ = "GPL-3.0"


import argparse


def main(args):
    """ Main entry point of the app """
    print("hello world")
    print(args)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    # Required positional argument
    PARSER.add_argument(
        "-s",
        "--stats",
        type=str,
        choices=["all", "simple", "workers", "server", "load", "cpu", "totals", "throughput"],
        default="all",
        help="Defines which values are reported back. Defaults to ALL stats.\n"
        "all        > all available stats are reported back\n"
        "simple     > just simple worker stats\n"
        "workers    > complete worker stats\n"
        "server     > just server informations\n"
        "load       > server load infos\n"
        "cpu        > cpu stats\n"
        "totals     > available totals\n"
        "throughput > stats on throughput")

    PARSER.add_argument(
        "--json",
        action="store_true",
        help="Output stats as json.")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    PARSER.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    PARSER.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    ARGS = PARSER.parse_args()
    main(ARGS)
