from unittest import TestCase

from api.models.models import Account, Mall, Unit, db
from config import app


class DatabaseTest(TestCase):
    def setUp(self):
        db.session.close()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_account(self):
        account = Account(id=1, name='test')
        db.session.add(account)
        db.session.commit()
        accounts = Account.query.all()
        assert account in accounts

    def test_update_account(self):
        account = Account(id=1, name='test')
        db.session.add(account)
        account.name = 'foo'
        db.session.commit()
        assert Account.query.filter_by(name='foo').first() is not None

    def test_delete_account(self):
        account = Account(id=1, name='test')
        db.session.add(account)
        db.session.commit()
        db.session.delete(account)
        assert Account.query.filter_by(name='test').first() is None

    def test_add_mall(self):
        mall = Mall(id=1, name='test', account_id='1')
        db.session.add(mall)
        db.session.commit()
        malls = Mall.query.all()
        assert mall in malls

    def test_update_mall(self):
        mall = Mall(id=1, name='test', account_id='1')
        db.session.add(mall)
        mall.name = 'foo'
        db.session.commit()
        assert mall.query.filter_by(name='foo').first() is not None

    def test_delete_mall(self):
        mall = Mall(id=1, name='test', account_id='1')
        db.session.add(mall)
        db.session.commit()
        db.session.delete(mall)
        assert mall.query.filter_by(name='test').first() is None

    def test_add_unit(self):
        unit = Unit(id=1, name='test', mall_id='1')
        db.session.add(unit)
        db.session.commit()
        units = Unit.query.all()
        assert unit in units

    def test_update_unit(self):
        unit = Unit(id=1, name='test', mall_id='1')
        db.session.add(unit)
        unit.name = 'foo'
        db.session.commit()
        assert unit.query.filter_by(name='foo').first() is not None

    def test_delete_unit(self):
        unit = Unit(id=1, name='test', mall_id='1')
        db.session.add(unit)
        db.session.commit()
        db.session.delete(unit)
        assert unit.query.filter_by(name='test').first() is None

class ApiTest(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_list_accounts(self):
        response = self.app.get('/accounts')
        self.assertEqual(200, response.status_code)

    def test_get_accounts(self):
        response = self.app.get('/accounts/1')
        self.assertEqual(200, response.status_code)

    def test_post_accounts(self):
        data = {"name": "test"}
        response = self.app.post('/accounts', data=data)
        self.assertEqual(200, response.status_code)

    def test_update_accounts(self):
        data = {"name": "new_name"}
        response = self.app.post('/accounts/1', data=data)
        self.assertEqual(200, response.status_code)

    def test_delete_accounts(self):
        response = self.app.delete('/accounts/1')
        self.assertEqual(200, response.status_code)

    def test_list_malls(self):
        response = self.app.get('/malls')
        self.assertEqual(200, response.status_code)

    def test_get_mall(self):
        response = self.app.get('/malls/1')
        self.assertEqual(200, response.status_code)

    def test_post_mall(self):
        data = {"name": "test", "account_id": 1}
        response = self.app.post('/malls', data=data)
        self.assertEqual(200, response.status_code)

    def test_update_mall(self):
        data = {"name": "new_name"}
        response = self.app.post('/malls/1', data=data)
        self.assertEqual(200, response.status_code)

    def test_delete_mall(self):
        response = self.app.delete('/malls/1')
        self.assertEqual(200, response.status_code)

    def test_list_units(self):
        response = self.app.get('/units')
        self.assertEqual(200, response.status_code)

    def test_get_unit(self):
        response = self.app.get('/units/1')
        self.assertEqual(200, response.status_code)

    def test_post_unit(self):
        data = {"name": "test", "mall_id": 1}
        response = self.app.post('/units', data=data)
        self.assertEqual(200, response.status_code)

    def test_update_unit(self):
        data = {"name": "new_name"}
        response = self.app.post('/units/1', data=data)
        self.assertEqual(200, response.status_code)

    def test_delete_unit(self):
        response = self.app.delete('/units/1')
        self.assertEqual(200, response.status_code)




