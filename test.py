import os
from Plant import Plant


#Clear terminal before running any code 
os.system('cls')

aloe = Plant(ID=1, schedule=1, name="aloemar")

print("ID is: ", aloe.ID)
print("Schedule is: ", aloe.schedule)
print("Name is: ", aloe.name)
