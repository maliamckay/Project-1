#Kaitlyn Keesee and Malia McKay Project 1
#(m) means Malia completed this part
#(k) means Kaitlyn completed this part

print ('Hello and welcome to the SAT acceptance requirement program!') #explaining what this program is for

print ('Use this program to enter your SAT scores and find out what popular NC colleges you fit into!') #explaining what interaction will occur between the user and the program

CUMATH = "510" #minimum math score accepted by CU (k)
CURW = "520" #minimum reading and writing score accepted by CU (k)
CUTOTAL = "1030"#minimum totals score accepted by CU


NCSUMATH="“630" #minimum math score accpeted by NCSU (k)
NCSURW = "620" #minimum reading and writing score accepted by NCSU (k)
NCSUTOTAL= "1250" #minimum total score accepted by NCSU (k)


UNCMATH = "640" #minimum math score accepted by UNC (k)
UNCRW= "630" #minimum reading and writing score accepted by UNC (k)
UNCTOTAL = "1270" #minimum total score accepted by UNC (k) 


mathSAT = input('Enter your Math SAT score here:') #here students will input their SAT math score (m)
rwSAT = input('Enter your Reading/Writing SAT score here:') #here students will input their Reading/Writing SAT score (m)
totalscore = int(mathSAT) + int(rwSAT) #adds what score student inputted to calculate total SAT score (m)
print ("Your total SAT score is", totalscore) #(m)

if totalscore == 1600:
	print("Woah! You got a perfect score!")
	#if statement that tells the student they got a perfect score if they received a 1600 (m)

#from here (k)
if totalscore >= int(CUTOTAL):
    print ('Congratulations, you are in the range for Campbell University!')
else:
    print ("I'm sorry, your score needs to improve for Campbell University.")
    #taking total score and comparing it to the required CU scores
    
if totalscore >= int(NCSUTOTAL):
    print ('Congratulations, you are in the range for University of North Carolina!')
else:
    print ("I'm sorry, your score needs to improve for University of North Carolina.")
    #taking total score and comparing it to the required UNC scores

if totalscore >= int(UNCTOTAL):
    print ('Congratulations, you are in the range for North Carolina State University!')
else:
    print ("I'm sorry, your score needs to improve for North Carolina State University.")
    #taking total score and comparing it to the required NCSU scores
#to here (k)


while totalscore in range(800, 1101, 1):
    print ("Your scores are a little low, study hard and try again soon!")
    break
#this takes total score and places it in total range of 800 to 1100 to determine if score is too low (m)
