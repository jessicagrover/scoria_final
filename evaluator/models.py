# evaluator/models.py
from django.db import models

class Evaluation(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    score = models.CharField(max_length=10)  # Assuming score is a string like '85%'
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Evaluation for question: {self.question_text[:50]}"
