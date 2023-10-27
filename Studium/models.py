from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pip._internal.resolution.resolvelib.resolver import Result


# A model for a course that contains quizzes and flashcards
class Course(models.Model):
    title = models.CharField(
        max_length=100)  # The title of the course # models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()  # *
    students = models.ManyToManyField(User, related_name="enrolled_courses")  # The users who enrolled in the course*

    # students = models.IntegerField() # The amount of users who enrolled the course*
    def __str__(self):
        return self.title


# A model for a quiz that belongs to a course
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name="quizzes")  # The course that the quiz belongs to
    title = models.CharField(max_length=100)
    number_of_questions = models.IntegerField(default=1)

    # instructions = models.TextField() # Not that important at all*
    # duration = models.IntegerField() # The time limit on single quiz*

    def __str__(self):
        return self.title


# A model for a question that belongs to a quiz
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name="questions")  # The quiz that the question belongs to
    text = models.TextField()

    def __str__(self):
        return self.text


# A model for a choice that belongs to a question
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name="choices")  # Question the choice belongs to
    text = models.CharField(max_length=100)  # The text of the choice
    is_correct = models.BooleanField()  # Boolean variable contains the correct field

    def __str__(self):
        return self.text  # also returning is_correct?*


# A model for an answer that belongs to a user and a question
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who submitted the answer
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # The question that the answer is for
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)  # The choice that user selected
    is_correct = models.BooleanField()  # Whether the answer is correct or not correct

    def __str__(self):
        return f"{self.user} answered {self.choice} for {self.question}"  # check this return*


# A model for a flashcard that belongs to a course
class Flashcard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name="flashcards")  # The course that the flashcard belongs to
    term = models.CharField(max_length=100)  # The term or concept on the flashcard
    definition = models.TextField()  # The definition or explanation of the term or concept
    percentage = models.FloatField()  # The percentage score of progress IMPORTANT update_score function*

    def __str__(self):
        return self.term  # percentage*


# A model for a score that belongs to a user and a quiz
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who took the quiz
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)  # The quiz that the user took
    total = models.IntegerField()  # The total number of questions
    correct = models.IntegerField()  # The number of correct answers
    wrong = models.IntegerField()  # The number of wrong answers
    percentage = models.FloatField()  # The percentage score of quiz

    def __str__(self):
        return f"{self.user} scored {self.percentage}% on {self.quiz}"


# A receiver function that updates the score and the result after an answer is saved
@receiver(post_save, sender=Answer)
def update_score(sender, instance, created, **kwargs):
    if created:  # Only run the function if a new answer is created
        user = instance.user  # Get the user who submitted the answer
        quiz = instance.question.quiz  # Get the quiz that the answer belongs to
        question = instance.question  # Get the question that the answer is for
        choice = instance.choice  # Get the choice that the user selected
        is_correct = instance.is_correct  # Get whether the answer is correct or not

        # Get or create a score object for the user and the quiz
        score, created = Score.objects.get_or_create(user=user, quiz=quiz)
        if created:  # If a new score object is created, initialize its fields
            score.total = quiz.questions.count()  # Set the total number of questions to the quiz's question count
            score.correct = 0  # Set the number of correct answers to zero
            score.wrong = 0  # Set the number of wrong answers to zero
            score.percentage = 0.0  # Set the percentage score to zero

        # Update the score object according to the answer's correctness
        if is_correct:  # If the answer is correct, increment the correct count and recalculate the percentage
            score.correct += 1
            score.percentage = (score.correct / score.total) * 100.0
        else:  # If the answer is wrong, increment the wrong count
            score.wrong += 1

        # Save the updated score object to the database
        score.save()

        # Update or create a result object for the question and the choice
        result, created = Result.objects.update_or_create(question=question, choice=choice)
        if created:  # If a new result object is created, initialize its fields
            result.count = 0  # Set the count of users who selected this choice to zero

        # Increment the count of users who selected this choice and save it to the database
        result.count += 1
        result.save()

########################################################################################################


# A model for a progress that belongs to a user and a course
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who is learning the flashcards
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # The course that the flashcards belong to
    total = models.IntegerField()  # The total number of flashcards in the course
    learned = models.IntegerField()  # The number of flashcards that the user has learned
    percentage = models.FloatField()  # The percentage of progress in the course

    def __str__(self):
        return f"{self.user} has learned {self.percentage}% of {self.course}"


# A receiver function that updates the progress after a flashcard is learned
@receiver(post_save, sender=Flashcard)
def update_progress(sender, instance, created, **kwargs):
    if created:  # Only run the function if a new flashcard is created
        user = instance.user  # Get the user who learned the flashcard
        course = instance.course  # Get the course that the flashcard belongs to
        term = instance.term  # Get the term or concept on the flashcard
        definition = instance.definition  # Get the definition or explanation of the term or concept

        # Get or create a progress object for the user and the course
        progress, created = Progress.objects.get_or_create(user=user, course=course)
        if created:  # If a new progress object is created, initialize its fields
            progress.total = course.flashcards.count()  # Set the total number of flashcards to the course flashcard count
            progress.learned = 0  # Set the number of flashcards learned to zero
            progress.percentage = 0.0  # Set the percentage of progress to zero

        # Update the progress object according to the flashcard's learning status
        if instance.learned:  # If the flashcard is learned, increment the learned count and recalculate the percentage
            progress.learned += 1
            progress.percentage = (progress.learned / progress.total) * 100.0
        else:  # If the flashcard is not learned, decrement the learned count and recalculate the percentage
            progress.learned -= 1
            progress.percentage = (progress.learned / progress.total) * 100.0

        # Save the updated progress object to the database
        progress.save()
