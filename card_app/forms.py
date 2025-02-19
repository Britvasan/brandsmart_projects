from django import forms
from .models import NewsTable, MagazineTable, SocialmediaTable, SlidesTable, OthersTable

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsTable
        fields = ['news_tasks', 'today_tasks', 'total_tasks']
        widgets = {
            'news_tasks': forms.Select(attrs={'class': 'form-control'}),
            'today_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def update_today_tasks(self, value):
        """Method to update today's task count."""
        self.instance.today_tasks = value
        self.save()

    def update_total_tasks(self, value):
        """Method to update total task count."""
        self.instance.total_tasks = value
        self.save()

class MagazineForm(forms.ModelForm):
    class Meta:
        model = MagazineTable
        fields = ['magazine_tasks', 'today_tasks', 'total_tasks']
        widgets = {
            'magazine_tasks': forms.Select(attrs={'class': 'form-control'}),
            'today_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def update_today_tasks(self, value):
        """Method to update today's task count."""
        self.instance.today_tasks = value
        self.save()

    def update_total_tasks(self, value):
        """Method to update total task count."""
        self.instance.total_tasks = value
        self.save()

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialmediaTable
        fields = ['socialmedia_tasks', 'today_tasks', 'total_tasks']
        widgets = {
            'socialmedia_tasks': forms.Select(attrs={'class': 'form-control'}),
            'today_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def update_today_tasks(self, value):
        """Method to update today's task count."""
        self.instance.today_tasks = value
        self.save()

    def update_total_tasks(self, value):
        """Method to update total task count."""
        self.instance.total_tasks = value
        self.save()

class SlidesForm(forms.ModelForm):
    class Meta:
        model = SlidesTable
        fields = ['slides_tasks', 'today_tasks', 'total_tasks']
        widgets = {
            'slides_tasks': forms.Select(attrs={'class': 'form-control'}),
            'today_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def update_today_tasks(self, value):
        """Method to update today's task count."""
        self.instance.today_tasks = value
        self.save()

    def update_total_tasks(self, value):
        """Method to update total task count."""
        self.instance.total_tasks = value
        self.save()

class OthersForm(forms.ModelForm):
    class Meta:
        model = OthersTable
        fields = ['other_tasks', 'today_tasks', 'total_tasks']
        widgets = {
            'other_tasks': forms.Select(attrs={'class': 'form-control'}),
            'today_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_tasks': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def update_today_tasks(self, value):
        """Method to update today's task count."""
        self.instance.today_tasks = value
        self.save()

    def update_total_tasks(self, value):
        """Method to update total task count."""
        self.instance.total_tasks = value
        self.save()
