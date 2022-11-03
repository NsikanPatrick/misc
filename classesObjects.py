class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    def change_name(self, new_name):
        return new_name
        
    def change_age(self, new_age):
        return new_age
        
    def add_tracks(self, added_tracks):
        new_tracks = added_tracks
        return new_tracks
        
    def get_score(self):
        return self.score
        
        
# Instantiating the class with initial values
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

#Providing unique values to print statements   
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_tracks("UI/UX"))
print(Bob.get_score())