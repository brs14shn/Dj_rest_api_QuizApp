
from django.db import models

class UpdateCreateDate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Category Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    # @property
    # def quiz_count(self):
    #     return self.quizz.count()  # related name varsa
        #return self.quiz_set.count() # related name yoksa classname.lower()_set



class Quiz(UpdateCreateDate):
    title = models.CharField(max_length=50, verbose_name = 'Quiz Title')
    category = models.ForeignKey(Category, on_delete = models.CASCADE,related_name="quizz")
    #? delete questions when category changes (models.CASCADE) 👆
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Quizzes'

    @property
    def question_count(self):
        return self.question_set.count()


class Question(UpdateCreateDate):
    SCALE = (
        ('B', 'Beginner'),
        ('I', 'Intermadiate'),
        ('A', 'Advanced')
    )
    title = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    difficulty = models.CharField(max_length = 1, choices = SCALE)
    

    def __str__(self):
        return self.title
 

class Option(UpdateCreateDate):
    option_text = models.CharField(max_length = 200)
    question = models.ForeignKey(Question, on_delete = models.CASCADE,related_name="options")
    is_right = models.BooleanField(default=False)
    

    def __str__(self):
        return self.option_text