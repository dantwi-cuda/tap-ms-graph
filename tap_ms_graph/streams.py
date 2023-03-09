"""Stream type classes for tap-ms-graph."""

from tap_ms_graph.client import MSGraphStream


class SubscribedSkusStream(MSGraphStream):
    name = 'subscribedSkus'
    path = '/subscribedSkus'
    primary_keys = ['id']
    replication_key = None
    schema_filename = 'subscribedSkus.json'


class UsersStream(MSGraphStream):
    name = 'users'
    path = '/users'
    primary_keys = ['id']
    replication_key = None
    schema_filename = 'users.json'


class UsersStream(MSGraphStream):
    name = 'devices'
    path = '/devices'
    primary_keys = ['id']
    replication_key = None
    schema_filename = 'devices.json'

class UsersStream(MSGraphStream):
    name = 'signins'
    path = '/auditLogs/signIns'
    primary_keys = ['id']
    replication_key = 'createdDateTime'
    schema_filename = 'signins.json'
