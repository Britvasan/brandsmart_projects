from django.db import models
from django.utils.timezone import now

class NewsTable(models.Model):
    news_choices = [
        ('news_website', 'No. of news published on Website'),
        ('news_socialmedia', 'No. of news published on Social Media'),
        ('newsletter_subscription', 'No. of subscriptions done for Newsletter'),
        ('email_newsletter', 'Newsletter prepared for customers via Email'),
    ]
    news_tasks = models.CharField(max_length=200,choices=news_choices)
    today_tasks = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_tasks
    
class NewsActivity(models.Model):
    task = models.ForeignKey(NewsTable, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # 'Added' or 'Updated'
    prev_today_tasks = models.IntegerField(null=True, blank=True, default=0)
    prev_total_tasks = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    @property
    def section_name(self):
        return "News"
    
    @property
    def task_name(self):
        return self.task.news_tasks

class MagazineTable(models.Model):
    magazine_choices = [
        ('magazine_designs', 'No. of pages designed for Magazine'),
        ('professionals_issue', 'No. of professionals prepared for the issue'),
        ('experts_issue', 'No. of experts prepared for the issue'),
        ('interview_questions', 'No. of Interview questionnaire prepared & sent'),
        ('new_advertisers', 'No. of new advertisers found & shared'),
        ('crossword_puzzles', 'No. of crossword puzzles prepared'),
    ]  
    magazine_tasks = models.CharField(max_length=200,choices=magazine_choices)
    today_tasks = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.magazine_tasks
    
class MagazineActivity(models.Model):
    task = models.ForeignKey(MagazineTable, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # 'Added' or 'Updated'
    prev_today_tasks = models.IntegerField(null=True, blank=True, default=0)
    prev_total_tasks = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    @property
    def section_name(self):
        return "Magazine"
    
    @property
    def task_name(self):
        return self.task.magazine_tasks

    
class SocialmediaTable(models.Model):
    socialmedia_choices = [
        ('linkedin_connection', 'No. of connections acquired on LinkedIn'),
        ('twitter_connection', 'No. of connections acquired on Twitter'),
        ('instagram_connection', 'No. of connections acquired on Instagram'),
        ('facebook_connection', 'No. of connections acquired on Facebook'),
    ]
    socialmedia_tasks = models.CharField(max_length=200,choices=socialmedia_choices)
    today_tasks = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.socialmedia_tasks
    
class SocialmediaActivity(models.Model):
    task = models.ForeignKey(SocialmediaTable, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # 'Added' or 'Updated'
    prev_today_tasks = models.IntegerField(null=True, blank=True, default=0)
    prev_total_tasks = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    @property
    def section_name(self):
        return "Socialmedia"
    
    @property
    def task_name(self):
        return self.task.socialmedia_tasks
    
class SlidesTable(models.Model):
    slides_choices = [
        ('business_slides', 'No. of slides prepared for Business team'),
        ('new_address', 'No. of new addresses collected'),
    ]
    slides_tasks = models.CharField(max_length=200, choices=slides_choices)
    today_tasks = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slides_tasks

class SlidesActivity(models.Model):
    task = models.ForeignKey(SlidesTable, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # 'Added' or 'Updated'
    prev_today_tasks = models.IntegerField(null=True, blank=True, default=0)
    prev_total_tasks = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    @property
    def section_name(self):
        return "Slides"
    
    @property
    def task_name(self):
        return self.task.slides_tasks

class OthersTable(models.Model):
    others_choices = [
        ('new_plugins', 'New Plugins designed'),
        ('other_tasks', 'Other tasks worked out'),
    ]
    other_tasks = models.CharField(max_length=200, choices=others_choices)
    today_tasks = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.other_tasks

class OthersActivity(models.Model):
    task = models.ForeignKey(OthersTable, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)  # 'Added' or 'Updated'
    prev_today_tasks = models.IntegerField(null=True, blank=True, default=0)
    prev_total_tasks = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    @property
    def section_name(self):
        return "Others"
    
    @property
    def task_name(self):
        return self.task.other_tasks