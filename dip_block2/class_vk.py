class VK_USER:

    def __init__(self, token, user_id, age, books, interests, movies, music, relation, sex):
        self.token = token
        self.user_id = user_id
        self.age = age
        self.books = books
        self.interests = interests
        self.movies = movies
        self.music = music
        self.relation = relation
        self.sex = sex
        self.params = {
            'access_token': token,
            'v': 5.92,
            'user_id': self.user_id,
         }
