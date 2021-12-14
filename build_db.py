import os

from api.models.models import Account, Mall, Unit, db


accounts = [
    {'id': '1', 'name': 'Farrell'},
    {'id': '2', 'name': 'Brockman'},
    {'id': '3', 'name': 'Easter'}
]

malls = [
    {'id': '1', 'name': 'Red', 'account_id': '1'},
    {'id': '2', 'name': 'Blue', 'account_id': '1'},
    {'id': '3', 'name': 'Green', 'account_id': '2'},

]

units = [
    {'id': '1', 'name': 'One', 'mall_id': '2'},
    {'id': '2', 'name': 'Two', 'mall_id': '1'},
    {'id': '3', 'name': 'Three', 'mall_id': '2'},

]

# Delete database file if it exists currently
if os.path.exists('app.db'):
    os.remove('app.db')

# Create the database
db.create_all()

# Iterate over the accounts structure and populate the database
for account in accounts:
    a = Account(name=account['name'])
    db.session.add(a)

for mall in malls:
    m = Mall(name=mall['name'], account_id=mall['account_id'])
    db.session.add(m)

for unit in units:
    u = Unit(name=unit['name'], mall_id=unit['mall_id'])
    db.session.add(u)

db.session.commit()
