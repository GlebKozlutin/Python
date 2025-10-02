def ageMachine(age : int):
    if age > 50:
        print("Du bist alt geworden")
    else:
        print("aha.eines Tages du wirst Alt auch")

def addTwoNumber(first_number:int,second_number:int)->int:
    return first_number+second_number

print("Wie alt bist du?")

age_from_user = input()
age_from_user = int(age_from_user)

ageMachine(age_from_user)







