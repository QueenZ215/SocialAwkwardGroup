#!/usr/bin/env python

import re

#Program dictonary's
#amtec
amtecAA ={"name":"Advanced Avionics","info":"","class":""}
amtecAMT={"name":"Aviation Maintenance Technology","info":"","class":""}
amtecComp={"name":"Composites","info":"","class":""}
amtecET={"name":"Engineering Technology","info":"","class":""}
amtecMech={"name":"Mechatronics / Maintenance Technician Training","info":"","class":""}
amtecPM={"name":"Precision Machining","info":"","class":""}
amtecWeld={"name":"Welding & Fabrication","info":"","class":""}

#arts
artsMusic={"name":"Music","info":"","class":""}
artsPhoto={"name":"Photography","info":"","class":""}
artsStudio={"name":"Studio Arts (Ceramics, Drawing, Painting, Printmaking)","info":"","class":""}
artsWeb={"name":"Graphic Design and Web Design","info":"","class":""}

#bisness
bisAcc={"name":"Accounting & Bookkeeping","info":"","class":""}
bisBAS={"name":"BAS in Accounting at EvCC","info":"","class":""}
bis={"name":"Business (Business Administration, Management, Marketing)","info":"","class":""}
bisCosmo={"name":"Cosmetology","info":"","class":""}
bisEcon={"name":"Economics","info":"","class":""}
bitHealth={"name":"Healthcare Management","info":"","class":""}
bisMOA={"name":"Medical Office Administration ","info":"","class":""}
bisBill={"name":"Medical Billing and Coding","info":"","class":""}
bisIT={"name":"Information Technolog","info":"","class":""}
bisTech={"name":"Business Technology","info":"","class":""}

#STEM
stemCS={"name":"Computer Science","info":"","class":""}
stemEng={"name":"Engineering","info":"","class":""}
stemMath={"name":"Math","info":"","class":""}
stemSci={"name":"Science","info":"","class":""}
stemPhy={"name":"Astronomy/Physics","info":"","class":""}
stemAtmo={"name":"Atmospheric Science","info":"","class":""}
stemBio={"name":"Biology","info":"","class":""}
stemBot={"name":"Botany","info":"","class":""}
stemChem={"name":"Chemistry","info":"","class":""}
stemEnv={"name":"Environmental Science","info":"","class":""}
stemGeo={"name":"Geology","info":"","class":""}
stemOcean={"name":"Oceanography","info":"","class":""}

#sjw
sjwAnth={"name":"Anthropology","info":"","class":""}
sjwCJ={"name":"Criminal Justice","info":"","class":""}
sjwDE={"name":"Diversity, Equity, and Social Justice","info":"","class":""}
sjwKid={"name":"Early Childhood Education","info":"","class":""}
sjwEdu={"name":"Education","info":"","class":""}
sjwEMT={"name":"EMT","info":"","class":""}
sjwFire={"name":"Fire Science","info":"","class":""}
sjwGeo={"name":"Geography","info":"","class":""}
sjwHuman={"name":"Human Services","info":"","class":""}
sjwPhy={"name":"Physical Education","info":"","class":""}
sjwPol={"name":"Political Science","info":"","class":""}
sjwPsy={"name":"Psychology","info":"","class":""}
sjwSoc={"name":"Sociology","info":"","class":""}

#trans
trans={"name":"Transitional Studies","info":"","class":""}

#exp
expEng={"name":"English Classes (ELA/ESL)","info":"","class":""}
expYouth={"name":"Youth Re-Engagement Program (U3)","info":"","class":""}
expGED={"name":"GED","info":"","class":""}
expHSC={"name":"High School Completion (HSC)","info":"","class":""}
expIBest={"name":"Integrated Basic Education and Skills Training (I-BEST)","info":"","class":""}
expsucc={"name":"College Success","info":"","class":""}

#Health
healthMA={"name":"Medical Assisting","info":"","class":""}
healthMSI={"name":"Medical Spanish Interpreter","info":"","class":""}
healthNUR={"name":"Nursing","info":"","class":""}
healthNut={"name":"Nutrition","info":"","class":""}
healthPhl={"name":"Phlebotomy","info":"","class":""}
healthDen={"name":"Pre-Dental Hygiene","info":"","class":""}
healthMED={"name":"Pre-Medicine","info":"","class":""}
healthPN={"name":"Pre-Nursing","info":"","class":""}
healthOT={"name":"Pre-Occupational Therapy","info":"","class":""}
healthPT={"name":"Pre-Physical Therapy","info":"","class":""}

#Humanities
humCom={"name":"Communication Studies","info":"","class":""}
humCW={"name":"Creative Writing","info":"","class":""}
humDrana={"name":"Drama","info":"","class":""}
humEng={"name":"English and Literature","info":"","class":""}
humGS={"name":"Global Studies","info":"","class":""}
humHis={"name":"History","info":"","class":""}
HumHum={"name":"Humanities","info":"","class":""}
humJou={"name":"Journalism","info":"","class":""}
humPhil={"name":"Philosophy","info":"","class":""}
humLang={"name":"World Languages","info":"","class":""}

