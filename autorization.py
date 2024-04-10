class Autorization():

    def __init__(self, UserModel):
        self.isClientLogin: bool = False
        self.isUserLogin: bool = False

        self.loginName: str = ""

        isUsersExist = UserModel.query.all()
        print("Список существующих администраторов: ", isUsersExist)

        if len(isUsersExist) == 0:
            self.loginUser("! Временный администратор !")

    def logout(self):
        self.isClientLogin = False
        self.isUserLogin = False

        self.loginName = ""

    def loginClient(self, loginName):
        self.isClientLogin = True
        self.isUserLogin = False

        self.loginName = loginName

    def loginUser(self, loginName):
        self.isClientLogin = False
        self.isUserLogin = True

        self.loginName = loginName
