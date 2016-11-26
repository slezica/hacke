from django.conf import settings


def paginate(page):
    page = int(page)

    start = (page - 1) * settings.PAGE_SIZE
    end = start + settings.PAGE_SIZE

    return start, end

