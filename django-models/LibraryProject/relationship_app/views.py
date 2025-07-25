from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Authentication views
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list_books')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
 
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

# Role-checking helper
def check_role(user, role_name):
    return hasattr(user, 'userprofile') and user.userprofile.role == role_name

def admin_required(user):
    return check_role(user, 'Admin')

def librarian_required(user):
    return check_role(user, 'Librarian')

def member_required(user):
    return check_role(user, 'Member')

@login_required
@user_passes_test(admin_required)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(librarian_required)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(member_required)
def member_view(request):
    return render(request, 'member_view.html')
