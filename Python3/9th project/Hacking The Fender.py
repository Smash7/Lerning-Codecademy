# 1.
import csv
# 12.
import json

# 2-7
with open('passwords.csv') as usrs_csv:
    usrs_reader = csv.DictReader(usrs_csv)
    compromised_users = [usrs['Username'] for usrs in usrs_reader]

# 8-11
with open('compromised_users.txt', 'w') as compromised_user_file:
    for compromised_user in compromised_users:
        compromised_user_file.write(compromised_user)

# 13-15
with open('boss_message.json', 'w') as boss_message:
    boss_message_dict = {"recipient": "The Boss",
                         "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)

# 16-19
with open('new_passwords.csv', 'w') as new_passwords_obj:
    slash_null_sig = """
                     _  _     ___   __  ____             
                    / )( \   / __) /  \(_  _)            
                    ) \/ (  ( (_ \(  O ) )(              
                    \____/   \___/ \__/ (__)             
                     _  _   __    ___  __ _  ____  ____  
                    / )( \ / _\  / __)(  / )(  __)(    \ 
                    ) __ (/    \( (__  )  (  ) _)  ) D ( 
                    \_)(_/\_/\_/ \___)(__\_)(____)(____/ 
                            ____  __     __   ____  _  _ 
                     ___   / ___)(  )   / _\ / ___)/ )( \\
                    (___)  \___ \/ (_/\/    \\\___ \) __ (
                           (____/\____/\_/\_/(____/\_)(_/
                     __ _  _  _  __    __                
                    (  ( \/ )( \(  )  (  )               
                    /    /) \/ (/ (_/\/ (_/\             
                    \_)__)\____/\____/\____/
                    """
    new_passwords_obj.write(slash_null_sig)
