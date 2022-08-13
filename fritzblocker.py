from fritzconnection.lib.fritzphonebook import FritzPhonebook
from fritzconnection.lib.fritzcall import FritzCall
from os import environ

if __name__ == "__main__":
    fb_user = environ.get("FRITZBLOCKER_USER")
    fb_pass = environ.get("FRITZBLOCKER_PASS")

    if fb_pass and fb_user:
        fp = FritzPhonebook(address='192.168.178.1', user=fb_user,password=fb_pass)
        for phonebook_id in fp.phonebook_ids:
            contacts = fp.get_all_names(phonebook_id)
            for name, numbers in contacts.items():
                print(name, numbers)

        fc = FritzCall(address="192.168.178.1", user=fb_user,password=fb_pass)
        calls = fc.get_calls()
        for call in calls:
            print (call)
        fp.