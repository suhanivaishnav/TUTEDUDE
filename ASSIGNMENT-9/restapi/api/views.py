from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        student = Student.objects.create(name=name, age=age)
        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "age": student.age
        }, status=201)

@csrf_exempt
def student_detail(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student not found"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": student.id,
            "name": student.name,
            "age": student.age
        })