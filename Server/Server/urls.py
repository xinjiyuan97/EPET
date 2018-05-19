"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from users import views as userViews
from experiment import views as experimentViews
from lessons import views as lessonsViews
from basicPages import views as basicViews
urlpatterns = [
    url(r'^register/varify/$', userViews.varify),
    url(r'^api/users/$', userViews.UsersList.as_view()),
    url(r'^api/userinfo/$', userViews.UserInfoList.as_view()),
    url(r'^api/register/completeInfo/(?P<id>[0-9]+)/$', userViews.CompleteUserInfo.as_view()),
    url(r'^api/register/$', userViews.UserRegister.as_view()),
    url(r'^api/login/$', userViews.UserLogin.as_view()),
    
    url(r'^admin/', admin.site.urls),
    
    url(r'^api/experiment/add/', experimentViews.AddExperiment.as_view()),
    url(r'^api/experiment/all/', experimentViews.ShowAllExperiments.as_view()),
    url(r'^api/experiment/(?P<id>[0-9]+)/$', experimentViews.ShowExperiment.as_view()),

    url(r'^api/lessons/add/', experimentViews.AddALesson.as_view()),
    url(r'^api/lessons/update/(?P<id>[0-9]+)/$', experimentViews.UpdateLessons.as_view()),
    url(r'^api/lessons/list/', experimentViews.ListAllLessons.as_view()),
    # url(r'^api/lessons/list/', experimentViews.ListRunningLessons.as_view())

    url(r'^api/lab/register/', lessonsViews.ServerRegister.as_view()),
    url(r'^api/lab/update/(?P<id>[0-9]+)/$', lessonsViews.ServerUpdate.as_view()),
    url(r'^api/lab/list/', lessonsViews.ServerList.as_view()),

    url(r'^api/student/request/', lessonsViews.SendStudentRequest.as_view()),
    url(r'^api/student/list/', lessonsViews.ListUndoStudentRequest.as_view()),
    url(r'^api/student/update/', lessonsViews.FillStudentRequest.as_view()),
    url(r'^api/student/get/', lessonsViews.GetRespond.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', basicViews.home, name = 'home'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

handler403 = basicViews.permissionDenied
handler404 = basicViews.pageNotFound
handler500 = basicViews.pageError
