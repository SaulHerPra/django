from django.db import models


class Question(models.Model):
    question_text = models.CharField('Titulo',max_length=200)
    pub_date = models.DateTimeField('Fecha de publicación')
    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural='Preguntas'

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='questions',on_delete=models.CASCADE)
    choice_text = models.CharField("Texto",max_length=200)
    votes = models.IntegerField("Votos",default=0)

    def __str__(self):
        return f"{self.question} - {self.choice_text} - {self.votes}"

    class Meta:
        verbose_name = 'Opción'
        verbose_name_plural='Opciones'
