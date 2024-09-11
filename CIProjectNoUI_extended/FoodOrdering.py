import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime



def Text_to_speech(Message):
    speech = gTTS(text=Message, slow=False, lang="en")
    file_path = r'C:\Users\mdabd\OneDrive\Desktop\CI_SmartRestaurantAssistant\orderingvoice.mp3'
    speech.save(file_path)
    playsound(file_path)
    os.remove(file_path)
    
def get_audio():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
		said=""

		try:
			said=r.recognize_google(audio)
			print(said)
				
		except Exception as e:
			print("Exception:"+str(e))
			#Text_to_speech("sorry i didn't get that, can you please repeat")
			#get_audio()
	return said	
	
				
def get_num(a):
	b=str(a)
	
	speech_num=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
	text_num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
	if b in speech_num:
		c=speech_num.index(b)
		d=text_num[c]
	return d



def saveorder(name,quantity,dish,price,current):	
	file=open("foodordering.txt",'a')
	file.write('\n----------------------------------------------------------------------------------\n'+current)
	file.write('\n{}\n'.format(name))
	file.write('{} {} RM.{}'.format(quantity,dish,price))
	file.close()

def savesameorder(quantity,dish,price):	
	file=open("foodordering.txt",'a')
	file.write('\n{} {} RM.{}'.format(quantity,dish,price))
	file.close()


pizza1="Beef Pepperoni"; pizza2="Smokey Chicken Bar-B-Q"; pizza3="Veggie Lovers"; pizza4="Cheesy Deluxe"
vegroll1="Chicken Veggie Roll"; vegroll2="Beef Veggie Roll"; vegroll3="Veggie Roll With Fries"
bur1="Spicy Chicken Burger"; bur2="Fish Fillet Burger"; bur3="Smokey Beef Burger"
sand1="Club Sandwich"; sand2="Chicken Crispy Sandwich"; sand3="Extreme Veggie Sandwich"
bir1="Chicken Biryani"; bir2="Deluxe Biryani"; bir3="Mandi Rice"
choice=0;gotostart="yes"
count=0

Text_to_speech("Thanks for using our service. Please respond by speaking when it asks you for any input.")
print("\t\t--------------------------------------------------Smart Restaurant System-------------------------------------------------------\n\n")
print("Please Enter Your Name: ")
Text_to_speech("Please Enter Your Name: ")
name=get_audio()


