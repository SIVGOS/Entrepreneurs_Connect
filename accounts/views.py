from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import entrepreneur
from django.db.models.fields import Field
# Create your views here.

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		if password1 != password2:
			messages.info(request,'The two passwords do not match')
			return render(request,'register.html',{'data':1, 'first_name':first_name, 'last_name':last_name , 'email': email,  'username': username})
		elif User.objects.filter(username = username):
			messages.info(request,'The user name is already taken')
			return render(request,'register.html',{'data':1, 'first_name':first_name, 'last_name':last_name , 'email': email,  'username': username})
		elif User.objects.filter(email = email):
			messages.info(request,'An account already exists with this email id. Please log in.')
			return render(request,'register.html',{'data':1, 'first_name':first_name, 'last_name':last_name , 'email': email,  'username': username})
		else:
			user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password1)
			messages.info(request,'Account Created. Please log in to create your profile.')
			return redirect('/accounts/login')
	else:
		return render(request, 'register.html',{'data': None})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username = username, password = password)
		
		if user is None:
			try:
				user1 = User.objects.get(email=username)
				user = auth.authenticate(username=user1.username, password = password)
			except:
				pass
		if user is not None:
			auth.login(request,user)
			print(user.email)
			if entrepreneur.objects.filter(user = user):
				return redirect('/')
			else:
				return redirect('edit_profile')
		else:
			messages.info(request,'Invalid credentials')
			return render(request,'login.html')
			
	else:
		return render(request,'login.html')

#login_required

@login_required(redirect_field_name='', login_url='/accounts/login')
def edit_profile(request):
	if request.method == 'GET':
		user = request.user
		if entrepreneur.objects.filter(user = user):
			ent_exist = True
		else:
			ent_exist = False
		return render(request, 'edit_profile.html',{'user':user, 'ent_exist':ent_exist})
	else:
		user = request.user
		if entrepreneur.objects.filter(user = user):
			ent_exist = True
		else:
			ent_exist = False
		city = request.POST['city']
		industry = request.POST['industry']
		intro = request.POST['intro']
		state = request.POST['state']
		country = request.POST['country']
		about = request.POST['about']
		if ent_exist:
			ent = user.entrepreneur
			ent.intro = intro
			ent.industry = industry
			ent.city = city
			ent.state = state
			ent.country = country
			ent.about = about

			if 'linkedin_url' in request.POST:
				ent.linkedin_url = request.POST['linkedin_url']
			if 'facebook_url' in request.POST:
				ent.facebook_url = request.POST['facebook_url']
			if 'instagram_url' in request.POST:
				ent.instagram_url = request.POST['instagram_url']

			if 'photo' in request.FILES:
				ent.photo = request.FILES['photo']
			if 'business_pic1' in request.FILES:
				ent.business_pic1 = request.FILES['business_pic1']
			if 'business_pic2' in request.FILES:
				ent.business_pic2 = request.FILES['business_pic2']
			if 'business_pic3' in request.FILES:
				ent.business_pic3 = request.FILES['business_pic3']
			if 'business_pic4' in request.FILES:
				ent.business_pic4 = request.FILES['business_pic4']
			if 'business_pic5' in request.FILES:
				ent.business_pic5 = request.FILES['business_pic5']

			if 'del_business_pic1' in request.POST:
				ent.business_pic1.delete()
			if 'del_business_pic2' in request.POST:
				ent.business_pic2.delete()
			if 'del_business_pic3' in request.POST:
				ent.business_pic3.delete()
			if 'del_business_pic4' in request.POST:
				ent.business_pic4.delete()
			if 'del_business_pic5' in request.POST:
				ent.business_pic5.delete()
			ent.save()
		else:
			ent = entrepreneur()
			ent.user = user
			ent.intro = intro
			ent.industry = industry
			ent.city = city
			ent.state = state
			ent.country = country
			ent.about = about

			if 'linkedin_url' in request.POST:
				ent.linkedin_url = request.POST['linkedin_url']
			if 'facebook_url' in request.POST:
				ent.facebook_url = request.POST['facebook_url']
			if 'instagram_url' in request.POST:
				ent.instagram_url = request.POST['instagram_url']

			if 'photo' in request.FILES:
				ent.photo = request.FILES['photo']
			if 'business_pic1' in request.FILES:
				ent.business_pic1 = request.FILES['business_pic1']
			if 'business_pic2' in request.FILES:
				ent.business_pic2 = request.FILES['business_pic2']
			if 'business_pic3' in request.FILES:
				ent.business_pic3 = request.FILES['business_pic3']
			if 'business_pic4' in request.FILES:
				ent.business_pic4 = request.FILES['business_pic4']
			if 'business_pic5' in request.FILES:
				ent.business_pic5 = request.FILES['business_pic5']
			ent.save()
		return redirect('/accounts/edit_profile')

def view_profile(request):
	user = request.user
	if entrepreneur.objects.filter(user = user):
		return redirect("profile")
	else:
		return HttpResponse("You don't have a profile")

def logout(request):
	auth.logout(request)
	return redirect('/')
