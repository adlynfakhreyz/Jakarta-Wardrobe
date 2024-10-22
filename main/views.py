from django.shortcuts import render, redirect
from main.models import ItemEntry, Rating, Rate
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from main.forms import RatingForm
import uuid


# Create your views here.
def show_main(request):
    return render(request, 'main.html')

# def show_reviews(request, id):
#     item = ItemEntry.objects.get(pk=id)

#     reviews = ItemEntry.objects.filter(item=item)
#     context = {
#         'item': item,
#         'reviews': reviews
#     }
#     return render(request, 'main.html', context)


# def add_rating_ajax(request, id):
#     item = ItemEntry.objects.get(pk=id)
#     user = request.user

#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             rating = form.save(commit=False)
#             rating.user_id = request.user
#             rating.product_id = ItemEntry.objects.get(id=request.POST['product_id'])
#             rating.save()
#             return redirect('main:show_main')
#     return redirect('main:show_main')

@login_required(login_url='login')
def product_details(request,imdb_id):
    if Movie.objects.filter(imdbID=imdb_id).exists():
        movie_data=Movie.objects.get(imdbID=imdb_id)
        reviews = Review.objects.filter(movie=movie_data)
        if Review.objects.filter(movie=movie_data,user=request.user).exists():
            reviewed=True
        else:
            reviewed=False
        reviews_avg = reviews.aggregate(Avg('rate'))
        if Review.objects.filter(movie=movie_data).exists():
            reviews_count = reviews.count()
        else:
            reviews_count=0
        our_db=True
    else:
        url='http://www.omdbapi.com/?apikey=c9161d22&i='+imdb_id
        response=requests.get(url, timeout=3)
        movie_data=response.json()

        #inject
        rating_objs=[]
        genre_objs=[]
            
        #genre
        genre_list=list(movie_data['Genre'].replace(" ","").split(','))
        for genre in genre_list:
            genre_slug=slugify(genre)
            g,created=Genre.objects.get_or_create(title=genre,slug=genre_slug)
            genre_objs.append(g)
        
        #Rate
        for rate in movie_data['Ratings']:
            r,created=Rating.objects.get_or_create(source=rate['Source'],rating=rate['Value'])
            rating_objs.append(r)

        #Language
        language_list=[x.strip() for x in movie_data['Language'].split(',')]
        if language_list[0] == 'Hindi':
            genre_slug=slugify("Bollywood")
            g,created=Genre.objects.get_or_create(title="Bollywood",slug=genre_slug)
            genre_objs.append(g)
        elif language_list[0] == 'English':
            genre_slug=slugify("Hollywood")
            g,created=Genre.objects.get_or_create(title="Hollywood",slug=genre_slug)
            genre_objs.append(g)
        elif language_list[0] == 'Tamil':
            genre_slug=slugify("Kollywood")
            g,created=Genre.objects.get_or_create(title="Kollywood",slug=genre_slug)
            genre_objs.append(g)
        elif  language_list[0] == 'Telugu':
            genre_slug=slugify("Tollywood")
            g,created=Genre.objects.get_or_create(title="Tollywood",slug=genre_slug)
            genre_objs.append(g)
        elif language_list[0] == 'Kannada':
            genre_slug=slugify("Sandalwood")
            g,created=Genre.objects.get_or_create(title="Sandalwood",slug=genre_slug)
            genre_objs.append(g)
        else:
            genre_slug=slugify("Others")
            g,created=Genre.objects.get_or_create(title="Others",slug=genre_slug)
            genre_objs.append(g)
        
        if language_list[0] == 'Japanese' and genre_list[0] == 'Animation' and movie_data['Type'] == 'series':
            genre_slug=slugify("Anime")
            g,created=Genre.objects.get_or_create(title="Anime",slug=genre_slug)
            genre_objs.append(g)

        m,created=Movie.objects.get_or_create(
            Title=movie_data['Title'],
            Year=movie_data['Year'],
            Rated=movie_data['Rated'],
            Released=movie_data['Released'],
            Runtime=movie_data['Runtime'],
            Actors=movie_data['Actors'],
            Director=movie_data['Director'],
            Writer=movie_data['Writer'],
            Plot=movie_data['Plot'],
            Language=movie_data['Language'],
            Country=movie_data['Country'],
            Metascore=movie_data['Metascore'],
			imdbRating=movie_data['imdbRating'],
            Awards=movie_data['Awards'],
            Poster_url=movie_data['Poster'],
            Type=movie_data['Type'],
            imdbID=movie_data['imdbID'],
        )
        m.Genre.set(genre_objs)
        m.Ratings.set(rating_objs)
        m.save()
        our_db=False
        reviewed=False
        movie_data_2=Movie.objects.get(imdbID=imdb_id)
        reviews = Review.objects.filter(movie=movie_data_2)
        reviews_avg='N/A'
        reviews_count=0

    context={
        'movie_data':movie_data,
        'our_db':our_db,
        'reviews':reviews,
        'reviews_avg':reviews_avg,
        'reviews_count':reviews_count,
        'reviewed':reviewed,
    }
    template=loader.get_template('MovieDetailsPage.html')
    return HttpResponse(template.render(context,request))

def Rate(request, imdb_id):
    movie = Movie.objects.get(imdbID=imdb_id)
    user = request.user
    if request.method == 'POST': 
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.movie = movie
            rate.save()
            return HttpResponseRedirect (reverse('movie-details', args=[imdb_id]))
    else:
        form = RateForm()
    template = loader.get_template('rate.html')
    context = {
        'form': form,
        'movie': movie,
    }
    return HttpResponse(template.render(context, request)) 