from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def simple_timesince(value):
    # Gunakan timesince untuk menghitung waktu yang telah berlalu
    time_ago = timesince(value)
    # Ambil hanya unit waktu pertama (menit, jam, hari, minggu)
    return time_ago.split(',')[0]
