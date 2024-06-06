from django.shortcuts import render, redirect
from blog_app.models import Article
from django.http import Http404
from comments_app.forms import CommentForm
from comments_app.models import Comment
from django.contrib import messages

# Create your views here.

def article_list_view(request):
    template_name = "blog/article_list.html"
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, template_name, context)


def article_detail_view(request, *args, **kwargs):
    template_name = "blog/article_detail.html"
    pk = kwargs['pk']
    try:
        article = Article.objects.get(id=pk)
    except:
        raise Http404

    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            text = form.cleaned_data.get("text")

            new_comment = Comment.objects.create(article=article, name=name, text=text)
            if new_comment is not None:
                new_comment.save()
                messages.add_message(request, messages.SUCCESS, message="Your Comment is Submited.")
                return redirect(article.get_absolute_url())
            else:
                form.add_error('text', 'somthing wraong, please try again!')
             
    else:
        form = CommentForm()

    context = {
        'article': article,
        'form': form
    }
    return render(request, template_name, context)