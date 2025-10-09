# in following code problem solving is to calculate exact full Euro per person, the 500 euro cannot be
# devided to 3, we have float, but we want to calculate fix Euro without cent for each persons
geld = 500
mostafa = 0
gleb = 0
olga = 0

restgeld = geld % 3 # in this case restgeld is 2
teilbareGeld = geld - restgeld # in this case 498
mostafa = teilbareGeld/3
print (f"mostafa tasche:" + str(mostafa))