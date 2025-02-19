
# Quiz
print("Welcome to KBC Quiz!")
print(
  '''You will be awarded 1000 Rs for each correct answer and 0 for wrong answer.'''
)
print("Let's Start !")
score = 0
score = int(score)

m = input('''Q1) Michael Phelps is related to which sport?
(A) Cricket
(B) Billiards
(C) Chess
(D) Swimming
''')
print(end="")
if m.upper() == "D":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer Correct ans is D")

n = input('''Q2) Where is the headquarter of W.T.O ?
(A) New York
(B) Geneva
(C) Uruge
(D) Doha
''')
if n.upper() == "B":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer Correct ans is B")
print("")

o = input('''Q3) When was the Swachh Bharat Abhiyan started?
(A) 1st April 2015
(B) 9 December 2014
(C) 2 October 2014
(D) 26 January 2015
''')
if o.upper() == "C":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is C")

p = input('''Q4 Which is the richest state in India?
(A) Tamil Nadu
(B) Maharashtra
(C) Uttar Pradesh
(D) New Delhi
''')
if p.upper() == "B":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is B")

q = input('''Q5 :Which creature can hold its breath for 6 days?
(A) Spider
(B) Caterpillar
(C) Scopion
(D) Lizard
''')
if q.upper() == "C":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is C")

r = input('''Q6 :Which is the oldest country in world?
(A) Egpyt
(B) San Marino
(C) India
(D) Japan
''')
if r.upper() == "A":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is A")

s = input('''Q7 :Grammy Award is given in the field of ?
(A) Acting
(B) Boxing
(C) Music
(D) Dancing
''')
if s.upper() == "C":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is C")

t = input('''Q8 :Which football player is also known as "Captian America" ?
(A) Christian Pulisic
(B) Timo Werner
(C) Paulo Dybala
(D) Neymar
''')
if t.upper() == "A":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is A")

u = input('''Which is the longest National Highway in India?
(A) NH-44
(B) NH-1
(C) NH-2
(D) NH-10
''')
if u.upper() == "A":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is A")

v = input('''10) Which is cleanest city in India ?
(A) Jaipur
(B) Indore
(C) Kochi
(D) Surat 
''')
if v.upper() == "B":
  print("Correct Answer")
  score = score + 1000
else:
  print("Wrong Answer correct ans is B")
  print("")

# Result
print("Your total score is " + str(score), "Rs")
