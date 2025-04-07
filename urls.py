from django.urls import path
from .views import *

urlpatterns = [
    path("students/", StudentListCreate.as_view()),
    path("students/<int:pk>/", StudentDetail.as_view()),
    # path('teachers/', TeacherListCreate.as_view()), #FIXME
    # 其他路由...
]
