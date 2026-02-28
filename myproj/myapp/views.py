from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Person
import json

def person_list(request):
    persons = Person.objects.all()
    xml = '<persons>'   
    for p in persons:
        xml += f'<person><id>{p.id}</id><name>{p.name}</name></person>'
    xml += '</persons>'
    return HttpResponse(xml, content_type='application/xml')


@csrf_exempt 
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        person = Person.objects.create(name=data['name'], address=data['address'])
        return HttpResponse(json.dumps({"name": person.name, "address": person.address}), content_type="application/json")

@csrf_exempt
def update(request, id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        person = Person.objects.get(id=id)
        person.name = data['name']
        person.address = data['address']
        person.save()
        return HttpResponse(json.dumps({"name": person.name, "address": person.address}), content_type="application/json")

@csrf_exempt
def delete(request, id):
    if request.method == 'DELETE':
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponse(json.dumps({"name": person.name, "address": person.address}), content_type="application/json")


