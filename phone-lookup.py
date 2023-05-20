from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ENTER YOURS HERE'
auth_token = 'ENTER YOURS HERE'
client = Client(account_sid, auth_token)
number = str(input("Please input the phone number to lookup including the country code with +1 and NO spaces or dashes: "))

phone_check1 = client.lookups \
   .phone_numbers(number) \
   .fetch(add_ons='icehook_scout')

phone_check2 = client.lookups \
   .phone_numbers(number) \
   .fetch(add_ons='nomorobo_spamscore') \
   .add_ons['results']['nomorobo_spamscore']['result']['score']

phone_check3 = client.lookups \
   .phone_numbers(number) \
   .fetch(add_ons='twilio_carrier_info')

phone_check4 = client.lookups \
   .phone_numbers(number) \
   .fetch(add_ons='twilio_caller_name')

print("\nIcehook:\n")
data_phone1 = phone_check1.add_ons
data_values = list(data_phone1['results']['icehook_scout']['result'].values())
data_keys = list(data_phone1['results']['icehook_scout']['result'].keys())

i = 0
while(i < len(data_keys) - 1):
    print(str(data_keys[i]) + ":" + " " + str(data_values[i]))
    i += 1
    
if(phone_check2 == 0):
    value = "FALSE"
else:
    value = "TRUE"
print("\n\nNomorobo:\n")
print("Result: " + value)

print("\n\nTwilio Carrier Info:\n")
data_phone3 = phone_check3.add_ons
print("Carrier name: " + str(data_phone3['results']['twilio_carrier_info']['result']['carrier']['name']))
print("Number type: " + str(data_phone3['results']['twilio_carrier_info']['result']['carrier']['type']))

print("\n\nTwilio Caller Name:\n")
data_phone4 = phone_check4.add_ons
print("Caller Name: " + str(data_phone4['results']['twilio_caller_name']['result']['caller_name']['caller_name']))
