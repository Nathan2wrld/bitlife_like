import random


# gallerie des noms
prenoms = ["Alex", "Jordan", "Emily", "Noah", "Sofia", "Liam", "Ava", "Ethan"]
noms = ["Smith", "Johnson", "Brown", "Martin", "Lee", "Wilson", "Clark", "Kenfack", "Donfack", "Kadji"]
prenoms_mere = ["Emma", "Justine", "Irene", "Annie", "Vanessa", "Jess"]
prenoms_pere = ["Alex", "Jordan", "Noah", "Liam", "Ethan"]
animal_name = ["Rex", "Bulldog", "Arrache", "Joe", "Guiness"]

#dates de naissance
date = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
february_date = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
#pour le menu asset
ass=["car", "TV", "boat", "lock", "text", "phone", "pant", "T-shirt", "doll", "shampoo"]

r_money = random.randint (1, 100000)

#faits randoms
facts = ["YOU GOT FLU", f"YOU FOUND $ {r_money}", "YOU GOT A NEW FRIEND", "YOU GOT A WOUND", "YOU LOOKED CARTOON NETWORK", "YOU WERE DEPRESSED", "YOU TOOK COCAINE", "YOU WROTE A BOOK", "YOU TRAVELLED UPON THE TIME", "YOU LOSED A FRIEND", "YOUR PHONE WERE CONFISCED", "YOU MESSED WITH YOUR MOTHER", "YOU JUST SOLD ONE OF YOU ASSETS", "YOU PLAYED WITH YOUR OLD FRIEND", "YOU GOT A LOOK AJUSTMENT", "YOU JUST CHILLED"]

#stats
argent = 0
age = 0
karma = random.randint(1, 100)
Esp_life = random.randint(1, 50)# petit a petit esperence de vie
happiness = random.randint(1, 100)
health = random.randint(1, 100)
intelligence = random.randint(1, 100)
look = random.randint(1, 100)
popularity = 0
grade_1 = random.randint(1, 100)# niveau scolaire au primaire

#esperence de vie du pere et de la mere et de l'animal
vie_pere = random.randint(1, 50)
vie_mere = random.randint(1, 50)
vie_animal = random.randint(1, 20)
vie_pere_1 = 0
vie_mere_1 = 0
vie_animal_1 = 0

#heritage de chaque parent
argent_pere = random.randint(1, 2000000)
argent_mere = random.randint(1, 2000000)

studies= ""#stat de niveau scolaire

name = ""

# choix du nom
print("choose your name (c) or random name (r)")
naming=str(input(">"))

if naming == 'c' or naming == 'C':
    first_name=str(input("what is your first name?"))
    last_name=str(input("what is your last name?"))
    name = first_name + " " + last_name
    print(name)
elif naming == 'r' or naming == 'R':
    first_name = random.choice(prenoms)
    last_name = random.choice(noms)
    name = first_name + " " + last_name
    print(name)

#choix de la date de naissance
birth_date = random.choice(date)
birth_month = random.choice(month)

if birth_month == "February":
    birth_date = random.choice(february_date)
print(f"you were born the {birth_date} of {birth_month}")
    
father_name = random.choice(prenoms_pere) +" "+ last_name# nom de papa
mother_name = random.choice(prenoms_mere) +" "+ last_name# nom de mama
animal = random.choice(animal_name)# nom animal


def affichage():#fonction affichage ecran principal
    print(f"""
____________________________________________________________
{name}
    
                money= {argent}$
                age= {age} years-old
____________________________________________________________
    1. job   |  2. assets  | 3. relations |  4. activities
_____________|_____________|______________|_________________
                happiness: {happiness}/100
____________________________________________________________
                health: {health}/100
____________________________________________________________
            intelligence: {intelligence}/100
____________________________________________________________
                look: {look}/100
____________________________________________________________
            popularity: {popularity}/100
____________________________________________________________
    
    """)


