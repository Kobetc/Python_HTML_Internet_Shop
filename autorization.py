class Autorization():
        
        def __init__(self):
            self.isClientLogin: bool = False
            self.isUserLogin: bool = False

            self.currentClientId: int = 0
            self.currentUserId: int = 0

        def logout(self):
            self.isClientLogin = False
            self.isUserLogin = False

            self.currentClientId = 0
            self.currentUserId = 0

        def loginClient(self, clientId):
            self.isClientLogin = True
            self.isUserLogin = False

            self.currentClientId = clientId
            self.currentUserId = 0

        def loginUser(self, userId):
            self.isClientLogin = False
            self.isUserLogin = True

            self.currentClientId = 0
            self.currentUserId = userId