#races
human={"name":"Human","pathway":"Any","info":"The true jack of all trades. With a minimal afinity for magic and a versitile skillset, most fields are a good fit for humans."}
elf={"name":"Elf","pathway":"Exploratory","info":"Free spirits with long lives. Their extreme afinity for magic and longevity leads to the exploratory path to find a good fit for their style."}
orc={"name":"Orc","pathway":"SJW","info":"Gentle, in spite of apperances. With their durable physique and patience the Social Justic Worker path is a good choice."}
dwarf={"name":"Dwarf","pathway":"Arts","info":"Traditionally master artisans. while a stereotype they do tend to enjoy the arts path, even if they don't plan on pursuing a full degree."}
goblin={"name":"Goblin","pathway":"TS","info":"Incredibly insightful and fast learners. Most goblins struggle with language and tend to follow the Transitional Studies route befor anything else. "}
kobold={"name":"Kobold","pathway":"Amtec","info":"Scrappy little tinkerers. Their innate trap making prowess leads quite nicely into the Advanced Manufaturing and Aerospace pathway."}
fae={"name":"Fae","pathway":"Humanities","info":"Will not lie to you ever. They tend to have a love of learning about language due to their long life spans which leads them to the Humanities path."}
gnome={"name":"Gnome","pathway":"STEM","info":"Not dwarves, they made them. with their incredible intelligence they fall very easily into the STEM pathway for obvious reasons."}
devil={"name":"Devil","pathway":"Business","info":"They are NOT inherently evil. the Buisness pathway is a very common route for devils to ensure they are making fair deals with their prospective clients."}
vampire={"name":"Vampire","pathway":"Healthcare","info":"Vampirism is only kind of a disease. Most vampirese go into Healthcare to try and cure themselves, but also to help others who have it worse than them."}

#lists
fantasyRace=[human,elf,orc,dwarf,goblin,kobold,fae,gnome,kobold,fae,gnome,devil,vampire]

amtecProgs = [amtecAA, amtecAMT, amtecComp, amtecET, amtecMech, amtecPM, amtecWeld]
artsProgs = [artsMusic, artsPhoto, artsStudio, artsWeb]
bisProgs = [bisAcc, bisBAS, bis, bisCosmo, bisEcon, bitHealth, bisMOA, bisBill, bisIT, bisTech]
stemProgs = [stemCS, stemEng, stemMath, stemSci, stemPhy, stemAtmo, stemBio,stemBot, stemChem, stemEnv, stemGeo, stemOcean]
sjwProgs = [sjwAnth, sjwCJ, sjwDE, sjwKid, sjwEdu, sjwEMT, sjwFire, sjwGeo, sjwHuman, sjwPhy, sjwPol, sjwPsy, sjwSoc]
transProgs = [trans]
expProgs = [expEng, expYouth, expGED, expHSC, expIBest, expsucc]
healthProgs = [healthMA, healthMSI, healthNUR, healthNut, healthPhl, healthDen, healthMED, healthPN, healthOT, healthPT]
humProgs = [humCom, humCW, humDrana, humEng, humGS, humHis, HumHum, humJou, humPhil, humLang]

#Pathway dictonary's 
# to call a key inside a dictonary dictonary["keyName"] exp print("Name:",arts["name"]) Name: Arts 
amtec = {
	"name": "Advanced Manufacturing and Aerospace",
	"info": "",
	"programs":amtecProgs}

arts = {
	"name":"Arts",
	"info":"",
	"programs":artsProgs}

business = {
	"name":"Business",
	"info":"",
	"programs":bisProgs}

stem = {
	"name":"Science, Technology, Engineering, and Math",
	"info":"",
	"programs":stemProgs}

sjw = {
	"name":"Social Science, Education, and Public Safety",
	"info":"",
	"programs":sjwProgs}

transitional = {
	"name":"Transitional Studies",
	"info":"",
	"programs":transProgs
}

explore = {
	"name":"Exploratory",
	"info":"",
	"programs":expProgs}

health = {
	"name":"Healthcare",
	"info":"",
	"programs":healthProgs}

humanities = {
	"name":"Humanities",
	"info":"",
	"programs":humProgs
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

def startUp():
   print("Welcome to the program")
   return()

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

def getUserRace():
  
  print(f"{user['name']}, these are the mighty races of the land: ")
  while True:
  	fixedWidth = 50
  	c = 0
  	for i,race in enumerate(fantasyRace):
  		if c < 2:
  			print(f"{i+1}:{race['name']:{fixedWidth}}", end="")
  			c = c + 1
  			i = i + 1
  		else:
  			print(f"{i+1}:{race['name']}")
  			c = 0
  			i = i + 1
  			print("") 
  		print("")
  	num=int(input("Enter the number left of the race you see more information:"))

  	print(f"{fantasyRace[num-1]['name']}	{fantasyRace[num-1]['pathway']}")
  	print(f"	{fantasyRace[num-1]['info']}")
  	choice=input(f"{user['name']}, would you like to keep this race?")
  	choice=choice.upper()
  	if choice == "YES":
  		user["race"]={fantasyRace[num-1]['name']}
  		break
  	else:
  		print()
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
	print("Check back soon we are working hard")
	return()

def displayInfo():
	return()


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
    for i,program in enumerate({pathways[{user["choice"]}]["programs"]}): #BUG need to be able to call the correct programs of the correct pathway
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
  while True:
  	startUp()
  	getUserName()
  	getUserGender()
  	getUserPronouns()
  	getUserRace()
  	print(f"Welcome to the EVCC's Pathway chooser "+user['name'])
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
  					break
  				elif confirm =="N":
  					break
  				else:
  					print("please enter y for yes n for no")
  			while user["programChoice"] != True:
  				displayPrograms()
  				choice=programChooser()
  				user['programChoice'] = {pathways[user["choice"]][choice]}
  				programInfo()
  		reset=print(f"Hey {user['name']}! thanks for useing EVCC's Pathway program today you explored the {user['programChoice']} program in the {user[choice]} pathway . if you would like try again type reset or anything eles to end")
  		reset=reset.upper
  		if reset == "RESET":
  			print("")
  		else:
  			break



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


    		
