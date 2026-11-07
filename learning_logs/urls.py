"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home pages
    path('', views.index, name='index'),
    # Page show all the topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding new topic.s
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry.
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Page for editting an entry.
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]