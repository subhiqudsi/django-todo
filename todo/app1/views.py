from django.shortcuts import render,redirect


from django.conf import settings
from .models import Todo

def index(request):
	# Its not secure to do it this way, but within the specified timeframe its impossible to learn Django REST + backbone.js
	test=""
	request.session.set_test_cookie()
	if request.COOKIES.get('sessionid', None):
		test =request.COOKIES[settings.SESSION_COOKIE_NAME]
	
	warning=''
	
	
	
	if not test:
			warning='allow cookies'
		
	if(request.method == 'POST') and test:
		text = request.POST['title']
		sess = test

		todo = Todo(text=text, sess=sess)
		todo.save()

		return redirect('index')
	
	
	if test:
		mylist= Todo.objects.filter(sess=test)
	else:
		mylist=""
	
	context={'list':mylist,'warning':warning}
	return render(request,'app1/index.html', context)