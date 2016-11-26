from django.conf import settings


def paginate(page=None):
    page = int(page or 1) # in case it's a string, from a URL

    start = (page - 1) * settings.PAGE_SIZE
    end = start + settings.PAGE_SIZE

    return start, end

