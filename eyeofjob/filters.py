from django import template

register = template.Library()

@register.filter
def split_names(participants):
    return participants.split(',')