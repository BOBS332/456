from django.db import models
import datetime


class Author:
    Au_Us = models.ManyToOneRel(UserWarning)

    @property
    def like(self, rating: int):
        self.rating = rating
        return rating + 1
    @property
    def dislike(self, rating):
        self.rating = rating
        return rating - 1



    def update_rating(self):
        return self.rating*3

class Category:
    news = models.TextField(unique=True)
    article = models.TextField(unique=True)

class Post:
    ptoduct = models.ManyToOneRel(Author)
    time = datetime.now
    prod = models.ManyToManyField(Category, trought = "PostCategory")
    _header = models.CharField(max_length=124)
    text = models.TextField()
    rating = 0

    @property
    def like(self, P_rating: int):
        self.P_rating = P_rating
        return P_rating + 1

    @property
    def dislike(self, P_rating):
        self.P_rating = P_rating
        return P_rating - 1

    def preview(self):
        return self._header



class PostCategory:
    PC_P = models.ManyToOneRel(Post)
    PC_C = models.ManyToOneRel(Category)


class Comment:
    C_P = models.ManyToOneRel(Post)
    C_U = models.ManyToOneRel(UserWarning)
    _text = models.TextField()
    time = datetime.now

    @property
    def like(self, C_rating: int):
        self.C_rating = C_rating
        return C_rating + 1
    @property
    def dislike(self, C_rating):
        self.C_rating = C_rating
        return C_rating - 1


class Author:
    Au_Us = models.ManyToOneRel(UserWarning)

    @property
    def like(self, rating: int):
        self.rating = rating
        return rating + 1

    @property
    def dislike(self, rating):
        self.rating = rating
        return rating - 1

    def update_rating(self):
        self.rating =  self.rating * 3
        return self.rating, self.C_rating, self.P_rating




