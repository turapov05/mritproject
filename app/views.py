from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Index
from .forms import IndexForm  # Create a form for your Index model

# List View
def index_list(request):
    index = Index.objects.all()
    context = {
        'index': index
    }
    return render(request, 'index_list.html', context)

# Detail View
def index_detail(request, pk):
    index = get_object_or_404(Index, pk=pk)
    contex = {
        'index': index
    }
    return render(request, 'index_detail.html', contex)
# Create View
@require_http_methods(["GET", "POST"])
def index_create(request):
    if request.method == "POST":
        form = IndexForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Index created successfully.")
            return redirect('index_list')
    else:
        form = IndexForm()
    return render(request, 'index.form.html', {'form': form})

# Update View
@require_http_methods(["GET", "POST"])
def index_update(request, pk):
    index = get_object_or_404(Index, pk=pk)
    if request.method == "POST":
        form = IndexForm(request.POST, request.FILES, instance=index)
        if form.is_valid():
            form.save()
            messages.success(request, "Index updated successfully.")
            return redirect('index_list')
    else:
        form = IndexForm(instance=index)
    return render(request, 'index.form.html', {'form': form})

# Delete View
@require_http_methods(["GET", "POST"])
def index_delete(request, pk):
    index = get_object_or_404(Index, pk=pk)
    if request.method == "POST":
        index.delete()
        messages.success(request, "Index deleted successfully.")
        return redirect('index_list')
    return render(request, 'index_confirm_delete.html', {'index': index})