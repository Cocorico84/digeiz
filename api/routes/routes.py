from api.models.models import Account, Mall, Unit, db
from api.schemas.schemas import (account_schema, accounts_schema, mall_schema,
                                 malls_schema, unit_schema, units_schema)
from flask_restful import Resource, abort, reqparse


class AccountAPI(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        super().__init__()

    def get(self, account_id):
        account = Account.query.filter_by(id=account_id).first()
        if not account:
            abort(409, message='This account does not exist.')
        return account_schema.jsonify(account)

    def put(self, account_id):
        args = self.reqparse.parse_args()
        account = Account.query.filter_by(id=account_id).first()
        if not account:
            abort(409, message='This account does not exist.')
        account.name = args["name"]
        db.session.commit()
        return account_schema.jsonify(account)

    def delete(self, account_id):
        account = Account.query.filter_by(id=account_id).first()
        if not account:
            abort(409, message='This account does not exist.')
        db.session.delete(account)
        db.session.commit()
        return ''


class ListAccountAPI(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        super().__init__()

    def get(self):
        accounts = Account.query.all()
        return accounts_schema.jsonify(accounts)

    def post(self):
        args = self.reqparse.parse_args()
        account = Account(name=args["name"])
        db.session.add(account)
        db.session.commit()
        return account_schema.jsonify(account)


class MallAPI(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('account_id', type=int)
        super().__init__()

    def get(self, mall_id):
        mall = Mall.query.filter_by(id=mall_id).first()
        if not mall:
            abort(409, message='This mall does not exist.')
        return mall_schema.jsonify(mall)

    def put(self, mall_id):
        args = self.reqparse.parse_args()
        mall = Mall.query.filter_by(id=mall_id).first()
        if not mall:
            abort(409, message='This mall does not exist.')
        if args.get("name"):
            mall.name = args["name"]
        if args.get("account_id"):
            mall.account_id = args["account_id"]
        db.session.commit()
        return account_schema.jsonify(mall)

    def delete(self, mall_id):
        mall = Mall.query.filter_by(id=mall_id).first()
        if not mall:
            abort(409, message='This mall does not exist.')
        db.session.delete(mall)
        db.session.commit()
        return ''


class ListMallAPI(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('account_id', type=int)
        super().__init__()

    def get(self):
        malls = Mall.query.all()
        return malls_schema.jsonify(malls)

    def post(self):
        args = self.reqparse.parse_args()
        mall = Mall(name=args["name"], account_id=args['account_id'])
        db.session.add(mall)
        db.session.commit()
        return mall_schema.jsonify(mall)


class UnitAPI(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('mall_id', type=int)
        super().__init__()

    def get(self, unit_id):
        unit = Unit.query.filter_by(id=unit_id).first()
        if not unit:
            abort(409, message='This unit does not exist.')
        return unit_schema.jsonify(unit)

    def put(self, unit_id):
        args = self.reqparse.parse_args()
        unit = Unit.query.filter_by(id=unit_id).first()
        if not unit:
            abort(409, message='This unit does not exist.')
        if args.get("name"):
            unit.name = args["name"]
        if args.get("mall_id"):
            unit.account_id = args["mall_id"]
        db.session.commit()
        return unit_schema.jsonify(unit)

    def delete(self, unit_id):
        unit = Unit.query.filter_by(id=unit_id).first()
        if not unit:
            abort(409, message='This unit does not exist.')
        db.session.delete(unit)
        db.session.commit()
        return ''


class ListUnitAPI(Resource):
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('mall_id', type=int)
        super().__init__()

    def get(self):
        units = Unit.query.all()
        return units_schema.jsonify(units)

    def post(self):
        args = self.reqparse.parse_args()
        unit = Unit(name=args["name"], mall_id=args['mall_id'])
        db.session.add(unit)
        db.session.commit()
        return unit_schema.jsonify(unit)
