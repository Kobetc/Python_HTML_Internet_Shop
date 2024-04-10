class Autorization():
        
        def __init__(self):
            self.isClientLogin: bool = False
            self.isUserLogin: bool = False

            self.loginName: str = ""

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