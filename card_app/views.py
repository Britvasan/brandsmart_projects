from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewsForm,MagazineForm,SlidesForm,SocialMediaForm,OthersForm
from .models import NewsTable, MagazineTable, SlidesTable, SocialmediaTable, OthersTable
from .models import NewsActivity, MagazineActivity, SlidesActivity, SocialmediaActivity, OthersActivity
from django.http import JsonResponse
from django.utils import timezone
from django.utils.timezone import localtime, now

# Create your views here.

def index(request):
    return render(request, 'card_app/index.html')

def all_activities(request):
    today = localtime(now())
    current_month = today.month
    current_year = today.year

    # Fetching activities and adding section names and task names
    news_activities = NewsActivity.objects.filter(timestamp__month=current_month, timestamp__year=current_year).select_related('task')
    magazine_activities = MagazineActivity.objects.filter(timestamp__month=current_month, timestamp__year=current_year).select_related('task')
    social_activities = SocialmediaActivity.objects.filter(timestamp__month=current_month, timestamp__year=current_year).select_related('task')
    slides_activities = SlidesActivity.objects.filter(timestamp__month=current_month, timestamp__year=current_year).select_related('task')
    others_activities = OthersActivity.objects.filter(timestamp__month=current_month, timestamp__year=current_year).select_related('task')

    # Adding section names and task names dynamically
    all_activities = []
    
    for activity in news_activities:
        all_activities.append({
            "section": "News",
            "task": activity.task.news_tasks,  # Ensure task field exists
            "action": activity.action,
            "timestamp": activity.timestamp
        })

    for activity in magazine_activities:
        all_activities.append({
            "section": "Magazine",
            "task": activity.task.magazine_tasks,
            "action": activity.action,
            "timestamp": activity.timestamp
        })

    for activity in social_activities:
        all_activities.append({
            "section": "Social Media",
            "task": activity.task.socialmedia_tasks,
            "action": activity.action,
            "timestamp": activity.timestamp
        })

    for activity in slides_activities:
        all_activities.append({
            "section": "Slides",
            "task": activity.task.slides_tasks,
            "action": activity.action,
            "timestamp": activity.timestamp
        })

    for activity in others_activities:
        all_activities.append({
            "section": "Others",
            "task": activity.task.other_tasks,
            "action": activity.action,
            "timestamp": activity.timestamp
        })

    # Sort activities by timestamp (latest first)
    all_activities.sort(key=lambda x: x["timestamp"], reverse=True)

    month_name = today.strftime("%B %Y")  # e.g., "February 2025"

    return render(request, "card_app/all_activities.html", {"activities": all_activities, "month_name": month_name})

