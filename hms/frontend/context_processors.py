from django.conf import settings

def main_images_dir(request):
    return {'MEDIA_URL': settings.MEDIA_URL}
