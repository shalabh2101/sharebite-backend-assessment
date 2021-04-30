from .models import Section
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_sections(request):
    if request.method == "GET":
        sections = Section.objects.all()
        return JsonResponse({
            "data": [i.serialize() for i in sections],
            "result": True,
            "message": "success",
        }, status=200)
