class Animal(object):
    def __init__(self,sound,name,age,favorite_color):
        self.sound=sound
        self.age=age
        self.name=name
        self.favorite_color=favorite_color
    def eat(self,food):
        print("Yummy!! " + self.name + "is eating" +food)
    def description(self):
        print(self.name + " is " + str(self.age)+" years old and loves the color " + self.favorite_color)
    def make_sound(self,times):
        print(self.sound*times)
class Person(object):
    def __init__(self,name,city,gender):
        self.name=name
        self.city=city
        self.gender=gender
    def eat_breakfast(self,favorite_food):
        print("Yummy!! " + "I am eating " + favorite_food)
    def play_sport(self,sport):
        print("I am playing " + sport)
class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self,list1):
        for s in list1:
            print(s)
i = Animal("Meow","cat",5,"green")
i.eat("fish")
i.description()
i.make_sound(4)
simon = Person("Simon","Nazareth","Male")
simon.eat_breakfast("Pancakes")
simon.play_sport("Soccer")
lyrics=["Roses are red","violets are blue","i made this poem for u"]
flower_song=Song(lyrics)
flower_song.sing_me_a_song(lyrics)

