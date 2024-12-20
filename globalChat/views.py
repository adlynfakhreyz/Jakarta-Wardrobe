from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Forum, Comment
from .forms import ForumForm, CommentForm
from django.http import JsonResponse
from django.db.models import Count

# Global Chat: List all forums with pagination
def global_chat(request):
    filter_option = request.GET.get('filter', 'newest')

    # Check if user is authenticated before filtering by user-specific attributes
    if not request.user.is_authenticated:
        # Redirect to login if trying to access user-specific filters while not logged in
        if filter_option in ['your_posts', 'saved']:
            return redirect('main:login')

    if filter_option == 'your_posts':
        # Filter forums by the current user
        forums_list = Forum.objects.filter(user=request.user).order_by('-posted_time')
    elif filter_option == 'most_likes':
        # Sort forums by likes count in descending order
        forums_list = Forum.objects.annotate(num_likes=Count('likes')).order_by('-num_likes', '-posted_time')
    elif filter_option == 'saved':
        # Filter forums that are bookmarked by the current user
        forums_list = Forum.objects.filter(bookmarks=request.user).order_by('-posted_time')
    else:
        # Default to newest posts (all posts)
        forums_list = Forum.objects.all().order_by('-posted_time')

    paginator = Paginator(forums_list, 5)  # Show 5 forums per page
    page_number = request.GET.get('page')
    forums = paginator.get_page(page_number)

    context = {
        'forums': forums,
        'filter_option': filter_option,  # Pass the current filter to the template
    }
    return render(request, 'global_chat.html', context)

# Forum Detail View
@login_required(login_url="main:login")
def detail_chat(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    comments = Comment.objects.filter(forum=forum).order_by('-posted_time')
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forum = forum
            comment.user = request.user  # Menyimpan user yang berkomentar
            comment.save()
            return redirect('globalChat:detail_chat', forum_id=forum.id)
    else:
        form = CommentForm()

    context = {
        'forum': forum,
        'comments': comments,
        'form': form,
    }
    return render(request, 'detail_chat.html', context)

# Create a new forum post
@login_required(login_url="main:login")
def new_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.user = request.user  # Set current logged-in user
            forum.save()
            return redirect('globalChat:global_chat')  # Redirect to global_chat after submit
        else:
            print(form.errors)  # Cetak errors untuk debugging
    else:
        form = ForumForm()

    return render(request, 'new_forum.html', {'form': form})


@login_required(login_url="main:login")
def toggle_like_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.user in forum.likes.all():
        forum.likes.remove(request.user)
        liked = False
    else:
        forum.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'like_count': forum.likes.count()})

@login_required(login_url="main:login")
def edit_forum(request, id):
    forum = get_object_or_404(Forum, id=id)
    if request.user != forum.user:
        return redirect('globalChat:global_chat')  # Redirect jika bukan pembuat forum

    if request.method == 'POST':
        form = ForumForm(request.POST, instance=forum)
        if form.is_valid():
            form.save()
            return redirect('globalChat:detail_chat', forum.id)
    else:
        form = ForumForm(instance=forum)
    
    return render(request, 'edit_forum.html', {'form': form, 'forum': forum})

@login_required(login_url="main:login")
def delete_forum(request, id):
    forum = get_object_or_404(Forum, id=id)
    if request.user == forum.user:
        forum.delete()
    return redirect('globalChat:global_chat')

@login_required(login_url="main:login")
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    forum = get_object_or_404(Forum, id=comment.forum.id)

    # Check if the logged-in user is either the comment owner or the forum owner
    if comment.user == request.user or forum.user == request.user:
        comment.delete()
        return redirect('globalChat:detail_chat', forum_id=forum.id)  # Redirect to the forum post after deleting the comment
    else:
        return redirect('globalChat:detail_chat', forum_id=forum.id)  # If not authorized, redirect back
    
@login_required(login_url="main:login")
def toggle_bookmark(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    if request.user in forum.bookmarks.all():
        forum.bookmarks.remove(request.user)
        bookmarked = False
    else:
        forum.bookmarks.add(request.user)
        bookmarked = True
    return JsonResponse({'bookmarked': bookmarked})

#test