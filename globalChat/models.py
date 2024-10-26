from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Forum Model
class Forum(models.Model):
    TITLE_MAX_LENGTH = 75

    PURPOSE_CHOICES = [
        ('Asking', 'Asking'),
        ('Sharing', 'Sharing'),
        ('Open Discussion', 'Open Discussion'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    description = models.TextField()
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Connects to the Django User
    posted_time = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='forum_likes', blank=True)
    bookmarks = models.ManyToManyField(User, related_name="bookmarked_forums", blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

# Comment Model
class Comment(models.Model):
    forum = models.ForeignKey(Forum, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='globalchat_comments')
    text = models.TextField()
    posted_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user} on {self.forum.title}"
