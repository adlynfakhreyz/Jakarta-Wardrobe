from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Article
from django.views.decorators.http import require_GET

@require_GET
def list_articles(request):
    articles = Article.objects.all().order_by('-timestamp')
    articles_data = [
        {
            "uuid": str(article.uuid),
            "title": article.title,
            "user": article.user.username,
            "content": article.content,
            "image_url": article.image_url,
            "timestamp": article.timestamp.strftime('%d %B %Y, %H:%M')
        }
        for article in articles
    ]
    return JsonResponse(articles_data, safe=False)

@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, uuid=article_id)
    return JsonResponse({
        "uuid": str(article.uuid),
        "title": article.title,
        "user": article.user.username,
        "content": article.content,
        "image_url": article.image_url,
        "timestamp": article.timestamp.strftime('%d %B %Y, %H:%M')
    })

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Article
import json

@login_required
@csrf_exempt
def add_article(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')
            image_url = data.get('image_url')

            # Validasi input
            if not all([title, content, image_url]):
                return JsonResponse({"status": "error", "message": "Missing fields"}, status=400)

            # Buat artikel baru, user diambil dari request.user
            article = Article.objects.create(
                title=title,
                content=content,
                image_url=image_url,
                user=request.user
            )

            return JsonResponse({
                "status": "success",
                "message": "Article added successfully",
                "article_id": str(article.uuid),
                "user": request.user.username
            }, status=201)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Article  # Pastikan model Article diimpor

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Article


@csrf_exempt
@login_required
def delete_article(request, article_id):
    if request.method == 'POST':
        try:
            article = get_object_or_404(Article, uuid=article_id)

            # Pastikan hanya penulis yang bisa menghapus
            if request.user != article.user:
                return JsonResponse(
                    {'message': 'You are not allowed to delete this article'}, 
                    status=403
                )

            article.delete()
            return JsonResponse({'message': 'Article deleted successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

from django.utils.timezone import now
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Article

