import os

import sys
from ldap3 import Server, Connection, ALL, core


def connect(address, dn, password):
    # Create the Server object with the given address.
    server = Server(address, get_info=ALL)
    try:
        conn = Connection(server, dn, password, auto_bind=True)

    except core.exceptions.LDAPBindError as e:
        # If the LDAP bind failed for reasons such as authentication failure.
        print('LDAP Bind Failed: ', e)
        sys.exit()
    return conn

forest = {"test1.test.com": ["user", "pw"]}


def main():



if __name__ == '__main__':
    main()
