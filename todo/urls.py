from django.urls import path
from . import views

urlpatterns = [
    #add task
    path("addTask/", views.addTask, name="addTask"),
    #mark as done
    path("mark_as_done/<int:pk>/",views.mark_as_done, name="mark_as_done"),
    # mark as undone
    path("mark_as_Undone/<int:pk>/",views.mark_as_Undone, name = 'mark_as_Undone'),
    # Edit feature
    path("Edit_task/<int:pk>/", views.Edit_task, name = 'Edit_task'),
    #Delete feature
    path("Delete_task/<int:pk>/", views.Delete_task, name = 'Delete_task'),
]