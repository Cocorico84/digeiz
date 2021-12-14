from config import ma
from api.models.models import Account, Mall, Unit


class AccountSchema(ma.Schema):
    class Meta:
        model = Account
        fields = ('id', 'name',)


class MallSchema(ma.Schema):
    class Meta:
        model = Mall
        fields = ('id', 'name', 'account_id',)


class UnitSchema(ma.Schema):
    class Meta:
        model = Unit
        fields = ('id', 'name', 'mall_id',)


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
mall_schema = MallSchema()
malls_schema = MallSchema(many=True)
unit_schema = UnitSchema()
units_schema = UnitSchema(many=True)
