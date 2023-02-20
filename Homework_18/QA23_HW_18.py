#1) Get user name 

# Expect : “jOhN”

# Result  : ”John” 

name="jOhN"
print(name.capitalize())

#2) Get user surname and split it by latter 

# DOE
# D O E 

surname = "DOE"
print(" ".join(surname))

# 3) Get user age and return year of birth 

user_age=input("Age: ")
import datetime 
year_of_birth=datetime.date.today().year-int(user_age)
print("Year of birth: ",year_of_birth)

# 4) Equal userAge and : 15 ; 23 ;13 and print it to the screen ;

# To every option use : <= , >= , < , > , ==

# int()

user_name=input("What is your name?: ")
user_surname=input("What is your surname?: ")
user_age=input("How old are you?: ")
if int (user_age)<13:
    print (user_name)
if int(user_age)  >=13 and int(user_age)<=23:
    print ("Teenager") 
if int(user_age)==23:
     print(user_name)
if int(user_age)>23:
    print(user_surname)    

# 5)
# Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laudantium nihil  laborum rerum ipsum iure dicta officiis, necessitatibus non vel excepturi minima
# quia fugiat hic numquam suscipit harum laboriosam magni quasi veniam voluptas
# eius sapiente aperiam vero? Eum ducimus consequuntur, accusamus tempore corporis
# numquam animi hic ad voluptatem saepe mollitia voluptate explicabo soluta earum!
# Consequatur porro eos minus facilis mollitia alias nesciunt. Molestias explicabo
# alias ea praesentium placeat ex ad maxime ipsam non velit architecto, iure
# laborum reiciendis pariatur dolorem amet nulla dolor quos a esse atque vel? Fuga
# quidem perspiciatis velit iure excepturi. Delectus velit amet distinctio error
# temporibus at voluptas suscipit laboriosam rerum ea, quibusdam nesciunt maiores
# quas necessitatibus fugit veniam, molestiae inventore dignissimos voluptatum
# libero enim natus! Cum, corrupti ad.

# -Find “ad” position 
# -Slice “ad” from text
# -Replace all “Lorem” on “Hey you”
expression ="""Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laudantium nihil  laborum rerum ipsum iure dicta officiis, necessitatibus non vel excepturi minima
quia fugiat hic numquam suscipit harum laboriosam magni quasi veniam voluptas
eius sapiente aperiam vero? Eum ducimus consequuntur, accusamus tempore corporis
numquam animi hic ad voluptatem saepe mollitia voluptate explicabo soluta earum!
Consequatur porro eos minus facilis mollitia alias nesciunt. Molestias explicabo
alias ea praesentium placeat ex ad maxime ipsam non velit architecto, iure
laborum reiciendis pariatur dolorem amet nulla dolor quos a esse atque vel? Fuga
quidem perspiciatis velit iure excepturi. Delectus velit amet distinctio error
temporibus at voluptas suscipit laboriosam rerum ea, quibusdam nesciunt maiores
quas necessitatibus fugit veniam, molestiae inventore dignissimos voluptatum
libero enim natus! Cum, corrupti ad."""
print(expression.find("ad"))
ad=expression[expression.find("ad"):]
print(ad)
txt=expression.replace("Lorem", "Hey you")
print(txt)