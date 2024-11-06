from dogs import Dog
from csv import reader

dogs = []

with open('dogslist.csv') as csv_file:
    csv_reader = reader(csv_file, delimiter=',')
    for dog, name, breed in csv_reader:
        dogs.append(Dog(name, breed))

for dog in dogs:
    print(dog)