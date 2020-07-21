from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import entrepreneur
from django.contrib.auth.models import User
# Create your views here.
def home(request):
	ents = entrepreneur.objects.all()
	#print(ents)
	return render(request,'home.html',{'ents':ents})

def profile(request):
	if 'id' in request.GET:
		username = request.GET['id']
		user = User.objects.get(username=username)
		if request.user == user:
			is_owner = True
		else:
			is_owner = False
	else:
		user = request.user
		is_owner = True
	print(user)
	ent = user.entrepreneur
	desc_paras = ent.about.split('\n')
	num_pics = 5
	pic_urls = []
	try:
		pic_urls.append(ent.business_pic1.url)
	except:
		num_pics-=1
	try:
		pic_urls.append(ent.business_pic2.url)
	except:
		num_pics-=1
	try:
		pic_urls.append(ent.business_pic3.url)
	except:
		num_pics-=1
	try:
		pic_urls.append(ent.business_pic4.url)
	except:
		num_pics-=1
	try:
		pic_urls.append(ent.business_pic5.url)
	except:
		num_pics-=1
	return render(request,'view_profile.html',{'ent':ent, 'desc_paras': desc_paras,'is_owner':is_owner, 'pic_urls':pic_urls})
	
def search(request):
	if request.method == 'POST':
		keyword = request.POST['keyword']
		keywords = keyword.split(' ')
		results = []
		for kw in keywords:
			first_name_key = (User.objects.filter(first_name__iexact=kw))
			for fnk in first_name_key:
				results.append(fnk.entrepreneur)
			last_name_key = (User.objects.filter(last_name__iexact=kw))
			for lnk in last_name_key:
				results.append(lnk.entrepreneur)
			results.extend(entrepreneur.objects.filter(intro__icontains=kw))
			results.extend(entrepreneur.objects.filter(industry__icontains=kw))
			results.extend(entrepreneur.objects.filter(city__icontains=kw))
			results.extend(entrepreneur.objects.filter(state__icontains=kw))
			results.extend(entrepreneur.objects.filter(country__icontains=kw))
		results = list(dict.fromkeys(results))
		user = User.objects.get(username="sivgos")
		ent = user.entrepreneur
		return render(request,"search.html", {"result_available": len(results), "results": results})
	else:
		return render(request,"search.html",{"result_available": -1, "results": []})
