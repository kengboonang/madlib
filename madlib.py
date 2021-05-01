#import module
from tkinter import *

# initialize window
root = Tk()
root.geometry('800x800')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'KB Mad Libs Generator Test \n Have Fun!' , font = 'Garde 40 bold').pack()
Label(root, text = 'Click Any One :', font = 'trebutchet 15 ').place(x=40, y=200)


################Stories##############

def madlib1():

    feeling = input('how are you feeling: ')
    food = input('What do you like to eat on a monday: ')
    verb = input('enter an action: ')
    vehicle = input('name a vehicle: ')
    duration = input('enter a duration: ')
    location = input('enter a place: ')
    cookingequipment = input('what do you bake macarons with: ')
    ingredient = input('food name: ')
    print('Whenever I get ' + feeling + ', I will be inclined to make a bowl of ' + food + '. Right after finising up on ' + verb + ', I got into the mood and decided to cook. I got on a ' + vehicle + ' and took about ' + duration + 'to reach my ' + location +' and took out my favourite ' + cookingequipment + '. After heating up the ' + cookingequipment + ', I realised that the dish simply had to have ' + ingredient + '. But alas, I was too lazy to get the missing ingredient and just went back to sleep. The end.')



def madlib2():

    action = input('enter a verb ending with ing: ')
    person = input('enter the name of your professor: ')
    sport = input('enter a sport:')
    dish = input('enter your favourite food: ')
    cheat = input('How would you cheat in an FTT: ')
    fish = input('What would someone have to do to get slapped with a fish: ')
    income = input('enter your dream income: ')

    print('Whenever I feel pissed, I like to vent by ' + action + '. One time while venting, I met ' + person + ' and we decided to have a friendly competition of ' + sport + '. The loser was to treat both participants to a meal of ' + dish + '. Taking into account ' + person + 'had a weaknesses, I deicided to cheat by ' + cheat + '. This turned out pretty badly when ' + fish + '. It was not meant to be and I had to pay ' + income + ' while losing the competition and still feeling pissed. The End. ')



def madlib3():
    date = input('enter date: ')
    name = input('enter a name: ')
    country = input('enter the last country you visited: ')
    item = input('enter a item you go to sleep with: ')
    relative = input('enter a relative: ')
    transport = input('enter a mode of transport: ')
    drink = input('enter your most hated drink: ')
    gender = input('enter m/f: ')
    if gender is 'm' or 'f':
        if gender == 'm':
            gender = 'he'
        elif gender == 'f':
            gender = 'she'
    else:
        gender = 'they'


    print('On a ' + date + ', ' + name + ' decided to go on a climbing trip in ' + country + '. "Dont forget to bring your ' + item + '" yelled ' + relative + '. ' + name + ' kept a mental note but ended up forgetting any way. Upon travelling via ' + transport + ' to the climbing area in ' + country + ', ' + name + ' took out a bottle of ' + drink + ' that was prepared beforehand to quench their thirst. All was good and ' + name + ' reached the famed climbing area. Just as ' + gender + ' was about to get on the first route, ' + name + ' realised that ' + gender + ' forgot to bring their ' + item + ' and broke down in tears. The end.')



######buttons
Button(root, text= 'Cooking', font ='arial 15', command= madlib1, bg = 'red').place(x=60, y=240)
Button(root, text= 'Venting', font ='arial 15', command = madlib2 , bg = 'yellow').place(x=70, y=300)
Button(root, text= 'Climbing', font ='arial 15', command = madlib3, bg = 'blue').place(x=80, y=360)

root.mainloop()