while gotostart=="yes":

		count+=1
		dt=datetime.now()
		current=str(dt)
		
		print("\t\t--------------------------------------------------Smart Restaurant System-------------------------------------------------------\n\n")
   
		print("Hello {}\n\nWhat would you like to order?\n\n".format(name))
		Text_to_speech("Hello {}\n\nWhat would you like to order?\n\n".format(name))

		print("\t\t\t\t--------Menu--------\n\n")

		Text_to_speech("enter 1 for pizzas 2 for burgers 3 for sandwich 4 for Veggie rolls 5 for biryani")
		print("1) Pizzas\n")
		print("2) Burgers\n")
		print("3) Sandwich\n")
		print("4) Veggie Rolls\n")
		print("5) Biryani\n\n")
		Text_to_speech("Please Enter Your choice from 1 to 5")
		choice= get_audio()  
	

		if "1" in choice: 
			Text_to_speech("Please select Your flavour")
			print("\n1){}\n".format(pizza1))
			print("2){}\n".format(pizza2))
			print("3){}\n".format(pizza3))
			print("4){}\n".format(pizza4))

			Text_to_speech("enter 1 for {} 2 for {} 3 for {} 4 for {}".format(pizza1,pizza2,pizza3,pizza4))
			#Text_to_speech("{}".format(pizza1)); Text_to_speech("{}".format(pizza2)); Text_to_speech("{}".format(pizza3)); Text_to_speech("{}".format(pizza4))
			Text_to_speech("Please Enter Your choice from 1to4")
			a= get_audio()  
			pchoice=get_num(a)#get_audio()
		
			if pchoice>=1 and pchoice<=5:
				print("\n1) Small RM 8.90\n2) Regular RM 12.90\n3) Large RM 16.90\n")
				Text_to_speech("please select pizza size 1Small RM8.90 2Regular RM12.90 3Large RM16.90")
				Text_to_speech("Please Enter Your choice from 1to3")
				a= get_audio()         
				pchoice1=get_num(a)#get_audio()

				if pchoice1>=1 and pchoice1<=3:
					Text_to_speech("Please Enter quantity")
					a=get_audio()
					quantity=get_num(a)#get_audio()
					
			
					if pchoice1==1:
						choice = 8.90*quantity
						

					elif pchoice1==2:
							choice = 12.90*quantity
							
		        
					elif pchoice1==3:
							choice = 16.90*quantity
							


			
			if pchoice==1:
				print("\t\t\t--------Your Order---------\n")
				print("{} {}".format(quantity,pizza1))
				print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
				print("\n\nThank you For Ordering From Smart Restaurant System\n")
				Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
				if count>1 :
					savesameorder(quantity,pizza1,choice)
				else:
					saveorder(name,quantity,pizza1,choice,current)

			elif pchoice==2:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,pizza2))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System\n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
					if count>1 :
						savesameorder(quantity,pizza2,choice)
					else:
						saveorder(name,quantity,pizza2,choice,current)

			elif pchoice==3:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,pizza3))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System\n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
					if count>1 :
						savesameorder(quantity,pizza3,choice)
					else:
						saveorder(name,quantity,pizza3,choice,current)

			elif pchoice==4:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,pizza4))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System\n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
					if count>1 :
						savesameorder(quantity,pizza4,choice)
					else:
						saveorder(name,quantity,pizza4,choice,current)


			Text_to_speech("Would you like to order anything else please enter yes or no")
			gotostart=get_audio()
			
			



		

	 


		elif "2" in choice:
	 
				print("\n1 {} RM 18\n".format(bur1))
				print("2 {} RM 15\n".format(bur2))
				print("3 {} RM 16\n".format(bur3))
				Text_to_speech("1 {} RM18. 2 {} RM15. 3 {} RM16".format(bur1,bur2,bur3))
				Text_to_speech("Please Enter Your choice from 1to3")
				a=get_audio()
				pchoice1=get_num(a)
		
				if pchoice1>=1 and pchoice1<=3:
					Text_to_speech("Please Enter quantity")
					a=get_audio()
					quantity=get_num(a)
			
					if pchoice1==1:
						choice = 18*quantity
						
					elif pchoice1==2:
							choice = 15*quantity
							

					elif pchoice1==3:
							choice = 16*quantity
							

			
			      
				if pchoice1==1:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,bur1))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System \n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
					if count>1 :
						savesameorder(quantity,bur1,choice)
					else:
						saveorder(name,quantity,bur1,choice,current)

				elif pchoice1==2:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,bur2))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
						if count>1 :
							savesameorder(quantity,bur2,choice)
						else:
							saveorder(name,quantity,bur2,choice,current)

				elif pchoice1==3:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,bur3))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
						if count>1 :
							savesameorder(quantity,bur3,choice)
						else:
							saveorder(name,quantity,bur3,choice,current)


				Text_to_speech("Would you like to order anything else please enter yes or no")
				gotostart=get_audio()

			
			


		elif "3" in choice:
				print("\n1) {} RM.10\n".format(sand1))
				print("2) {} RM.8\n".format(sand2))
				print("3) {} RM.6.50\n".format(sand3))
				Text_to_speech("1 {} RM10. 2 {} RM8. 3 {} RM6.50".format(sand1,sand2,sand3))
				Text_to_speech("Please Enter Your choice from 1to3")
				a=get_audio()
				pchoice1=get_num(a)
		
				if pchoice1>=1 and pchoice1<=3:
					Text_to_speech("Please Enter quantity")
					a=get_audio()
					quantity=get_num(a)
			
					if pchoice1==1:
						choice = 10*quantity
						

					elif pchoice1==2:
							choice = 8*quantity
							

					elif pchoice1==3:
							choice = 6.50*quantity
							

			
			
				if pchoice1==1:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,sand1))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System\n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
					if count>1 :
						savesameorder(quantity,sand1,choice)
					else:
						saveorder(name,quantity,sand1,choice,current)

				elif pchoice1==2:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,sand2))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
						if count>1 :
							savesameorder(quantity,sand2,choice)
						else:
							saveorder(name,quantity,sand2,choice,current)

				elif pchoice1==3:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,sand3))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
						if count>1 :
							savesameorder(quantity,sand3,choice)
						else:
							saveorder(name,quantity,sand3,choice,current)

				Text_to_speech("Would you like to order anything else please enter yes or no")
				gotostart=get_audio()
				
			

		elif "4" in choice:
				print("\n1) {} RM.9\n".format(vegroll1))
				print("2) {} RM.5\n".format(vegroll2))
				print("3) {} RM.7\n".format(vegroll3))
				Text_to_speech("1 {} RM9. 2 {} RM5. 3{} RM7".format(vegroll1,vegroll2,vegroll3))
				Text_to_speech("Please Enter Your choice from 1to3")
				a=get_audio()
				pchoice1=get_num(a)
		
				if pchoice1>=1 and pchoice1<=3:
					Text_to_speech("Please Enter quantity")
					a=get_audio()
					quantity=get_num(a)
			
					if pchoice1==1:
						choice = 9*quantity
						

					elif pchoice1==2:
							choice = 5*quantity
							

					elif pchoice1==3:
							choice = 7*quantity
							

			
			
				if pchoice1==1:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,vegroll1))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System\n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
					if count>1 :
						savesameorder(quantity,vegroll1,choice)
					else:
						saveorder(name,quantity,vegroll1,choice,current)

				elif pchoice1==2:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,vegroll2))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
						if count>1 :
							savesameorder(quantity,vegroll2,choice)
						else:
							saveorder(name,quantity,vegroll2,choice,current)

				elif pchoice1==3:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,vegroll3))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(choice))
						if count>1 :
							savesameorder(quantity,vegroll3,choice)
						else:
							saveorder(name,quantity,vegroll3,choice,current)

				Text_to_speech("Would you like to order anything else please enter yes or no")
				gotostart=get_audio()
			

 

		elif "5" in choice:
				print("\n1) {} RM.16\n".format(bir1))
				print("2) {} RM.22\n".format(bir2))
				print("3) {} RM.14\n".format(bir3))
				Text_to_speech("1 {} RM16. 2 {} RM22. 3 {} RM14".format(bir1,bir2,bir3))
				Text_to_speech("Please Enter Your choice from 1to3")
				a=get_audio()
				pchoice1=get_num(a)
		
				if pchoice1>=1 and pchoice1<=3:
					Text_to_speech("Please Enter quantity")
					a=get_audio()
					quantity=get_num(a)
			
					if pchoice1==1:
						choice= 16*quantity
						

					elif pchoice1==2:
							choice = 22*quantity
						

					elif pchoice1==3:
							choice = 14*quantity
						

			
			
				if pchoice1==1:
					print("\t\t--------Your Order---------\n")
					print("{} {}".format(quantity,bir1))
					print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
					print("\nThank you For Ordering From Smart Restaurant System\n")
					Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant Assistant".format(choice))
					if count>1 :
						savesameorder(quantity,bir1,choice)
					else:
						saveorder(name,quantity,bir1,choice,current)

				elif pchoice1==2:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,bir2))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant Assistant".format(choice))
						if count>1 :
							savesameorder(quantity,bir2,choice)
						else:
							saveorder(name,quantity,bir2,choice,current)

				elif pchoice1==3:
						print("\t\t--------Your Order---------\n")
						print("{} {}".format(quantity,bir3))
						print("\nYour Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(choice))
						print("\nThank you For Ordering From Smart Restaurant System\n")
						Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant Assistant".format(choice))		
						if count>1 :
							savesameorder(quantity,bir3,choice)
						else:
							saveorder(name,quantity,bir3,choice,current)

				Text_to_speech("Would you like to order anything else please enter yes or no")
				gotostart=get_audio()
	
			
		else:
				Text_to_speech("Please Select Right Option. Would you like to start the program again please enter yes or no")
				print("Please Select Right Option:\n Would you like to start the program again please enter yes or no")
				gotostart=get_audio()
				



Text_to_speech("Thanks for ordering with us. Have a nice day")
print("\nThanks for ordering with us...Have a nice day :)")