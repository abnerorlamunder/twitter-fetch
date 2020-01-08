import requests
from django.shortcuts import render
from django.utils import timezone
from .models import Hashtag
from .forms import HashtagForm
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView
import tweepy
from django.urls import reverse_lazy

# Create your views here.
def hashtag_list(request):
  hashtags = Hashtag.objects.order_by('created_date')

  auth = tweepy.OAuthHandler("IOBoByzw7sXqXe8zrSBL4Iyvq", "4DEC0VOGuevexfBTfy2bERIX8fRQtX5kGQPZ6Nhz3rxupgrb5c")
  auth.set_access_token("1191824923301482501-Hr3h5O0QtIt7ONdMEvbPMMhRca4iuE", "1uf2tlpLCmQwwkT2zxVWcOtPTExSkm4TyjPvwqSYvR79y")

  api = tweepy.API(auth)

  hashtags_string = ""
  for i in range(len(hashtags)):
    if i != 0:
      hashtags_string += ","
    hashtags_string += hashtags[i].text

  if hashtags_string != "":
    tweets = api.search(hashtags_string, lang="en", rpp=100, result_type="recent", wait_on_rate_limit=True)
  else:
    tweets = []

  if request.method == "POST":
    form = HashtagForm(request.POST)
    if form.is_valid():
      hashtag = form.save(commit=False)
      hashtag.save()

      return render(request, 'hashtag_list.html', {'hashtags': hashtags, 'tweets': tweets})
    else:
      return render(request, 'hashtag_list.html', {'hashtags': hashtags, 'tweets': tweets})
  else:
    form = HashtagForm()
    return render(request, 'hashtag_list.html', {'hashtags': hashtags, 'tweets': tweets})

class HashtagDelete(DeleteView):
    model = Hashtag
    success_url = reverse_lazy('hashtag_list')