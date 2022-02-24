'''
Tracks the location of a phone number.
'''
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier, timezone

def getCallerInfo(phonenumber):
    
    #Country and History
    ch_number = phonenumbers.parse(phonenumber, "CH")
    #Takes in number and outputs location in english
    print("Location: ")
    print(str(geocoder.description_for_number(ch_number, "en")))
    
    #Get service provider
    service_nmber = phonenumbers.parse(phonenumber, "RO")
    print("\nService Provider: ")
    print(str(carrier.name_for_number(service_nmber,"en")))

    
    gb_number = phonenumbers.parse(phonenumber,"GB")
    print("TimeZone: ")
    print(str(timezone.time_zones_for_number(gb_number)))
    
    

if __name__ == "__main__":
    nationalNumber = "+" + input("Enter Country Code (US: 1): ")
    phonenumber = input("Enter the phone number you want to trace (no spaces): ")
    total_phonenumber = nationalNumber + phonenumber
    print("Looking up phone number: {}\n".format(total_phonenumber))
    getCallerInfo(total_phonenumber)
    
    
    