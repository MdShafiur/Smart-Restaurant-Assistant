#app.py
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

def Text_to_speech(Message):
    speech = gTTS(text=Message, slow=False, lang="en")
    file_path = r'C:\Users\mdabd\OneDrive\Desktop\CI_SmartRestaurantAssistant\orderingvoice.mp3'
    speech.save(file_path)
    playsound(file_path)
    os.remove(file_path)
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:" + str(e))
            Text_to_speech("Sorry, I didn't get that. Can you please repeat?")
            return get_audio()
    return said

def get_num(a):
    b = str(a)
    speech_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    text_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    if b in speech_num:
        c = speech_num.index(b)
        d = text_num[c]
        return d
    return None

def saveorder(name, quantity, dish, price, current):    
    file = open("foodordering.txt", 'a')
    file.write('\n----------------------------------------------------------------------------------\n' + current)
    file.write('\n{}\n'.format(name))
    file.write('{} {} RM.{}'.format(quantity, dish, price))
    file.close()

def savesameorder(quantity, dish, price):    
    file = open("foodordering.txt", 'a')
    file.write('\n{} {} RM.{}'.format(quantity, dish, price))
    file.close()

pizza1 = "Beef Pepperoni"
pizza2 = "Smokey Chicken Bar-B-Q"
pizza3 = "Veggie Lovers"
pizza4 = "Cheesy Deluxe"

vegroll1 = "Chicken Veggie Roll"
vegroll2 = "Beef Veggie Roll"
vegroll3 = "Veggie Roll With Fries"

bur1 = "Spicy Chicken Burger"
bur2 = "Fish Fillet Burger"
bur3 = "Smokey Beef Burger"

sand1 = "Club Sandwich"
sand2 = "Chicken Crispy Sandwich"
sand3 = "Extreme Veggie Sandwich"

bir1 = "Chicken Biryani"
bir2 = "Deluxe Biryani"
bir3 = "Mandi Rice"

@app.route("/")
def order():
    welcome_message = "Thanks for using our service. Please respond by speaking when it asks you for any input."
    Text_to_speech(welcome_message)
    print("\t\t--------------------------------------------------Smart Restaurant System-------------------------------------------------------\n\n")
    Text_to_speech("Please Enter Your Name: ")
    name = get_audio()

    while True:
        print("\nHello {}\n\nWhat would you like to order?\n\n".format(name))
        Text_to_speech("Hello {}. What would you like to order?".format(name))

        print("\t\t\t\t--------Menu--------\n\n")
        Text_to_speech("1) Pizzas\n2) Burgers\n3) Sandwiches\n4) Veggie Rolls\n5) Biryani")
        Text_to_speech("Please Enter Your choice from 1 to 5")
        choice = get_audio()

        if "1" in choice.lower():
            print("\n1) {}\n2) {}\n3) {}\n4) {}\n".format(pizza1, pizza2, pizza3, pizza4))
            Text_to_speech("Please select your pizza flavor.")
            Text_to_speech("1) {}\n2) {}\n3) {}\n4) {}".format(pizza1, pizza2, pizza3, pizza4))
            Text_to_speech("Please Enter Your choice from 1 to 4")
            pizza_choice = get_audio()

            if "1" in pizza_choice:
                print("\n1) Small RM 8.90\n2) Regular RM 12.90\n3) Large RM 16.90\n")
                Text_to_speech("Please select the size of {}.".format(pizza1))
                Text_to_speech("1) Small RM 8.90\n2) Regular RM 12.90\n3) Large RM 16.90")
                Text_to_speech("Please Enter Your choice from 1 to 3")
                pizza_size_choice = get_audio()

                if "1" in pizza_size_choice:
                    Text_to_speech("Please Enter quantity.")
                    quantity = get_num(get_audio())
                    total_bill = 8.90 * quantity

                elif "2" in pizza_size_choice:
                    Text_to_speech("Please Enter quantity.")
                    quantity = get_num(get_audio())
                    total_bill = 12.90 * quantity

                elif "3" in pizza_size_choice:
                    Text_to_speech("Please Enter quantity.")
                    quantity = get_num(get_audio())
                    total_bill = 16.90 * quantity

                print("\t\t--------Your Order---------\n")
                print("{} {}\n".format(quantity, pizza1))
                print("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes".format(total_bill))
                print("\n\nThank you For Ordering From Smart Restaurant System\n")
                Text_to_speech("Your Total Bill is {}\nYour Order Will be delivered in 20 Minutes. Thank you For Ordering From Smart Restaurant System".format(total_bill))
                if quantity > 1:
                    savesameorder(quantity, pizza1, total_bill)
                else:
                    saveorder(name, quantity, pizza1, total_bill, str(datetime.now()))

        elif "2" in choice.lower():
            print("\n1) {}\n2) {}\n3) {}\n".format(bur1, bur2, bur3))
            Text_to_speech("Please select your burger.")
            Text_to_speech("1) {}\n2) {}\n3) {}".format(bur1, bur2, bur3))
            Text_to_speech("Please Enter Your choice from 1 to 3")
            burger_choice = get_audio()

            # Add handling for burgers...

        elif "3" in choice.lower():
            print("\n1) {}\n2) {}\n3) {}\n".format(sand1, sand2, sand3))
            Text_to_speech("Please select your sandwich.")
            Text_to_speech("1) {}\n2) {}\n3) {}".format(sand1, sand2, sand3))
            Text_to_speech("Please Enter Your choice from 1 to 3")
            sandwich_choice = get_audio()

            # Add handling for sandwiches...

        elif "4" in choice.lower():
            print("\n1) {}\n2) {}\n3) {}\n".format(vegroll1, vegroll2, vegroll3))
            Text_to_speech("Please select your veggie roll.")
            Text_to_speech("1) {}\n2) {}\n3) {}".format(vegroll1, vegroll2, vegroll3))
            Text_to_speech("Please Enter Your choice from 1 to 3")
            veggie_roll_choice = get_audio()

            # Add handling for veggie rolls...

        elif "5" in choice.lower():
            print("\n1) {}\n2) {}\n3) {}\n".format(bir1, bir2, bir3))
            Text_to_speech("Please select your biryani.")
            Text_to_speech("1) {}\n2) {}\n3) {}".format(bir1, bir2, bir3))
            Text_to_speech("Please Enter Your choice from 1 to 3")
            biryani_choice = get_audio()

            # Add handling for biryanis...

        else:
            Text_to_speech("Please Select Right Option.")
            print("Please Select Right Option:\n")

        Text_to_speech("Would you like to order anything else? Please enter yes or no")
        more_orders = get_audio()
        if "no" in more_orders.lower():
            break

    closing_message = "Thanks for ordering with us. Have a nice day!"
    Text_to_speech(closing_message)
    return render_template("order.html")


if __name__ == "__main__":
    app.run()

#end of app.py