from django.urls import path 
from.views       import DuplicationView,SignUpView,SignInView

urlpatterns = [
    path('/check',DuplicationView.as_view()),
    path('/sign_up',SignUpView.as_view()),
    path('/sign_in',SignInView.as_view()),
]