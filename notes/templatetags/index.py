from django import template

register = template.Library()


def count_notes(notes):
    return len(notes)

register.filter('count_notes', count_notes)