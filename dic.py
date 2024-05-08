#!/usr/bin/env python

import re

#Pathway dictonary's 
# to call a key inside a dictonary dictonary["keyName"] exp print("Name:",arts["name"]) Name: Arts 
amtec = {
	"name": "Advanced Manufacturing and Aerospace",
	"info": "",
	"programs":["Advanced Avionics", "Aviation Maintenance Technology", "Composites", "Engineering Technology", "Mechatronics / Maintenance Technician Training", "Precision Machining", "Welding & Fabrication"]
}

arts = {
	"name":"Arts",
	"info":"",
	"programs":["Music", "Photography", "Studio Arts (Ceramics, Drawing, Painting, Printmaking)", "Graphic Design and Web Design"]
}

business = {
	"name":"Business",
	"info":"",
	"programs":["Accounting & Bookkeeping", "BAS in Accounting at EvCC", "Business (Business Administration, Management, Marketing)", "Cosmetology", "Economics", "Healthcare Management (Business Technology, Healthcare Risk Management, Medical Front Office, Medical Office Administration, Medical Billing and Coding)", "Information Technology"]
}

stem = {
	"name":"Science, Technology, Engineering, and Math",
	"info":"",
	"programs":["Computer Science", "Engineering", "Math", "Science", "Astronomy/Physics", "Atmospheric Science", "Biology", "Botany", "Chemistry", "Environmental Science", "Geology", "Oceanography"]
}

sjw = {
	"name":"Social Science, Education, and Public Safety",
	"info":"",
	"programs":["Anthropology", "Criminal Justice", "Diversity, Equity, and Social Justice", "Early Childhood Education", "Education", "EMT", "Fire Science", "Geography", "Human Services", "Physical Education", "Political Science", "Psychology", "Sociology"]
}

transitional = {
	"name":"Transitional Studies",
	"info":"",
	"programs":" "
}

explore = {
	"name":"Exploratory",
	"info":"",
	"programs":["English Classes (ELA/ESL)", "Youth Re-Engagement Program (U3)", "GED", "GED in Español", "High School Completion (HSC)", "Integrated Basic Education and Skills Training (I-BEST)", "College Success 101", "Study Online"]
}

health = {
	"name":"Healthcare",
	"info":"",
	"programs":["Medical Assisting", "Medical Spanish Interpreter", "Nursing", "Nutrition", "Phlebotomy", "Pre-Dental Hygiene", "Pre-Medicine", "Pre-Nursing", "Pre-Occupational Therapy", "Pre-Physical Therapy"]
}

humanities = {
	"name":"Humanities",
	"info":"",
	"programs":["Communication Studies", "Creative Writing", "Drama, English and Literature", "Global Studies", "History", "Humanities", "Journalism", "Philosophy", "World Languages"]
}

pathways = [amtec, arts, business, stem, sjw, transitional, explore, health, humanities]

#User dic
user = {
	"name": "",
	"gender":"",
	"subjectPronoun":"they",
	"objectPronoun":"them",
	"possessivePronoun":"theirs",
	"fantasyRace":"",
	"choice": "",
	"programChoice":""
}

#definitions to run the scipt
#startUp displays welcome message in the furture might contain start up for cursers modual
def startUp():
   print("Welcome to the program")
   return()
#adds user input to user dictonary key
def getUserName():
  user["name"] = input("Enter your name: ")
  return()
def getUserGender():
  user["gender"] = input("What is your gender(this is an optional release of information): ")
  return()
def getUserPronouns():
  pronounInput = input("what are your pronouns? ")
  pronouns = [pronoun.strip() for pronoun in re.split(r'[, /]', pronounInput)]
  # Assign pronouns to respective keys
  if len(pronouns) >= 1:
    user["subjectPronoun"] = pronouns[0]
  if len(pronouns) >= 2:
    user["objectPronoun"] = pronouns[1]
  if len(pronouns) >= 3:
    user["possessivePronoun"] = pronouns[2]
  return()

def mainMenu():
	while True:
	  choice=input("Press 1 to start the pathway Quiz or 2 to get information on all of the pathways: ")
	  if choice=="1":
	    startQuiz()
	    break
	  elif choice=="2":
 	    displayPathways()
 	    break
	  else:
	  	print("invalid input!")
	return(choice)

def startQuiz():
	return()

def displayInfo():

def displayPathways():
    fixedWidth = 50
    c = 0
    for i,pathway in enumerate(pathways):
        if c < 2:
            print(f"{i+1}:{pathway['name']:{fixedWidth}}", end="")
            c = c + 1
            i = i + 1
        else:
            print(f"{i+1}:{pathway['name']}")
            c = 0
            i = i + 1
            print("") 
    print("")        
    return()

def displayPathwayInfo(num):
	num -= 1
	print(f"\n{pathways[num]['name']}\n{pathways[num]['info']}")
	return()

def displayPrograms():
    fixedWidth = 50
    c = 0
    for i,program in enumerate({pathways[user["choice"]]["programs"]}):
        if c < 2:
            print(f"{i+1}:{program}:{fixedWidth}", end="")
            c = c + 1
            i = i + 1
        else:
            print(f"{i+1}:{program}")
            c = 0
            i = i + 1
            print("") 
    print("")        
    return()

def pathwayChooser():
 	while True:
 		try:
 		  display = int(input("Enter the number to the left of the pathway to get more information: "))
 		  break
 		except ValueError:
 			print("Please enter a valid choice")
 	return(display)		

def programChooser():
 	while True:
 		try:
 		  display = int(input("Enter the number to the left of the program to get more information: "))
 		  break
 		except ValueError:
 			print("Please enter a valid choice")
 	return(display)		



# This is the entry point if this code is run as a script
if __name__ == "__main__":


 startUp()
 getUserName()
 getUserGender()
 getUserPronouns()
 print(f"Welcome to the EVCC's Pathway chooser "+user["name"])
 while user["choice"] != True:
 	choice=mainMenu()
 	if choice == "2":
 		display=pathwayChooser()

 	displayPathwayInfo(display)
 	while True:
 		confirm=input("Would you like to pick this pathway and explore the programs in it? (Y/n)")
 		confirm=confirm.upper()
 		if confirm =="Y":
 			user["choice"] = pathways[display]
 			displayPrograms()
 			break
 		elif confirm =="N":
 			break
 		else:
 			print("please enter y for yes n for no")
 while user["programChoice"] != True:
 	us=programChooser()


#testing database keys
# for i in pathways:
#    try:
#        print(i["name"])
#        print(i["Programs"])
#    except KeyError:
#        print("Missing key in dictionary:", i)
#    except TypeError:
#        print("Not a dictionary:", i)
#print (user["name"]+" "+user["gender"]+" "+user["subjectPronoun"]+"/"+user["objectPronoun"]+"/"+user["possessivePronoun"])


    		
