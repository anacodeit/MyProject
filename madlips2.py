#i needed input from the user first. For that I used the input function

noun_name = input("Give me a Proper Noun or a Person's Name: ")
noun_1 = input("Give me a Noun: ")
feeling_1 = input("Adjective that conveys a Feeling: ")
verb_1 = input("Give me a Verb:  ")
feeling_2 = input("Give me another Adjective that conveys a Feeling: ")
animal = input("Name an Animal: ")
verb_2 = input("Give me another Verb: ")
color = input("Name a Color: ")
verb_ing = input("Give me a Verb ending with 'ing': ")
adverb_ly = input("Name an Adverb ending with 'ly': ")
number = input("Give me a Number: ")
measure_of_time = input("Give me a Measure of Time: ") #COLOR had to be used after this line, same for the ANIMAL, same for NUMBER
silly_word = input("Tell me Silly Word: ")
noun_2 = input("Give a noun again: ")


madLibs2 = f"""
This weekend I am going camping with {noun_name}. I packed my lantern, sleeping bag, and {noun_1}.
I am so {feeling_1} to {verb_1} in a tent. I am {feeling_2} we might see a(n) {animal}. I heard they're kind of dangerous.
While we're camping, we are going to hike, fish and {verb_2}. I have heard that the {color} lake is great for {verb_ing}.
Then we will {adverb_ly} hike through the forest for {number} {measure_of_time}. If  I see a {color} {animal} while hiking.
I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun_2} around the
campfire!

"""
print(madLibs2)
