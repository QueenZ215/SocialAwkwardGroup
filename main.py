#!/usr/bin/env python
from dic import *
import re

#races
human={"name":"Human","pathway":"Any","info":"The true jack of all trades. With a minimal afinity for magic and a versitile skillset, most fields are a good fit for humans."}
elf={"name":"Elf","pathway":"Exploratory","info":"Free spirits with long lives. Their extreme afinity for magic and longevity leads to the exploratory path to find a good fit for their style."}
orc={"name":"Orc","pathway":"SJW","info":"Gentle, in spite of apperances. With their durable physique and patience the Social Justic Worker path is a good choice."}
dwarf={"name":"Dwarf","pathway":"Arts","info":"Traditionally master artisans. while a stereotype they do tend to enjoy the arts path, even if they don't plan on pursuing a full degree."}
goblin={"name":"Goblin","pathways":"TS","info":"Incredibly insightful and fast learners. Most goblins struggle with language and tend to follow the Transitional Studies route befor anything else. "}
kobold={"name":"Kobold","pathway":"Amtec","info":"Scrappy little tinkerers. Their innate trap making prowess leads quite nicely into the Advanced Manufaturing and Aerospace pathway."}
fae={"name":"Fae","pathway":"Humanities","info":"Will not lie to you ever. They tend to have a love of learning about language due to their long life spans which leads them to the Humanities path."}
gnome={"name":"Gnome","pathways":"STEM","info":"Not dwarves, they made them. with their incredible intelligence they fall very easily into the STEM pathway for obvious reasons."}
devil={"name":"Devil","pathway":"Business","info":"They are NOT inherently evil. the Buisness pathway is a very common route for devils to ensure they are making fair deals with their prospective clients."}
vampire={"name":"Vampire","pathway":"Healthcare","info":"Vampirism is only kind of a disease. Most vampirese go into Healthcare to try and cure themselves, but also to help others who have it worse than them."}

#lists
fantasyRace=[human,elf,orc,dwarf,goblin,kobold,fae,gnome,kobold,fae,gnome,devil,vampire]
pathways = [amtec, arts, business, stem, sjw, transitional, explore, health, humanities]
amtecProgs = [amtecAA, amtecAMT, amtecComp, amtecET, amtecMech, amtecPM, amtecWeld]
artsProgs = [artsMusic, artsPhoto, artsStudio, artsWeb]
bisProgs = [bisAcc, bisBAS, bis, bisCosmo, bisEcon, bitHealth, bisMOA, bisBill, bisIT, bisTech]
stemProgs = [stemCS, stemEng, stemMath, stemSci, stemPhy, stemAtmo, stemBio,stemBot, stemChem, stemEnv, stemGeo, stemOcean]
sjwProgs = [sjwAnth, sjwCJ, sjwDE, sjwKid, sjwEdu, sjwEMT, sjwFire, sjwGeo, sjwHuman, sjwPhy, sjwPol, sjwPsy, sjwSoc]
transProgs = [trans]
expProgs = [expEng, expYouth, expGED, expHSC, expIBest, expsucc]
healthProgs = [healthMA, healthMSI, healthNUR, healthNut, healthPhl, healthDen, healthMED, healthPN, healthOT, healthPT]
humProgs = [humCom, humCW, humDrana, humEng, humGS, humHis, HumHum, humJou, humPhil, humLang]

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
