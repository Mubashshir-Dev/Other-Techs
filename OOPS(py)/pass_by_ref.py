class person:
    def __init__(self,name,cool):
        self.name=name
        self.cool=cool

# call by reference pass by refernce
def join_fightclub(fighter):
    print(id(fighter))
    fighter.name="tyler durden"
    fighter.cool=True

person1 = person("Narrator",False)
print("before fight club")
print(id(person1))
print("\n",person1.name,person1.cool,"\n")
join_fightclub(person1)
print("after joining fight club")
print("\n",person1.name,person1.cool)