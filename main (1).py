age = int(input("what is your age?"))

if age >= 17:
  print ("You can see R rated movie alone")
  
elif age >= 13:
  print ("You can see PG 13 movies alone")
  
elif age >= 5:
  print ("You can see G or PG movies alone")

else:
  print ("You are way too young for movies")