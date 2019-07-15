from django.db import models
from django.conf import settings
from django.utils import timezone
import stripe
from django.contrib.auth.models import User
from datetime import datetime
# from shortuuidfield import ShortUUIDField


class Subscriber(models.Model):
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec

class QuestionsTable(models.Model):
    TYPE_LIST = (
                 (1, 'ASAP'),
                 (2, 'TODAY'),
                 (3, 'TOMORROW'),
                 (4, 'END WEEK'),
                 (5, 'NEXT WEEK'),
             )
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=100)
    question_details = models.CharField(max_length=100, blank=True)
    budget = models.CharField(max_length=50)
    field = models.CharField(max_length=30, blank=True)
    deadline = models.PositiveSmallIntegerField(choices=TYPE_LIST)
    email_address = models.CharField(max_length=100, blank=False)
    date_time = models.DateTimeField(default=datetime.now, blank=True)
    # document = models.FileField(upload_to='documents/')
    class Meta:
        verbose_name_plural = 'questions'

    def __unicode__(self):
        return u"%s's Questions Info" % self.user_rec


class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

# class Communication(models.Model):
#     uuid = ShortUUIDField(unique=True)
#     TYPE_LIST = (
#         (1, 'Meeting'),
#         (2, 'Phone'),
#         (3, 'Email'),
#     )
#     subject = models.CharField(max_length=50)
#     notes = models.TextField()
#     kind = models.PositiveSmallIntegerField(choices=TYPE_LIST)
#     date = models.DateField()
#     owner = models.ForeignKey(User)
#     account = models.ForeignKey(QuestionsTable)
#     created_on = models.DateField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'communications'
#
#     def __unicode__(self):
#         return u"%s" % self.subject
#
#     @models.permalink
#     def get_absolute_url(self):
#         return 'comm_detail', [self.uuid]
#
#     @models.permalink
#     def get_update_url(self):
#         return 'comm_update', [self.uuid]
#
#     @models.permalink
#     def get_delete_url(self):
#         return 'comm_delete', [self.id]