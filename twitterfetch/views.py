from django.shortcuts import render
from django.utils import timezone
from .models import Hashtag
from .forms import HashtagForm
from django.shortcuts import redirect

# Create your views here.
def hashtag_list(request):
  hashtags = Hashtag.objects.order_by('created_date')
  if request.method == "POST":
    form = HashtagForm(request.POST)
    if form.is_valid():
      hashtag = form.save(commit=False)
      hashtag.save()
      return render(request, 'hashtag_list.html', {'hashtags': hashtags})
    else:
      return render(request, 'hashtag_list.html', {'hashtags': hashtags})
  else:
    form = HashtagForm()
    return render(request, 'hashtag_list.html', {'hashtags': hashtags})