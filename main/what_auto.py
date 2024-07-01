import pywhatkit as kit
import time

def send_whatsapp_message(phone_number, message):
    try:
        kit.sendwhatmsg_instantly(phone_number, message, 10, True, 2)
        print(f"Message sent to {phone_number}")
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")




'''print("enter the number to whom you wish to send the message:")
number = input()

print("enter the message you wish to send:")
msg = input()

send_whatsapp_message(number,msg)'''