def random_event():
    global random_fact, r_money, facts, happiness, health, look, intelligence, argent, karma, popularity, age
    #faits randoms
    random_fact = random.choice(facts)
    print(f"\n {random_fact}\n")
    if "FLU" in random_fact:
        health = max(0, health - 5)
        look = max(0, look - 3)
        return
    if "$" in random_fact:
        argent += r_money
        return
    if "NEW" in random_fact:
        happiness = min(100, happiness + 10)
        karma = min(100, karma + 3)
        popularity = min(100, popularity + 5)
        return
    if "WOUND" in random_fact:
        health = max(0, health - 4)
        look = max(0, look -3)
        return
    if  "NETWORK" in random_fact:
        happiness = min(100, happiness + 10)
        intelligence = min(100, intelligence +10)
        karma = min(100, karma + 6)
        return
    if "DEPRESSED" in random_fact:
        happiness = max(0, happiness - 10)
        health = max(0, health - 10)
    if "COCAINE" in random_fact:
        happiness = min(100, happiness + 10)
        health = max(0, health - 11)
        return
    if "BOOK" in random_fact:
        intelligence = min(100, intelligence + random.randint(1, 20))
        karma = min(100, karma + 3)
        return
    if "TIME" in random_fact:
        look = min(100, look + random.randint(1, 15))
        intelligence = min(100, intelligence + 5)
        karma = max(0, karma - 5)
        age = max(0, age - random.randint(0, 5))
        return
    if "LOSED" in random_fact:
        happiness = max(0, happiness - 5)
        health = max(0, health -2)
        karma = max (0, karma - 3)
        popularity = max(0, popularity - 3)
        return
    if "PHONE" in random_fact:
        happiness = max(0, happiness - 10)
        health = min(100, health + 5)
        return
    if "MOTHER" in random_fact:
        happiness = max(0, happiness - 5)
        look = max(0, look - 3)
        return
    if "SOLD" in random_fact:
        argent += random.randint(1, 500)
        return
    if "OLD" in random_fact:
        happiness = min(100, happiness + 5)
        health = min(100, health + 10)
        return
    if "LOOK" in random_fact:
        look = min(100, look + 10)
        happiness = min (100, happiness + 8)
        return
    if "CHILLED" in random_fact:
        happiness = min (100, happiness + 8)
        health = min(100, health + 2)
        intelligence = min(100, intelligence + 2)
        return

def relations():# fonction du menu relations
    global happiness, intelligence, health, look, vie_mere, vie_mere_1, vie_pere_1, vie_pere, vie_animal, vie_animal_1
    print((f"""
--------- RELATIONS--------------

_________________________________
1. {father_name} (father)
_________________________________
2. {mother_name} (mother)
_________________________________
3. {animal} (animal)
_________________________________
b. Main Menu
_________________________________    
    """))
    rel=input(">")
    
    if rel=="1" and (happiness < 100 or intelligence < 100):#menu pere
        if vie_pere_1 < vie_pere:
            print(f"\n YOU ARE TALKING WITH YOUR FATHER {father_name}\n")
            happiness = min(100, happiness + 1)
            intelligence = min(100, intelligence + 1)
            if happiness == 100 or intelligence == 100:
                print(f"\n WHAT A GOOD RELATION WITH YOUR DAD\n")
        elif vie_pere_1 >= vie_pere:
            print(f"\n YOU DAD IS DEAD\n")
                
    elif rel=="2" and (happiness < 100 or look < 100):#menu mere
        if vie_mere_1 < vie_mere:
            print(f"\n YOU ARE TALKING WITH YOUR MOTHER {mother_name}\n")
            happiness = min(100, happiness +1)
            look = min(100, look +1)
            if happiness == 100 or look == 100:
                print(f"\n WHAT A GOOD RELATION WITH YOUR MUM\n")
        elif vie_mere_1 >= vie_mere:
            print(f"\n YOUR MUM IS DEAD\n")
            
    elif rel=="3" and (happiness < 100 or health < 100):#menu animal
        if vie_animal_1 < vie_animal:
            print(f"\n YOU ARE PLAYING WITH YOUR ANIMAL {animal}\n")
            happiness = min(100, happiness + 1)
            health = min(100, health + 1)
            if happiness == 100 or health == 100:
                print(f"\n WHAT A GOOD RELATION WITH YOUR ANIMAL\n")
        elif vie_animal_1 >= vie_animal:
            print(f"\n YOUR ANIMAL IS DEAD\n")
                
    elif rel=="b":#back
        return

def job_1():# fonction du menu job 
    global grade_1, intelligence
    print(f"""
--------JOB/ SCHOOL-----------

grade= {grade_1}/100

______________________________
1. study harder
______________________________
2. escape from school
______________________________
3. Joke during classes
______________________________
b. Main Menu
______________________________

""")
    e_choice=input(">")
    
    if e_choice == "1" and (grade_1 < 100 or intelligence < 100):
        print(f"\n YOU DECIDED TO STUDY HARDER IN SCHOOL\n")
        grade_1 = min(100, grade_1 + random.randint(0, 10))
        intelligence = min(100, intelligence + random.randint(0, 5))
        if grade_1 == 100:
            print(f"\n WHY DO YOU WANT TO STUDIE, YOU GENIUS?\n")
            
    elif e_choice == "2":
        print(f"\n YOU DECIDED TO ESCAPE FROM THE SCHOOL\n")
        grade_1 = max(0, grade_1 - random.randint(1, 5))
        
    elif e_choice == "3":
        print(f"\n YOU DECIDED TO JOKE DURING CLASSES\n")
        grade_1 = max(0, grade_1 - random.randint(1, 5))
        intelligence = max(0, intelligence - random.randint(1, 5))
    
    elif e_choice == "b":
        return

