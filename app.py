from api.routes.routes import (AccountAPI, ListAccountAPI, ListMallAPI,
                               ListUnitAPI, MallAPI, UnitAPI)
from config import api, app

api.add_resource(AccountAPI, "/accounts/<int:account_id>")
api.add_resource(ListAccountAPI, "/accounts")
api.add_resource(MallAPI, "/malls/<int:mall_id>")
api.add_resource(ListMallAPI, "/malls")
api.add_resource(UnitAPI, "/units/<int:unit_id>")
api.add_resource(ListUnitAPI, "/units")

if __name__ == "__main__":
    app.run(debug=True)
