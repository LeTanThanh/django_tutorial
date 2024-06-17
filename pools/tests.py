import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("pools:questions"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pools are available.")
        self.assertQuerySetEqual(response.context["question_list"], [])

    def test_future_questions(self):
        create_question(question_text="Past question.", days=30)
        response = self.client.get(reverse("pools:questions"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No pools are available.")
        self.assertQuerySetEqual(response.context["question_list"], [])

    def test_future_and_past_questions(self):
        create_question(question_text="Past question.", days=30)
        past_question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("pools:questions"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["question_list"], [past_question])

    def test_past_questions(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("pools:questions"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["question_list"], [question])

    def test_order_past_questions(self):
        question1 = create_question(question_text="Past question.", days=-30)
        question2 = create_question(question_text="Past question.", days=-5)
        response = self.client.get(reverse("pools:questions"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["question_list"], [question2, question1])


class QuesionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=30)
        url = reverse("pools:question_detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Future question.", days=-5)
        url = reverse("pools:question_detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
