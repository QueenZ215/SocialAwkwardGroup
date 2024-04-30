
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
	"pronouns":"",
	"fantasyRace":""
}


for i in pathways:
    try:
        print(i["name"])
        print(i["Programs"])
    except KeyError:
        print("Missing key in dictionary:", i)
    except TypeError:
        print("Not a dictionary:", i)