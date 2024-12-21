from django.urls import path
from user_choices.views import show_user_choices, show_user_choices_json, add_user_choices, delete_user_choices, edit_notes, edit_notes_flutter

app_name = 'user_choices'

urlpatterns = [
    path('', show_user_choices, name='show_user_choices'),
    path('add_user_choices/<uuid:id>', add_user_choices, name='add_user_choices'),
    path('delete_user_choices/<uuid:id>', delete_user_choices, name='delete_user_choices'),
    path('json/', show_user_choices_json, name='show_user_choices_json'),
    path('edit_notes/<uuid:id>', edit_notes, name='edit_notes'),
    path('edit_notes_flutter/<uuid:id>', edit_notes_flutter, name='edit_notes_flutter'),
]