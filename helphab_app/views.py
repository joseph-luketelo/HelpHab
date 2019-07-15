from django.shortcuts import render
from .forms import SubscriberForm, QuestionsForm, LoginForm
from django.contrib.auth.models import User
from .models import Subscriber, QuestionsTable, Room, Message
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseForbidden

def chat_room(request, label):
    # If the room with the given label doesn't exist, automatically create it
    # upon first visit (a la etherpad).
    room, created = Room.objects.get_or_create(label=label)

    # We want to show the last 50 messages, ordered most-recent-last
    messages = reversed(room.messages.order_by('-timestamp')[:50])

    return render(request, "helphab_app/room.html", {
        'room': room,
        'messages': messages,
    })

def home_view(request):
    return render(request, 'helphab_app/home.html')

@login_required()
def questions_list_view(request, template='helphab_app/questions.html'):
    quiz_list = QuestionsTable.objects.all()
    variables = {
        "details": quiz_list
    }
    return render(request, 'helphab_app/questions_list.html', variables)
    # return render(request, 'helphab_app/questions_list.html', {'quiz': quiz_list})

@login_required()
def questions_view(request, template='helphab_app/questions.html'):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        # form = QuestionsForm(request.POST, request.FILES)
        if form.is_valid():
            # Unpack form values
            question_title = form.cleaned_data['question_title']
            question_details = form.cleaned_data['question_details']
            budget = form.cleaned_data['budget']
            field = form.cleaned_data['field']
            deadline = form.cleaned_data['deadline']
            email_address = form.cleaned_data['email_address']
            # upload_files = request.FILES['upload_files']
            user = request.user
            ques = QuestionsTable(question_title=question_title, question_details=question_details, budget=budget,
                                  field=field, deadline=deadline, email_address=email_address, user_rec=user)
            ques.save()
            return HttpResponse("Data saved")
        else:
            return HttpResponse("Form not valid")
    else:
        form = QuestionsForm()
    return render(request, template, {'form': form})

@login_required()
def messages_view(request, template='helphab_app/questions.html'):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            # Unpack form values
            question_title = form.cleaned_data['question_title']
            question_details = form.cleaned_data['question_details']
            budget = form.cleaned_data['budget']
            deadline = form.cleaned_data['deadline']
            field = form.cleaned_data['field']
            urgency = form.cleaned_data['urgency']
            # ques = Subscriber(question_title=question_title, question_details=question_details,
            #                  budget=budget, deadline=deadline, field=field, urgency=urgency, user_rec=User)
            # ques.save()
            return HttpResponse("form working")
    else:
        form = QuestionsForm()
    return render(request, template, {'form': form})


def signup(request, template='helphab_app/signup.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Create the User record
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one=address_one, address_two=address_two,
                             city=city, state=state, user_rec=user)
            sub.save()
            return HttpResponse("Registrations successful")
    else:
        form = SubscriberForm()
    return render(request, template, {'form': form})


def login_view(request,  template='helphab_app/login.html'):
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
    user = authenticate(request, username=username, password=password)
    if request.method == 'POST':
        if user is not None:
            login(request, user)
            return render(request, "helphab_app/index.html")
        else:
            return HttpResponse("login failed")
    else:
        form = LoginForm()
    return render(request, template, {'form': form})


def logout_view(request):
    logout(request)
    return render(request, "helphab_app/login.html")