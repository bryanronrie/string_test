def string_test(string):

	str=0	str_=0

	for s in string:

		if(s.isupper()):

			str+=1

		

		if(s.islower()):

			str_+=1	

	print("The number of lowercase letters is :")

	print(str_)

	print("The number of uppercase letters is :")

	print(str)

	

string_test("You are a Student of 30days0fcode")
