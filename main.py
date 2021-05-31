import json
import hashlib


def json_reader(file):
    with open(file.encode()) as f:
        countries = json.load(f)
    return countries


def writer_txt(file, countries_list, line_number):
    with open(file, "a+") as f:
        country = countries_list[line_number]['name']['common']
        url = f'https://en.wikipedia.org/wiki/' + country
        f.write(f'{country} - {url}\n')


class IterJson:
    def __init__(self, line_number):
        self.line_number = line_number
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.line_number:
            writer_txt('countries.txt', file_json, self.counter)
            self.counter += 1
        else:
            raise StopIteration


def generator_hash(file):
    with open(file) as f:
        for each_line in f:
            yield hashlib.md5(each_line.encode()).hexdigest()


if __name__ == '__main__':
    file_json = json_reader("countries.json")
    iterator = [country for country in IterJson(250)]

    for hash_line in generator_hash('countries.txt'):
        print(hash_line)
