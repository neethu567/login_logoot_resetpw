from django.urls import path
from.import views
app_name='polls'
urlpatterns=[
    # path('',views.IndexView.as_view(),name='index'),
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('setpassword/', views.set_password, name='set_password'),

    path('login-handle/', views.login_handle, name='index_handle'),
    path('password-handle/', views.password_handle, name='password_handle'),

    path('polls/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    # path('logout/', views.logout_view, name='logout'),

]