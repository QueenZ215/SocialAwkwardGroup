import re

#Pathway dictonary's 
# to call a key inside a dictonary dictonary["keyName"] exp print("Name:",arts["name"]) Name: Arts 
amtec = {
	"name": "Advanced Manufacturing and Aerospace",
	"info": "",
	"choice": False,
	"programs":"Advanced Avionics, Aviation Maintenance Technology, Composites, Engineering Technology ,Mechatronics / Maintenance Technician Training ,Precision Machining, Welding & Fabrication"
}

arts = {
	"name":"Arts",
	"info":"",
	"choice": False,
	"programs":"Music, Photography, Studio Arts (Ceramics, Drawing, Painting, Printmaking), Graphic Design and Web Design"
}

business = {
	"name":"Business",
	"info":"",
	"choice": False,
	"programs":"Accounting & Bookkeeping, BAS in Accounting at EvCC, Business(Business Administration, Management, Marketing), Cosmetology, Economics, Healthcare Management(Business Technology, Healthcare Risk Management, Medical Front Office, Medical Office Administration, Medical Billing and Coding), Information Technology"
}

stem = {
	"name":"Science, Technology, Engineering, and Math",
	"info":"",
	"choice": False,
	"programs":"Computer Science, Engineering, Math, Science(Astronomy/Physics, Atmospheric Science, Biology, Botany, Chemistry, Environmental Science, Geology, Oceanography)"
}

sjw = {
	"name":"Social Science, Education, and Public Safety",
	"info":"",
	"choice": False,
	"programs":"Anthropology, Criminal Justice, Diversity, Equity, and Social Justice, Early Childhood Education, Education, EMT, Fire Science, Geography, Human Services, Physical Education, Political Science, Psychology, Sociology"
}

transitional = {
	"name":"Transitional Studies",
	"info":"",
	"choice": False,
	"programs":" "
}

explore = {
	"name":"Exploratory",
	"info":"",
	"choice": False,
	"programs":"English Classes (ELA/ESL), Youth Re-Engagement Program (U3), GED, GED in Español, High School Completion (HSC), Integrated Basic Education and Skills Training (I-BEST), College Success 101, Study Online"
}

health = {
	"name":"Healthcare",
	"info":"",
	"choice": False,
	"programs":"Medical Assisting, Medical Spanish Interpreter, Nursing, Nutrition, Phlebotomy, Pre-Dental Hygiene, Pre-Medicine, Pre-Nursing, Pre-Occupational Therapy, Pre-Physical Therapy"
}

humanities = {
	"name":"Humanities",
	"info":"",
	"choice": False,
	"programs":"Communication Studies, Creative Writing, Drama, English and Literature, Global Studies, History, Humanities, Journalism, Philosophy, World Languages"
}

pathways = [amtec, arts, business, stem, sjw, transitional, explore, health, humanities]

#User dic
user = {
	"name": "",
	"gender":"",
	"subjectPronoun":"they",
	"objectPronoun":"them",
	"possessivePronoun":"theirs",
	"fantasyRace":""
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
    print("Welcome to the EVCC's Pathway chooser " + user["name"] + "!")
    while True:
        choice = input("Press 1 to start the pathway Quiz or 2 to get information on all of the pathways: ")
        if choice == "1":
            startQuiz()
            break
        elif choice == "2":
            displayInfo()
            break
        else:
            print("Invalid input!")
    return()


def startQuiz():
	return()

def displayInfo():




# This is the entry point if this code is run as a script
if __name__ == "__main__":

#testing database keys
# for i in pathways:
#    try:
#        print(i["name"])
#        print(i["Programs"])
#    except KeyError:
#        print("Missing key in dictionary:", i)
#    except TypeError:
#        print("Not a dictionary:", i)
 startUp()
 getUserName()
 getUserGender()
 mainMenu()
 #print (user["name"]+" "+user["gender"]+" "+user["subjectPronoun"]+"/"+user["objectPronoun"]+"/"+user["possessivePronoun"])


    		