def assets():#assets et ajouter le fait que tu peux rater ton cambriolage et etre emprisone
    global argent, happiness, health, intelligence, ass
    rob=random.randint(0, 100)
    
    ass1=random.choice(ass)
    print("""

------ASSETS------------------

1. buy something
2. sell something
3. hang out with your bicycle
4. play some music
5. listen music
6. rob someone's house

b. back
""")
    assets_c=input(">")
    if assets_c=='1':
        print(f"\n YOU BOUGHT A {ass1}\n")
        argent-=random.randint(0, 100)
    elif assets_c=='2':
        print(f"\n YOU SOLD A {ass1}\n")
        argent+=random.randint(0,100)
    elif assets_c=='3':
        print(f"\n YOU MADE A TIME OUT \n")
        happiness=min(100, happiness + random.randint(0, 10))
        health=min(100, health + random.randint(0, 10))
    elif assets_c=='4':
        print("\n YOU PLAYED SOME MUSIC \n")
        intelligence=min(100, intelligence + random.randint(0, 10))
        happiness=min(100, happiness + random.randint(0, 10))
    elif assets_c=='5':
        print("\n YOU LISTENED SOME MUSIC \n")
        intelligence=min(100, intelligence + random.randint(0, 10))
        happiness=min(100, happiness + random.randint(0, 10))
    elif assets_c=='6':
        print(f"\n YOU ROBBED SOMEONE HOUSE AND GAIN ${rob} \n")
        argent+=rob
        health=max(0, health - random.randint(0, 10))
        happiness=max(0, happiness - random.randint(0, 10))
        intelligence=min(100, intelligence + random.randint(0, 10))
    elif assets_c=='b':
        return

def activities():#menu activites
    global happiness, health, intelligence, look
    print("""
------ACTIVITIES-----------------
1. go to the gym
2. go to the cinema
3. go to the park
4. go to the beach
b. back
----------------------------------
""")
    act=input(">")
    if act == "1":
        print("\n YOU WENT TO THE GYM \n")
        health=min(100, health + random.randint(0, 10))
        look=min(100, look + random.randint(0, 10))
    elif act == "2":
        print("\n YOU WENT TO THE CINEMA \n")
        happiness=min(100, happiness + random.randint(0, 10))
    elif act == "3":
        print("\n YOU WENT TO THE PARK \n")
        happiness=min(100, happiness + random.randint(0, 10))
        health=min(100, health + random.randint(0, 10))
    elif act == "4":
        print("\n YOU WENT TO THE BEACH \n")
        happiness=min(100, happiness + random.randint(0, 10))
        health=min(100, health + random.randint(0, 10))
    elif act == "b":
        return

#boucle principale du jeu
while True:
    affichage()

    
    
    if age == 5 and studies != "e.school":# debut ecole primaire
        print("""

        YOU JUST STARTED ELEMENTARY SCHOOL

        """)
        studies = "e.school"

    if age == 12 and studies != "m.school":#debut du middle school
        print("""

        YOU JUST STARTED MIDDLE SCHOOL

        """)
        studies = "m.school"
    
    if age == 14 and studies != "h.school":#debut du high school
        print("""

        YOU JUST STARTED HIGH SCHOOL
        
        """)
        studies = "h.school"

    if age == 18 and studies != "u.school":#debut de l'universite
        print("""

        YOU CAN NOW START UNIVERSITY
        
        """)
        studies = "u.school"

    print("""chose one menu between 1 and 4
                or get a year older by tapping the touch 'enter'
                """ )# choisir le menu
    menu=input(">")


    if menu.strip() == "":#grandir d'une annee
        change = random.randint(-5, 5)
        random_event()
        age+=1
        vie_pere_1 += 1
        vie_mere_1 += 1
        vie_animal_1 += 1
        if vie_pere_1 == vie_pere:
            print(f"\n YOUR FATHER IS DEAD\n")
            argent += argent_pere
            happiness = max(0, happiness - 15)
            health = max(0, health - 10)
            continue
            
        if vie_mere_1 == vie_mere:
            print(f"\n YOUR MOTHER IS DEAD\n")
            argent += argent_mere
            happiness = max(0, happiness - 17)
            health = max(0, health - 11)
            continue
            
        if vie_animal_1 == vie_animal:
            print(f"\n YOUR ANIMAL IS DEAD\n")
            happiness = max(0, happiness - 10)
            health = max(0, health - 5)
            continue
    
        happiness = max(0, min(100, happiness + change))
        health = max(0, min(100, health + change))
        intelligence = max(0, min(100, intelligence + change))
        look = max(0, min(100, look + change))
        popularity = max(0, min(100, popularity + random.randint(-2, 2)))
        
    if menu == "1":#menu job
        if age < 5:#si tu n'as pas au moins 5 ans, tu ne commence pas l'ecole
            print(f"""
            you are not old enough
            """)
            continue
        elif studies=="e.school":#faire les niveaux superieurs
            job_1()
            
    if menu == "2":#menu assets
        if age < 5:
            print(f"""
            you are not old enough
            """)
            continue
        else:
            assets()

    if menu == "3":# affichage menu 3
        relations()

    if menu == "4":# affichage menu 4
        if age < 5:
            print(f"""
            you are not old enough
            """)
            continue
        else:
            activities()

    #enfin, la mort
    if health <= 0 or age >= Esp_life:
        print(f"GAME OVER. {name} est mort à {age} ans.")
        break
