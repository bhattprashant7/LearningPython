import time
import random

# ANSI color codes
colors = [
    "\033[31m", "\033[32m", "\033[33m",
    "\033[34m", "\033[35m", "\033[36m", "\033[37m"
]

reset = "\033[0m"

lyrics = """
Mann jogiyaa jogiyaa, ik tu hi jog hai mera.. 
Dil ho gayaa, rogiyaa, aur tu hi rog hai mera.. 
Mann jogiyaa jogiyaa, ik tu hi jog hai mera.. 
Dil ho gayaa, rogiyaa, aur tu hi rog hai mera.. 


Umar bhar main teri, parwaah karun..
Ke marr jaoon jo tujhe, ruswa karun..
Tu sapne dekhe jinhe main, poora karun..
Ke ab toh Rab bhi hai dooja, pehlaa hai tu..

Neh ka dhaaga, jo laaga yun, Naa tod jaana tu..
Naa chhod jaana tu.. Naa chhod jaana tu.. 
Neh ka dhaaga, jo laaga yun, Naa tod jaana tu..
Naa chhod jaana tu.. Naa chhod jaana tu.. 

Tere bina main, mere bina tu.. Jachataa nahi..
Dil pe jo naam, aur koi.. Rachataa nahi..
Tere bina main, mere bina tu.. Jachataa nahi..
Dil pe jo naam, aur koi.. Rachataa nahi..

Haan sang tera zaroori hai, Naa ab manzoor doori hai..
Mere hansne pe rone pe, Haq bus hai tera..

Ke har Subha dekhun main, chehra tera..
Tu saansein ban jaa main dhadkoon, dil ki tarah..
Haan meri palkon se ojhal, hona tu naa..
Ke tujhko dekhe bina naa, reh paunga..

Mann jogiyaa jogiyaa, ik tu hi jog hai ............
Dil ho gayaa, rogiyaa, aur tu hi rog hai mera.. 
Mann jogiyaa jogiyaa, ik tu hi jog hai ............
Dil ho gayaa, rogiyaa, aur tu hi rog hai mera.. 


"""

lines = lyrics.strip().split("\n")

for line in lines:
    words = line.split()
    for w in words:
        color = random.choice(colors)
        for ch in w:                 # print letter by letter
            print(color + ch + reset, end="", flush=True)
            time.sleep(0.25)         # delay per letter
        print(" ", end="", flush=True)
        time.sleep(0.05)             # delay after each word
    print()
