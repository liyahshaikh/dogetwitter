import random
from django.http import HttpResponse, Http404,JsonResponse
from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>What color is a sunflower?<br>Yellllloow!</h1>")
    return render(request, "pages/home.html", context={}, status=200 )

def tweet_create_view(request, *args,**kwargs):
    form=TweetForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        form= TweetForm()
    return render(request, "components/form.html", context={"form":form})
    

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript/java/swift/iOS/Android
    """
    queryList = Tweet.objects.all()
    tweet_list = [{'id': tweet.id, 'content': tweet.content, 'likes':random.randint(0,120)} for tweet in queryList]
    data={
        'response':tweet_list
    }
    return JsonResponse(data)
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript/java/swift/iOS/Android
    """
    data={
        "id":tweet_id,
        # "content": obj.content,
        # #image here later once we figure out how to store it :)
        
    }
    status=200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['message']="Not Found"
        status=404
    
    return JsonResponse(data, status=status) #json.dumps content_type='application/json'
    
