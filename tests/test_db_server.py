from main import CategoryModel, ClientModel, ImageModel, PositionModel, UserModel


def test_client_list_from_db():
    ClientsFromQuery = ClientModel.query.all()

    assert ClientsFromQuery != None


def test_user_list_from_db():
    UsersFromQuery = UserModel.query.all()

    assert UsersFromQuery != None


def test_category_list_from_db():
    CategoriesFromQuery = CategoryModel.query.all()

    assert CategoriesFromQuery != None


def test_position_list_from_db():
    PositionsFromQuery = PositionModel.query.all()

    assert PositionsFromQuery != None


def test_image_list_from_db():
    ImagesFromQuery = ImageModel.query.all()

    assert ImagesFromQuery != None
