from main import CategoryModel, ClientModel


def test_client_list_from_db():
    ClientsFromQuery = ClientModel.query.all()

    assert ClientsFromQuery != None


def test_category_list_from_db():
    CategoriesFromQuery = CategoryModel.query.all()

    assert CategoriesFromQuery != None
