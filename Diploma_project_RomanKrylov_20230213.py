import datetime
import csv


class Person():
    def __init__(self, first_name, last_name, patronymic,
                 birthdate, gender, deathdate=None):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.gender = gender
        self.birthdate = self._parse_date(birthdate) or datetime.date.today()
        self.deathdate = self._parse_date(deathdate)

    def __str__(self):
        str_list = [self.first_name]
        if self.last_name:
            str_list.append(self.last_name)
        if self.patronymic:
            str_list.append(self.patronymic)
        if self.is_alive():
            age_str = str(self.age()) + ' років'
        else:
            age_str = str(self.age(self.deathdate)) + ' років (помер)'
        str_list.append(age_str)
        str_list.append('чоловік' if self.gender == 'm'
                        else 'жінка' if self.gender == 'f' else 'стать не вказана')
        str_list.append(f'Народи{"вся" if self.gender == "m" else "лась"}: '
                        f'{self.birthdate.strftime("%d.%m.%Y")}')
        if not self.is_alive():
            str_list.append(f'Помер{"" if self.gender == "m" else "ла"}: '
                            f'{self.deathdate.strftime("%d.%m.%Y")}')
        return ' '.join(str_list)

    def _parse_date(self, date_str):
        if date_str:
            try:
                return datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
            except ValueError:
                try:
                    return datetime.datetime.strptime(date_str, '%d %m %Y').date()
                except ValueError:
                    try:
                        return datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
                    except ValueError:
                        try:
                            return datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
                        except ValueError:
                            return None
        else:
            return None

    def is_alive(self):
        return self.deathdate is None

    def age(self, reference_date=None):
        if reference_date is None:
            reference_date = datetime.date.today()
        if self.is_alive():
            return reference_date.year - self.birthdate.year - ((reference_date.month, reference_date.day) < (self.birthdate.month, self.birthdate.day))
        else:
            return self.deathdate.year - self.birthdate.year - ((self.deathdate.month, self.deathdate.day) < (self.birthdate.month, self.birthdate.day))

    @staticmethod
    def from_list(lst):
        return Person(*lst)

    @staticmethod
    def to_list(person):
        birthdate_str = person.birthdate.strftime('%d.%m.%Y') if person.birthdate else ''
        deathdate_str = person.deathdate.strftime('%d.%m.%Y') if person.deathdate else ''
        return [person.first_name, person.last_name, person.patronymic, birthdate_str, deathdate_str, person.gender]


class PeopleDB():
    def __init__(self):
        self.people = []

    def load(self, filename):
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # skip header row
            for row in reader:
                self.people.append(Person.from_list(row))

    def save(self, filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Ім`я', 'Прізвище', 'По-батькові', 'Дата народження', 'Дата смерті', 'Стать'])
            for person in self.people:
                writer.writerow(Person.to_list(person))

    def show_people(self, people):
        for person in people:
            print(person)

    def search_people(self, **params):
        result = self.people
        for key, value in params.items():
            if value:
                if key == "birthdate" or key == "deathdate":
                    date = self._parse_date(value)
                    if date:
                        result = [person for person in result if getattr(person, key) == date]
                else:
                    result = [person for person in result if getattr(person, key) == value]
        return result

    def search_or_add_people(self):
        first_name = input('Ім`я: ')
        last_name = input('Прізвище: ')
        patronymic = input('Побатькові: ')
        birthdate = input('Дата народження: ')
        deathdate = input('Дата смерті: ')
        gender = input('Стать (m/f): ')
        new_person = Person(first_name, last_name, patronymic,
                            birthdate, gender, deathdate)
        if not new_person.first_name or not new_person.last_name or not new_person.gender:
            print('Ім`я, Прізвище та стать є обов`язковими полями.')
            return
        if not new_person.birthdate:
            choice = input('Дата народження не вказана. Продовжити? (y/n)')
            if choice.lower() != 'y':
                return
        if not new_person.is_alive() and not new_person.deathdate:
            choice = input('Людина померла, але дата смерті не вказана. Продовжити? (y/n)')
            if choice.lower() != 'y':
                return
        self.people.append(new_person)
        print(f'Людина {new_person} успішно додана до бази даних.')


def main():
    db = PeopleDB()
    db.save('people.csv')
    db.load('people.csv')
    while True:
        while True:
            choice = input('Введіть команду (s - пошук, a - додати нову людину, q - вийти з програми): ')
            if choice == 's':
                first_name = input('Ім`я: ')
                last_name = input('Прізвище: ')
                patronymic = input('Побатькові: ')
                birthdate = input('Дата народження: ')
                deathdate = input('Дата смерті: ')
                gender = input('Стать (m/f): ')
                people = db.search_people(first_name=first_name,
                                          last_name=last_name, patronymic=patronymic,
                                          birthdate=birthdate, deathdate=deathdate,
                                          gender=gender)
                db.show_people(people)
            elif choice == 'a':
                db.search_or_add_people()
            elif choice == 'q':
                break
            else:
                continue
        db.save('people.csv')
        break


main()
