import xmlrpc.client


class Odoo:
    def __init__(self):
        self.url = 'http://172.27.0.1:8069'
        self.db = 'foodcoops'
        self.username = 'admin'
        self.password = 'admin'

        self.common = None
        self.models = None
        self.uid = None

    def setCredentials(self, url: str, db: str, username: str, password: str):
        self.url = url
        self.db = db
        self.username = username
        self.password = password

    def setCommonEndpoint(self):
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(
            self.url))

    def authenticate(self):
        self.uid = self.common.authenticate(self.db, self.username,
                                            self.password, {})

    def setObjectEndpoint(self):
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(
            self.url))

    def connect(self):
        try:
            self.setCommonEndpoint()
            print("passed common endpoint")
            self.authenticate()
            print("passed auth")
            self.setObjectEndpoint()
            print("Connection successful ! ")
        except Exception as e:
            print(e)

    def searchRead(self, dbTable: str, filters: [str], fields: [str]):
        if self.models:
            return self.models.execute_kw(self.db, self.uid, self.password, dbTable,
                                            'search_read', [filters], {'fields': fields})


    def searchPartnerByBirthdate(self, birthdate):
        return self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                'search_read',[[['birthdate', '=', birthdate]]], {'fields': ['name', 'id']})



    '''
    odoo.createEvent("cree avec python", "2020-11-25 20:18:18",
                     "2020-11-26 20:18:18", 6)
    '''

    def createEvent(self, name: str, dateBegin: str, dateEnd: str,
                    organizerID: int):
        """
        Date example : 2020-11-25 20:18:18"
        """
        return self.models.execute_kw(self.db, self.uid, self.password,
                                      'event.event', 'create',
                                      [{
                                          'name': name,
                                          'date_begin': dateBegin,
                                          'date_end': dateEnd,
                                          'organizer_id': organizerID
                                      }])

    def version(self) -> str:
        if self.common:
            return self.common.version()
        else:
            return "You need to connect first.\nExecute .setCommonEndpoint()"
