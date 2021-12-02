###########################   Thin Individual  #########################
def thinp(w):
    #protein requirement
    thinp_intake = w * 0.8
    return thinp_intake
def thinc(w):
    #carb requirement
    thinc_intake = w * 4
    return thinc_intake
def thinf(w):
    #fat requirement
    thinf_intake = w * 0.4
    return thinf_intake
###########################   Obese Individual  #########################
def obbp(w):
    #protein requirement
    thinp_intake = w * 1
    return thinp_intake
def obbc(w):
    #carb requirement
    thinc_intake = w * 3
    return thinc_intake
def obbf(w):
    #fat requirement
    thinf_intake = w * 0.3
    return thinf_intake
###########################   Athelets  #########################
def ap(w):
    #protein requirement
    thinp_intake = w * 1.5
    return thinp_intake
def ac(w):
    #carb requirement
    thinc_intake = w * 8
    return thinc_intake
def af(w):
    #fat requirement
    thinf_intake = w * 0.8
    return thinf_intake
###########################   Normal (Dont Know)  #########################
def sp(w):
    #protein requirement
    thinp_intake = w * 1.2
    return thinp_intake
def sc(w):
    #carb requirement
    thinc_intake = w * 3.5
    return thinc_intake
def sf(w):
    #fat requirement
    thinf_intake = w * 0.5
    return thinf_intake
############################### main code below ############################






name = input("Please Enter Your Name: ")
name = name.upper()
limit = 1950
currentyear = 2021
currentyear = int(currentyear)
while True:
    while True:
        age = input("Please Enter The Year You Were Born: ")
        try:
            age = int(age)
            break
        except:
            print("Please Enter Your Age In Numericals 'Ex: 1980'")
            continue
    if age < currentyear and age > limit:
        confirm_age = currentyear - age
        break    
    else:    
        print("Please Enter Your Correct Year Of Birth")
        continue
weight = 0
while True:
    weight = input("Enter Your Current Weight In Kilograms: ")
    try:
        weight = int(weight)
        break
    except:
        print("Please Enter Your Weight In Numericals Ex: '65'")
        continue

print("Please Tell Us What Type Of Body Type You Got\n We Divided These Catogories Into Four Major Parts Please Define Us By Entering The Given Option\nFor 'THIN' Body Type Please Enter 'T'\nFor 'OBESSE' Body Type Please Enter 'O'\nFor 'ATHELETE' Body Type Please Enter 'A'\nIf You Are In Quandry About Your Own Body Type Please Enter 'S'")
while True:
    lifestyle = input("What kind of Body Type You Have From The Above: ")
    lifestyle.lower()
    t = "t"
    o = "o"
    a = "a"
    s = "s"
    if lifestyle == t:
        protein = thinp(weight)
        carb = thinc(weight)
        fats = thinf(weight)
        break
    elif lifestyle == o:
        protein =  obbp(weight)
        carb = obbc(weight)
        fats = obbf(weight)
        break
    elif lifestyle == a:
        protein = ap(weight)
        carb = ac(weight)
        fats = af(weight)
        break
    elif lifestyle == s:
        protein = sp(weight)
        carb = sc(weight)
        fats = sf(weight)
        break
    else:
        print("Please Enter Only Given Choices.")
        continue

converted = weight / 0.45
#name
print(f"Your Name: {name}")
# testing
print(f"Your Age: {confirm_age}")
# testing
# testing
print(f"Your Current Weight: {weight} Kgs (Kilograms) , {converted} Lbs (Pounds)")
# testing

print(f'''Protien {protein}
Carbs {carb} 
Fats {fats} ''')


print("Thanks For Using Our Program. Your Soft-Copy Is Generated Named(daily.txt) , Please Consider It For Your Daily Food Intake")
data = open('daily.txt','w')
data.write('''Thanks For Using Our Program Daily Food Intake Calculator
Your All Data Is Here In This Document
 ''')
data.write(f'''Name: {name}
Your Weight: {weight} Kgs(Kilograms) , {converted} Lbs(Pounds)
Your Current Age Approx*: {confirm_age} 
Your Daily Protein Requirement: {protein} Grams 
Your Daily Carbohydrates Requirement: {carb} Grams
Your Daily Fats Requirement: {fats}
''') 
data.close()