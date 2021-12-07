from unittest import TestCase

from models import Account, Mall, Unit, db


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
