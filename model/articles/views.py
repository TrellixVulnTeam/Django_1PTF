from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    # 모델을 이용해서 모든 데이터를 가져온다
    articles = Article.objects.order_by('-pk')

    #가져온 데이터를 템플릿으로 넘긴다
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 데이터 저장하기
    article = Article(title=title, content=content)
    article.save()
    
    # return redirect('articles:index')
    # 인덱스 대신 detail로 가자
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    # articles 변수에 글 하나를 가져와서 할당해주세요
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
     # 1. pk 에 해당하는 글을 데이터베이스에서 가져옴
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # 2. 해당 글을 삭제한다
        article.delete()
        # 3. 삭제 하고 나면 index 페이지로 이동하게 한다
        return redirect('articles:index')
    else:
        return redirect('article:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 수정할 article을 가져온다
    article = Article.objects.get(pk=pk)
    # request로부터 사용자가 입력한 데이터를 가져온다 + 수정한다
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    # article 상세페이지로 보낸다
    return redirect('articles:detail', article.pk)