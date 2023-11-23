from django.urls import path
from cards import views
urlpatterns = [
    path('create/', views.CreateFlashCardView.as_view(), name='create'),
    path('update/<id>/', views.UpdateFlashCardView.as_view(), name='update'),
    path('list/<user_id>/', views.FlashCardListView.as_view(), name='list'),
]
