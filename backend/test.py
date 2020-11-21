import xmlrpc.client

# https://www.odoo.com/documentation/9.0/api_integration.html

url = 'http://127.0.0.1:8069'
db = 'foodcoops'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

print(common.version())

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

res = models.execute_kw(db, uid, password,
                        'event.event', 'search_read',
                        [[]],
                        {'fields': [], 'limit': 5})

for el in res:
    with open("output", "w") as f:
        f.write(str(el))
    print(el)

print("len of res", len(res))