def news_form(request):
    tasks = NewsTable.objects.all()

    if request.method == "POST":
        form = NewsForm(request.POST)

        if form.is_valid():
            news_task = form.cleaned_data['news_tasks']
            today_tasks = form.cleaned_data['today_tasks']

            # Get or create the task
            task, created = NewsTable.objects.get_or_create(news_tasks=news_task)

            # Capture previous values before updating
            prev_today = task.today_tasks
            prev_total = task.total_tasks  

            # Update task details
            task.today_tasks = today_tasks
            task.total_tasks += today_tasks  
            task.timestamp = timezone.now()
            task.save()

            # Log activities correctly with previous values
            if created:
                NewsActivity.objects.create(
                    task=task, action="Added",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )
            elif prev_total != task.total_tasks:  # Only log if total changes
                NewsActivity.objects.create(
                    task=task, action="Modified",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )

            return JsonResponse({
                "success": True,
                "task_name": news_task,
                "today_tasks": today_tasks,
                "total_tasks": task.total_tasks
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return render(request, "card_app/news_form.html", {"tasks": tasks, "form": NewsForm()})





def news_activities(request):
    activities = NewsActivity.objects.all().order_by('-timestamp')  # Fetch only logged activities

    return render(request, "card_app/news_activities.html", {"activities": activities})

def magazine_form(request):
    tasks = MagazineTable.objects.all()

    if request.method == "POST":
        form = MagazineForm(request.POST)

        if form.is_valid():
            magazine_task = form.cleaned_data['magazine_tasks']
            today_tasks = form.cleaned_data['today_tasks']

            task, created = MagazineTable.objects.get_or_create(magazine_tasks=magazine_task)

            prev_today = task.today_tasks
            prev_total = task.total_tasks  

            task.today_tasks = today_tasks
            task.total_tasks += today_tasks  
            task.timestamp = timezone.now()
            task.save()

            if created:
                MagazineActivity.objects.create(
                    task=task, action="Added",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )
            elif prev_total != task.total_tasks:
                MagazineActivity.objects.create(
                    task=task, action="Modified",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )

            return JsonResponse({
                "success": True,
                "task_name": magazine_task,
                "today_tasks": today_tasks,
                "total_tasks": task.total_tasks
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return render(request, "card_app/magazine_form.html", {"tasks": tasks, "form": MagazineForm()})


def magazine_activities(request):
    activities = MagazineActivity.objects.all().order_by('-timestamp')  # Fetch only logged activities

    return render(request, "card_app/magazine_activities.html", {"activities": activities})


def social_form(request):
    tasks = SocialmediaTable.objects.all()

    if request.method == "POST":
        form = SocialMediaForm(request.POST)

        if form.is_valid():
            social_task = form.cleaned_data['socialmedia_tasks']
            today_tasks = form.cleaned_data['today_tasks']

            task, created = SocialmediaTable.objects.get_or_create(socialmedia_tasks=social_task)

            prev_today = task.today_tasks
            prev_total = task.total_tasks  

            task.today_tasks = today_tasks
            task.total_tasks += today_tasks  
            task.timestamp = timezone.now()
            task.save()

            if created:
                SocialmediaActivity.objects.create(
                    task=task, action="Added",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )
            elif prev_total != task.total_tasks:
                SocialmediaActivity.objects.create(
                    task=task, action="Modified",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )

            return JsonResponse({
                "success": True,
                "task_name": social_task,
                "today_tasks": today_tasks,
                "total_tasks": task.total_tasks
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return render(request, "card_app/social_form.html", {"tasks": tasks, "form": SocialMediaForm()})


def social_activities(request):
    activities = SocialmediaActivity.objects.all().order_by('-timestamp')  # Fetch only logged activities
    return render(request, "card_app/social_activities.html", {"activities": activities})


def slides_form(request):
    tasks = SlidesTable.objects.all()

    if request.method == "POST":
        form = SlidesForm(request.POST)

        if form.is_valid():
            slides_task = form.cleaned_data['slides_tasks']
            today_tasks = form.cleaned_data['today_tasks']

            task, created = SlidesTable.objects.get_or_create(slides_tasks=slides_task)

            prev_today = task.today_tasks
            prev_total = task.total_tasks  

            task.today_tasks = today_tasks
            task.total_tasks += today_tasks  
            task.timestamp = timezone.now()
            task.save()

            if created:
                SlidesActivity.objects.create(
                    task=task, action="Added",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )
            elif prev_total != task.total_tasks:
                SlidesActivity.objects.create(
                    task=task, action="Modified",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )

            return JsonResponse({
                "success": True,
                "task_name": slides_task,
                "today_tasks": today_tasks,
                "total_tasks": task.total_tasks
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return render(request, "card_app/slides_form.html", {"tasks": tasks, "form": SlidesForm()})


def slides_activities(request):
    activities = SlidesActivity.objects.all().order_by('-timestamp')  # Fetch only logged activities

    return render(request, "card_app/slides_activities.html", {"activities": activities})

def others_form(request):
    tasks = OthersTable.objects.all()

    if request.method == "POST":
        form = OthersForm(request.POST)

        if form.is_valid():
            others_task = form.cleaned_data['other_tasks']
            today_tasks = form.cleaned_data['today_tasks']

            task, created = OthersTable.objects.get_or_create(other_tasks=others_task)

            prev_today = task.today_tasks
            prev_total = task.total_tasks  

            task.today_tasks = today_tasks
            task.total_tasks += today_tasks  
            task.timestamp = timezone.now()
            task.save()

            if created:
                OthersActivity.objects.create(
                    task=task, action="Added",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )
            elif prev_total != task.total_tasks:
                OthersActivity.objects.create(
                    task=task, action="Modified",
                    prev_today_tasks=prev_today,
                    prev_total_tasks=prev_total,
                    timestamp=timezone.now()
                )

            return JsonResponse({
                "success": True,
                "task_name": others_task,
                "today_tasks": today_tasks,
                "total_tasks": task.total_tasks
            })
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    return render(request, "card_app/others_form.html", {"tasks": tasks, "form": OthersForm()})



def others_activities(request):
    activities = OthersActivity.objects.all().order_by('-timestamp')  # Fetch only logged activities

    return render(request, "card_app/others_activities.html", {"activities": activities})

def update_task(request, task_id, task_type):
    # Determine the model and form dynamically
    model_mapping = {
        'news': (NewsTable, NewsForm, 'card_app:news_activities'),
        'magazine': (MagazineTable, MagazineForm, 'card_app:magazine_activities'),
        'socialmedia': (SocialmediaTable, SocialMediaForm, 'card_app:social_activities'),
        'slides': (SlidesTable, SlidesForm, 'card_app:slides_activities'),
        'others': (OthersTable, OthersForm, 'card_app:others_activities')
    }

    if task_type not in model_mapping:
        return redirect('card_app:index')  # Default redirection if task_type is invalid

    model, form_class, redirect_url = model_mapping[task_type]
    task = get_object_or_404(model, id=task_id)
    form = form_class(request.POST or None, instance=task)

    if request.method == 'POST' and form.is_valid():
        old_today_tasks = task.today_tasks  # Store old value for comparison
        old_total_tasks = task.total_tasks  

        # Save the updated task
        task.timestamp = timezone.now()
        form.save()

        # Log changes only if values were modified
        if old_today_tasks != task.today_tasks or old_total_tasks != task.total_tasks:
            NewsActivity.objects.create(task=task, action="Updated", timestamp=timezone.now())

        return redirect(redirect_url)

    return render(request, 'card_app/update_task.html', {'form': form, 'task': task})
    

