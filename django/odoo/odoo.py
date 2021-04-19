import xmlrpc.client
from datetime import datetime


class Odoo:
    def __init__(self, username, password):
        self.url = 'http://odoo:8069'
        self.db = 'foodcoops'
        self.username = username
        self.password = password

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
            return 1
        except Exception as e:
            print(e)
            print("common endpoint: ", self.common)
            print("models: ", self.models)
            print("uid: ", self.uid)
            return 0

    def searchPartnerByBirthdate(self, birthdate):
        return self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                                      'search_read', [[['birthdate', '=', birthdate]]], {'fields': ['id', 'email', 'name']})

    def searchPartnerByName(self, name):
        return self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                                      'search_read', [[['name', '=', name]]], {'fields': ['email', 'id']})

    def getOdooName(self, mail):
        encodedData = self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                                             'search_read', [[['email', '=', mail]]], {'fields': ['name']})
        sample = encodedData[0]
        decodedData = tuple(sample.items())
        return decodedData[1][1]

    def getOdooPartnerUid(self, mail):
        encodedData = self.models.execute_kw(self.db, self.uid, self.password, 'res.partner',
                                             'search_read', [[['email', '=', mail]]], {'fields': ['name']})
        sample = encodedData[0]
        decodedData = tuple(sample.items())
        return decodedData[0][1]


    def createEvent(self, name: str, dateBegin: str, dateEnd: str,
                    organizerID: int):
        return self.models.execute_kw(self.db, self.uid, self.password,
                                      'event.event', 'create',
                                      [{
                                          'name': name,
                                          'date_begin': dateBegin,
                                          'date_end': dateEnd,
                                          'organizer_id': organizerID,
                                      }])

    def getLatestCreatedEventOdooId(self, name: str, dateBegin: str, dateEnd: str, organizerId: int):
        encodedData = self.models.execute_kw(self.db, self.uid, self.password, 'event.event',
                                             'search_read', [[['organizer_id', '=', organizerId], ['name', '=', name], ['date_begin', '=', dateBegin],
                                              ['date_end', '=', dateEnd]]], {'fields': ['event_id']})
        sample = encodedData[-1]
        decodedData = tuple(sample.items())
        return decodedData[0][1] 

    def sendEventToOdoo(self, name: str, dateBegin: str, dateEnd: str, organizerId: int):
        self.createEvent(name,dateBegin,dateEnd,organizerId)
        return self.getLatestCreatedEventOdooId(name, dateBegin, dateEnd, organizerId)

    def getEventOdooId(self, name: str, eventId: int):
        encodedData = self.models.execute_kw(self.db, self.uid, self.password, 'event.event',
                                             'search_read', [[['organizer_id', '=', eventId], ['name', '=', name]]], {'fields': ['event_id']})

        sample = encodedData[0]
        decodedData = tuple(sample.items())
        return decodedData[0][1]

    def modifyOdooEvent(self, name: str, dateBegin: str, dateEnd: str,
                        organizerId: int, odooId):
        return self.models.execute_kw(self.db, self.uid, self.password,
                                      'event.event', 'write',
                                      [[odooId], {
                                          'name': name,
                                          'date_begin': dateBegin,
                                          'date_end': dateEnd,
                                          'organizer_id': organizerID
                                      }])

    def deleteOdooEvent(self, odooId: int):
        return self.models.execute_kw(self.db, self.uid, self.password,
                                      'event.event', 'unlink', [[odooId]])

    def getOdooAdminUid(self):
        if self.uid == False:
            return -1
        else:
            return self.uid

    def version(self) -> str:
        if self.common:
            return self.common.version()
        else:
            return "You need to connect first.\nExecute .setCommonEndpoint()"

    def formatDate(self, inputDate):
        tmpDate = datetime.strptime(inputDate, '%d/%m/%Y')
        return(tmpDate.strftime('%Y-%m-%d'))
