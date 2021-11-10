# app/views.py
from banjo.urls import route_get, route_post
from app.models import Person

@route_post('add_person', args={'name': str, 'email_address': str})
def add_person(params):
    new_person = Person.from_dict(params)
    new_person.save()
    return new_person.to_dict()


@route_get('all_persons')
def all_persons(params):
    if len(Person.objects.all()) > 0:
        all_persons = []
        for person in Person.objects.all():
            all_persons.append(person.to_dict())
        return {'all persons': all_persons}

    else:
        return {'error': 'no persons exisit'}


@route_get('one_person', args={'name':str})
def one_persons(params):
    if Person.objects.filter(name=params['name']).exists():
        one_person = Person.objects.filter(name=params['name'])[0]
        return {params['name']:one_person.email_address}

    else:
        return {'error': 'no persons exisit'}
