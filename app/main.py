class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    Person.people.clear()

    
    for item in people:
        Person(item["name"], item["age"])


    for item in people:
        person = Person.people[item["name"]]
        if "wife" in item and item["wife"] is not None:
            person.wife = Person.people[item["wife"]]
        if "husband" in item and item["husband"] is not None:
            person.husband = Person.people[item["husband"]]
    return list(Person.people.values())
