number_1 = input("Tell me a Number: ")
time_frame = input("Give me a Measure of Time: ")
transportation = input("Tell me a Mode of Transportation: ")
adjective_1 = input("Tell me an Adjective: ")
adjective_2 = input("Tell me another Adjective: ")
noun_1= input("Give me a Noun: ")
color = input("Name a Color: ")
part_body_1 = input("Tell me a Part of the Body: ")
verb = input("Give me a Verb: ")
number_2 = input("Give me a Number once more: ")
noun_2 = input("Give me a Noun again: ")
noun_3 = input("Another Noun: ")
part_body_2 = input("An example of a Part of the Body: ")
noun_4 = input("Tell me a Noun: ")
adjective_3 = input("Give an Adjective: ")
silly_word = input("Tell me a Silly Word: ")

madLip = f"""
It was about {number_1} {time_frame} ago when I arrived at the hospital in a {transportation}. The hospital is a/an {adjective_1} place, 
there are a lot of {adjective_2} {noun_1} here. There are nurses here who have {color} {part_body_1}. If someone wants to come into my room,
I told them that they have to {verb} first. I've decorated my room with {number_2} {noun_2}.Today I talked to a doctor and they were wearing a {noun_3} on their {part_body_2}. I heard that
all doctors {verb} {noun_4} every day for breakfast. The most {adjective_3} thing about being in the hospital is the {silly_word} {noun_1} !
"""

print(madLip)
