from django.shortcuts import render,redirect
from app.models import Album,Song


# Create your views here.
def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def albums(request):
	albums = Album.objects.all()
	return render(request,'albums.html',{ 'albums':albums})

def songs(request):
	songs = Song.objects.all()
	return render(request,'songs.html',{ 'songs':songs})



#ndio hii io io view
def newalbum(request):
	return render(request,'addalbum.html')



def addalbum(request):
	a = request.GET['artist']
	b = request.GET['album_title']
	c = request.GET['genre']
	d = request.GET['album_logo']
	album = Album.objects.create(
		artist =a,
		genre = c,
		album_logo = d,
		album_title = b
		)
	album.save()
	return redirect('albums')

def newsong(request,pk):
	return render(request,'newsong.html')


def addsong(request,pk):
	album = get_object_or_404(Album,pk=pk)
	song_type = request.GET['song_type']
	song_title = request.GET['song_title']
	song = Song.objects.create(
		album = album,
		song_type = song_type,
		song_title = song_title
		)
	song.save()
	redirect('albumflani',pk=pk)
	return render(request,'newsong.html')

def albumflani(request,pk):
	#album = get_object_or_404(Album,pk=pk)
	#producer = get_object_or_404(Producer,pk=pk)
	#actors = Actor.objects.select_related().filter(programme = programme_id)
	album = Album.objects.get(id=pk)
	songs = Song.objects.select_related().filter(album_id=pk)
	return render(request,'albumflani.html',{'album':album,'songs':songs})