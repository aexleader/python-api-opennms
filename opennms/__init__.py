'''
'''

import os
from opennms import api

def initialize(server=None, port=None, user=None, password=None):
    '''
    Initialize and configure OpenNMS.api module.

    :param server: The address or fqdn of an OpenNMS server instance
    :type server: string

    :param port: The port to use when connecting to the server instance
    :type port: integer

    :param user: The user account to use when connecting to the server instance
    :type user: string

    :param password: The password to use when connecting to the server instance
    :type password: string
    '''

    # configure api
    api.server = server if server is not None else os.environ.get('OPENNMS_API_SERVER')
    api.port = port if port is not None else os.environ.get('OPENNMS_API_PORT')
    api.user = user if user is not None else os.environ.get('OPENNMS_API_USER')
    api.password = password if password is not None else os.environ.get('OPENNMS_API_PASSWORD')

    # http client & api options
    for key, value in iteritems(kwargs):
        attribute = "_{0}".format(key)
        setattr(api, attribute, value)
