from google.appengine.ext import ndb

class Person(ndb.Model):
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()

class Restaurants(ndb.Model):
    name = ndb.StringProperty()
    hours = ndb.StringProperty()
    date = ndb.StringProperty()
    value = ndb.StringProperty()

def insert():
    r = Restaurants(name='PandaExp', hours='11:00am-9:00pm', value='Bakery')
    k = r.put()
    q = Restaurants.all()
    return str(q)

def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val

# def sanitize_input(input):
#     return re.sub('\s+', '', input).lower()
#
#
# def get_address(building):
#     '''
#     Query DB and return addresses
#     '''
#
#
# def get_restaurants(food):
#     '''
#     Query DB and return restaurant names with addresses
#     '''
#
#
# def get_building(request):
#     context = request['context']
#     entities = request['entities']
#
#     loc = first_entity_value(entities, 'location')
#     if loc:
#         building = sanitize_input(loc)
#         context['building'] = building
#         #content['address'] = get_address(building)
#         if context.get('missingBuilding') is not None:
#             del context['missingBuilding']
#     else:
#         context['missingBuilding'] = True
#         if context.get('building') is not None:
#             del context['building']
#
#     return context
#
#
def get_food(request):
    context = request['context']
    entities = request['entities']

    food = first_entity_value(entities, 'food')
    if food:
        food_name = sanitize_input(food)
        restaurants = get_restaurants(food_name)
        context['food'] = food_name
        content['restaurants'] = restaurants

        if context.get('missingFood') is not None:
            del context['missingFood']
    else:
        context['missingFood'] = True
        if context.get('food') is not None:
            del context['food']

    return context


# def get_event(request):
#     context = request['context']
#     entities = request['entities']
#
#     loc = first_entity_value(entities, 'location')
#     if loc:
#         location = sanitize_input(loc)
#         context['location'] = location
#         date_time = first_entity_value(entities, 'dateTime')
#         if date_time:
#             content['datetime'] = get_date_time(date_time)
#             if context.get('missingDateTime') is not None:
#                 del context['missingDateTime']
#
#     else:
#         date_time = first_entity_value(entities, 'dateTime')
#         if date_time:
#
#         else:
#
#         context['missingDateTime'] = True
#         if context.get('dateTime') is not None:
#             del context['dateTime']
#
#     return context
#
#
# def get_person_location(name):
#     '''
#     Query DB and return location of person with name
#     '''
#
#
# def get_person(request):
#     context = request['context']
#     entities = request['entities']
#
#     person = first_entity_value(entities, 'person')
#     if person:
#         person_name = sanitize_input(food)
#         context['name'] = person_name
#         content['location'] = get_person_location(person_name)
#
#         if context.get('missingName') is not None:
#             del context['missingName']
#     else:
#         context['missingName'] = True
#         if context.get('name') is not None:
#             del context['name']
#
#     return context

# def get_objectss(subject, predicate):
#
#     return []
#
# def get_subjects(predicate, object):
#     return []
#
# def create_tuple(subject, predicate, object):
#     return False