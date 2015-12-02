"""
Definition of views.
"""

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from django.template import RequestContext, loader
from django.http import HttpResponse
from datetime import datetime
from .models import MyViewModel

from .models import Post
from django.http import JsonResponse
from django.core import serializers
#from forms import PostForm

import json

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def MyViewXX(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/User.html',
        query_results = MyViewModel.objects.all()
    )

def MyView(request):
    query_results = MyViewModel.objects.all()
    template = loader.get_template('app/User.html')
    context = RequestContext(request, {
        'title':'Cengiz View',
        'query_results': query_results,
    })
    return HttpResponse(template.render(context))


def edit_favorites(request):
    if request.is_ajax():
        message = "Yes, AJAX!"
    else:
        message = "Not Ajax"
    context = RequestContext(request, {
        'message':message,
        'query_results': query_results,
    })
    return HttpResponse(render(context))

@csrf_exempt
def create_post(request):
    if request.method == 'POST':
            post_text = request.POST.get('the_post')
            response_data = {}

            post = Post(text=post_text, author=request.user)
            #post.save()
            post.save()
            response_data['result'] = 'Create post successful!'
            response_data['postpk'] = post.pk
            response_data['text'] = post.text
            response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
            response_data['author'] = post.author.username

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )
    #if request.method == 'POST':
    #    post_text = request.POST.get('the_post')
    #    response_data = {}

    #    post = Post(text=post_text, author=request.user)
    #    post.save()

    #    response_data['result'] = 'Create post successful!'
    #    response_data['postpk'] = post.pk
    #    response_data['text'] = post.text
    #    response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
    #    response_data['author'] = post.author.username

    #    return HttpResponse(
    #        json.dumps(response_data),
    #        content_type="application/json"
    #    )
    #else:

        #post_text = request.POST.get('the_post')
        #response_data = {}

        #post = Post(text=post_text, author=request.user)
        #post.save()

        #response_data['result'] = 'Create post successful!'
        #response_data['postpk'] = post.pk
        #response_data['text'] = post.text
        #response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
        #response_data['author'] = post.author.username

        #return HttpResponse(
        #    json.dumps(response_data),
        #    content_type="application/json"
        #)

    #if request.is_ajax():
    #    message = "Yes, AJAX!"
    #else:
    #    message = "Not Ajax"
    #context = RequestContext(request, {
    #    'message':message
    #})
    #return HttpResponse(message)
    #return HttpResponse(render(context))
#    return render_to_response('hello from py',  {'errors': errors}, context_instance=RequestContext(request))  
    #return a response to your template and add query_results to the context

@csrf_exempt
def load_post_data(request):
    if request.method == 'POST':

            posts = Post.objects.all()
            #post_text = request.POST.get('the_post')
            #response_data = {}

            #post = Post(text=post_text, author=request.user)

            #response_data['result'] = 'Create post successful!'
            #response_data['postpk'] = post.pk
            #response_data['text'] = post.text
            #response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
            #response_data['author'] = post.author.username
            data = serializers.serialize("json", posts)
            return HttpResponse(data, content_type='application/json')
            #return JsonResponse(posts)
    #        return HttpResponse(
    #            json.dumps(posts),
    #            content_type="application/json"
    #        )
    #else:
    #        return HttpResponse(
    #            json.dumps({"nothing to see": "this isn't happening"}),
    #            content_type="application/json"
    #        )