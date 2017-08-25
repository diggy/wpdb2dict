"""
Converts a WordPress database to a Python dictionary, using WP-CLI's `wp db query` command.
"""
from __future__ import print_function
import re
import sys
import argparse
import subprocess as sp

def compat(data):
    """
    Check data type, transform to string if needed.

    Args:
        data: The data.

    Returns:
        The data as a string, trimmed.
    """
    if not isinstance(data, str):
        data = data.decode()
    return data.rstrip()

def explode(data):
    """
    Split data string.

    Args:
        data: The data.

    Returns:
        A list.
    """
    return re.split(r'(?<!\\\\)\t', compat(data))

def main(args=None):
    """
    Converts a WordPress database to a Python dictionary, using WP-CLI's wp db query command.

    Args:
        args: The arguments.

    Returns:
        Void.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--path', type=str, required=True,
                        help='Path to the WordPress files.')
    parser.add_argument('--url', type=str, required=True,
                        help='Pretend request came from given URL.')
    args = parser.parse_args()

    data = {}
    command = [
        'wp', 'db', 'query', '{}',
        '--skip-column-names', '--path='+args.path, '--url='+args.url
    ]

    tables = sp.Popen([arg.format("SHOW TABLES") for arg in command],
                      stdout=sp.PIPE, bufsize=10**8)

    for table in tables.stdout.readlines():
        if table.startswith(b'Tables_in_'):
            continue
        table = compat(table)
        data[table] = {}
        cols = sp.Popen([arg.format("SHOW columns FROM "+table) for arg in command],
                        stdout=sp.PIPE, bufsize=10**8)
        colx = [explode(col) for col in cols.stdout.readlines()]
        proc = sp.Popen([arg.format("SELECT * FROM {}".format(table)) for arg in command],
                        stdout=sp.PIPE, bufsize=10**8)
        for line in proc.stdout.readlines():
            linex = explode(line)
            data[table].update({linex[0]:dict(zip([i[0] for i in colx], linex))})

    print(data)

if __name__ == '__main__':
    sys.exit(main())
