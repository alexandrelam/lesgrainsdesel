import xmlrpc.client
import sys
import json 


class Odoo:
    def __init__(self):
        self.url = 'http://lesgrainsdesel_app_1:8069'
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
            print("trying to set common endpoint ...")
            self.setCommonEndpoint()
            print("passed common endpoint")
            print("trying to authenticate ...")
            self.authenticate()
            print("passed auth")
            print("trying to set object endpoint ...")
            self.setObjectEndpoint()
            print("Connection successful ! ")
            print("common endpoint: ", self.common)
            print("models: ", self.models)
            print("uid: ", self.uid)
        except Exception as e:
            print(e)
            print("common endpoint: ", self.common)
            print("models: ", self.models)
            print("uid: ", self.uid)
            sys.exit()

    def searchRead(self, dbTable: str, filters: [str], fields: [str]):
        if self.models:
            return self.models.execute_kw(self.db, self.uid, self.password, dbTable,
                                            'search_read', [filters], {'fields': fields})


    def searchPartnerByBirthdate(self, birthdate):
        data = self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                'search_read',[[['birthdate', '=', birthdate]]], {'fields': ['name', 'id']})
        #output = json.loads(data)
        return data 


    def searchPartnerByName(self, name):
        return self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                'search_read',[[['name', '=', name]]], {'fields': ['birthdate', 'id']})

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
