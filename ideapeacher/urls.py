from django.urls import path
from . import views
app_name = "ideapeacher"
urlpatterns = [

	path('peacher/', views.registerPeacher, name="register" ),
	path('login_request/',views.login_request,name="login_request" ),
	path('home/',views.ideapeacherpage,name="home" ),
	path('logout_request/',views.logout_request,name="logout" ),
	path('home_sponser/',views.sponserPage,name="home_sponser"),
	path('submitidea/',views.submitidea,name="submitidea"),
	path('idea/',views.post,name="post"),
	path("comment/<int:pk>/",views.comment,name="comment"),
	path("edit_idea/<int:pk>/",views.edit_idea,name="edit_idea"),
	path("updateidea/<int:pk>/",views.updateidea,name="updateidea"),
	path("deleteidea/<int:pk>/",views.deleteidea,name="deleteidea"),

]
