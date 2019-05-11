class VK_USER:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.params = {
            'access_token': token,
            'v': 5.92,
            'user_id': self.user_id,
         }
