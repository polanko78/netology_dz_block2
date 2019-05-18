class VK_USER:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.params = {
            'access_token': token,
            'v': 5.92,
            'user_id': self.user_id,
         }

    def user_stat(self, age, books, interests, movies, music, relation, sex):
        self.age = age
        self.books = books
        self.interests = interests
        self.movies = movies
        self.music = music
        self.relation = relation
        self.sex = sex

    def friend_list(self, friend_list):
        self.fr_list = friend_list
