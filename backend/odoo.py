import xmlrpc.client


class Odoo:
    def __init__(self):
        self.url = 'http://127.0.0.1:8069'
        self.db = 'foodcoops'
        self.username = 'admin'
        self.password = 'admin'

        self.common = None
        self.models = None

    def setCredentials(self, url: str, db: str, username: str, password: str):
        self.url = url
        self.db = db
        self.username = username
        self.password = password

    def setCommonEndpoint(self):
        self.common = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/common'.format(self.url))
        return common

    def setObjectEndpoint(self):
        self.models = xmlrpc.client.ServerProxy(
            '{}/xmlrpc/2/object'.format(self.url))
        return common

    def version(self) -> str:
        if self.common != None:
            return self.common.version()
        else:
            return "You need to connect first.\nExecute .setCommonEndpoint()"
