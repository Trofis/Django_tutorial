import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() - datetime.timedelta(days=1, minutes=1)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_new_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True)

