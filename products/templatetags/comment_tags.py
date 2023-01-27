from django.template import Library

register = Library()


@register.filter()
def filter_comment(comment):
    return comment.filter(active=True)


@register.filter()
def count_comment(comment):
    return filter_comment(comment).count()

