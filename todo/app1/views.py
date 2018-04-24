from django.shortcuts import render,redirect
from django.conf import settings
from .models import Todo

def index(request):
	user_list=''
	warning=''	
	user_session_id=''
	request.session.set_test_cookie()
	
	if request.COOKIES.get('sessionid', None):
		user_session_id =request.COOKIES[settings.SESSION_COOKIE_NAME]
	

	if(request.method == 'POST'):
		if user_session_id:
			
			text = request.POST['title']
			sess = user_session_id
			todo = Todo(text=text, sess=sess)
			todo.save()
			
			return redirect('index')

		
	
	
	if user_session_id:
		user_list= Todo.objects.filter(sess=user_session_id)
	else:
		warning='allow cookies'
	
	context={'list':user_list,'warning':warning}
	return render(request,'app1/index.html', context)
	
	
def update(request):
	if (request.method=='POST') :
		row = Todo.objects.get(id=request.POST['id'])
		row.complete=bool(request.POST['val'])
		row.save()
	
