def main_menu():
    main_menu = """
========================= MAIN MENU ===========================
                          [Press]

                          1.  Phone book
                          2.  Messages
                          3.  Chat
                          4.  Call register
                          5.  Tones
                          6.  Settings
                          7.  Call divert
                          8.  Music
                          9.  Games
                          10. Calculator
                          11. Reminders
                          12. Clock
                          13. Profiles
                          14. Services
                          15. SIM services
                          0.  Turn off
================================================================
"""

    while True:
        print(main_menu)
        menu_choice = input("Enter the number: ")

        match menu_choice:
            case "1":   phone_book_menu()
            case "2":   messages_menu()
            case "3":   print("Chat")
            case "4":   call_register_menu()
            case "5":   tones_menu()
            case "6":   settings_menu()
            case "7":   print("Call divert")
            case "8":   music_menu()
            case "9":   print("Games")
            case "10":  print("Calculator")
            case "11":  print("Reminders")
            case "12":  clock_menu()
            case "13":  print("Profiles")
            case "14":  print("Services")
            case "15":  print("SIM services")
            case "0":   print("Nokia phone turned off.")
                        break
            case _:     print("Invalid")


def phone_book_menu():
    phone_book = """

================== PHONE BOOK ==========================
                Press[Menu] and then [select]

                1.  Search
                2.  Service Nos.
                3.  Add name
                4.  Erase
                5.  Edit
                6.  Copy
                7.  Assign tone
                8.  Send b"card
                9.  Options
                10. Speed dials
                11. Voice tags
                0.  Back
                99. Home
=========================================================

"""

    while True:
        print(phone_book)
        press_phone_book = input("Enter the number: ")

        match press_phone_book:
            case "99":
                return
            case "0":
                break

            case "1":   print("Search")
            case "2":   print("Service Nos.")
            case "3":   print("Add name")
            case "4":   print("Erase")
            case "5":   print("Edit")
            case "6":   print("Copy")
            case "7":   print("Assign tone")
            case "8":   print('Send your b"card')
            case "9":   print("Options")

                        options = """
============================ OPTIONS ====================================
                            [Select]
                            1.  Memory in use
                            2.  Type of view
                            3.  Memory status
                            0.  Back
                            99. Home
=========================================================================

"""

                        while True:
                            print(options)
                            sub_options = input("Enter the number: ")

                            match sub_options:
                                case "99":
                                    return
                                case "0":
                                    break

                                case "1":   print("Memory in use")
                                case "2":   print("Type of view")
                                case "3":   print("Memory status")
                                case _:     print("Invalid")

            case "10":
                print("Speed dials")
            case "11":
                print("Voice tags")
            case _:
                print("Invalid")

def messages_menu():
    messages = """
========================= MESSAGES ================================

                         Press[Menu] and then [select]

                         1.  Write messages
                         2.  Inbox
                         3.  Outbox
                         4.  Picture messages
                         5.  Templates
                         6.  Smileys
                         7.  Message settings
                         8.  info service
                         9.  Voice mailbox number
                         10. Service command editor
                         0.  Back
                         99. Home
===================================================================

"""

    while True:
        print(messages)
        sms_messages = input("Enter the number: ")

        match sms_messages:
            case "99":
                return
            case "0":
                break

            case "1":   print("Write a message")
            case "2":   print("Inbox")
            case "3":   print("Outbox")
            case "4":   print("Picture messages")
            case "5":   print("Templates")
            case "6":   print("Smileys")
            case "7":   print("Message settings")

                        message_settings = """
============================= MESSAGE SETTINGS =================================
                              Options[Select]
                              1.  Set 1
                              2.  Common
                              0.  Back
                              99. Home
================================================================================
"""

                        while True:
                            print(message_settings)
                            subOptions1 = input("Input Number Choice: ")

                        match subOptions1:
                            case "99":
                                return
                            case "0":
                                break

                            case "1":
                                print("Set")

                                set_menu = """
================================ SET ================================
                              [Select]
                              1.  Message centre number
                              2.  Message sent as
                              3.  Message validity
                              0.  Back
                              99. Home
=====================================================================
"""

                                while True:
                                    print(set_menu)
                                    subOption2 = input("Input Number Choice: ")

                                    match subOption2:
                                        case "99":
                                            return
                                        case "0":
                                            break

                                        case "1":   print("Message centre number")
                                        case "2":   print("Message sent as")
                                        case "3":   print("Message validity")
                                        case _:     print("Invalid")

                            case "2":
                                print("Common")

                                common = """
================================= COMMON ===================================
                                [Select]
                                1.  Delivery reports
                                2.  Reply via same centre
                                3.  Character support
                                0.  Back
                                99. Home
============================================================================
"""

                                while True:
                                    print(common)
                                    subOption3 = input("Input Number Choice: ")

                                    match subOption3:
                                        case "99":
                                            return
                                        case "0":
                                            break

                                        case "1":   print("Delivery reports")
                                        case "2":   print("Reply via same centre")
                                        case "3":   print("Character support")
                                        case _:     print("Invalid")

                            case _:
                                print("Invalid")

            case "8":
                print("Info service")
            case "9":
                print("Voice mailbox number")
            case "10":
                print("Service command editor")
            case _:
                print("Invalid")


def call_register_menu():
    call_register = """
============================= CALL REGISTER ================================

                            Press[Menu] and then [select]
                            1.  Missed calls
                            2.  Received calls
                            3.  Dialled numbers
                            4.  Erase recent call lists
                            5.  Show call duration
                            6.  Show call costs
                            7.  Call cost settings
                            8.  Prepaid credit
                            0.  Back
                            99. Home
============================================================================

"""

    while True:
        print(call_register)
        register = input("Input Number Choice: ")

        match register:
            case "99":
                return
            case "0":
                break

            case "1":   print("Missed calls")
            case "2":   print("Received calls")
            case "3":   print("Dialled numbers")
            case "4":   print("Erased recent call lists")
            case "5":   print("Call duration")

                        call_duration = """
================================== CALL DURATION ===============================
                                  [Select]
                                  1.  Last call duration
                                  2.  All calls' duration
                                  3.  Received calls' duration
                                  4.  Dialled calls' duration
                                  5.  Clear timers
                                  0.  Back
                                  99. Home
================================================================================
"""

                        while True:
                            print(call_duration)
                            duration = input("Input Number Choice: ")

                            match duration:
                                case "99":
                                    return
                                case "0":
                                    break

                                case "1":   print("Last call duration")
                                case "2":   print("All calls' duration")
                                case "3":   print("Received calls' duration")
                                case "4":   print("Dialled calls' duration")
                                case "5":   print("Clear timers")
                                case _:     print("Invalid")

            case "6":
                print("Show call costs")

                call_costs = """
================================ CALL COSTS ===============================
                                [Selects]
                                1.  Last call costs
                                2.  All calls' cost
                                3.  Clear counters
                                0.  Back
                                99. Home
===========================================================================
"""

                while True:
                    print(call_costs)
                    costs = input("Input Number Choice: ")

                    match costs:
                        case "99":
                            return
                        case "0":
                            break

                        case "1":   print("Last call costs")
                        case "2":   print("All calls' cost")
                        case "3":   print("Clear counters")
                        case _:     print("Invalid")

            case "7":
                print("Call Cost Settings")

                call_cost_settings = """
=================================== CALL COST SETTINGS ==============================
                                  [Select]
                                  1.  Call cost limit
                                  2.  Show costs in
                                  0.  Back
                                  99. Home
=====================================================================================
"""

                while True:
                    print(call_cost_settings)
                    cost_settings = input("Input Number Choice: ")

                    match cost_settings:
                        case "99":
                            return
                        case "0":
                            break

                        case "1":   print("Call cost limit")
                        case "2":   print("Show cost in")
                        case _:     print("Invalid")

            case "8":
                print("Prepaid credit") 
            case _:
                print("Invalid")

def tones_menu():
    tones = """
============================== TONES ================================
                           Press[Menu] and then [select]
                           1. Ringing tone
                           2. Ringing volume
                           3. Incoming call alert
                           4. Message alert tone
                           5. Keypad tones
                           6. Warning tones
                           7. Vibrating alert
                           8. Screen saver
                           0. Back
                           99. Home
======================================================================

"""

    while True:
        print(tones)
        tone_list = input("Input Number Choice: ")

        match tone_list:
            case "99":
                return
            case "0":
                break

            case "1":   print("Ringing tone")
            case "2":   print("Ringing volume")
            case "3":   print("Incoming call alert")
            case "4":   print("Message alert tone")
            case "5":   print("Keypad tones")
            case "6":   print("Warning tones")
            case "7":   print("Vibrating alert")
            case "8":   print("Screen saver")
            case _:     print("Invalid")

def settings_menu():
    settings = """
============================== SETTINGS =================================
                              Press[Menu] and then [select]
                              1.  Call settings
                              2.  Phone settings
                              3.  Security settings
                              4.  Restore factory settings
                              0.  Back
                              99. Home
=========================================================================

"""

    while True:
        print(settings)
        setting_lists = input("Input Number Choice: ")

        match setting_lists:
            case "99":
                return
            case "0":
                break

            case "1":
                print("Call settings")

                call_settings = """
================================== CALL SETTINGS ===============================
                                  [Select]
                                  1.  Automatic redial
                                  2.  Speed dialling
                                  3.  Call waiting options
                                  4.  Own number sending
                                  5.  Phone line in use
                                  6.  Automatic answer
                                  0.  Back
                                  99. Home
================================================================================

"""

                while True:
                    print(call_settings)
                    call = input("Input Number Choice: ")

                    match call:
                        case "99":
                            return
                        case "0":
                            break

                        case "1":   print("Automatic redial")
                        case "2":   print("Speed dialling")
                        case "3":   print("Call waiting options")
                        case "4":   print("Own number sending")
                        case "5":   print("Phone line in use")
                        case "6":   print("Automatic answer")
                        case _:     print("Invalid")

            case "2":
                print("Phone settings")

                phone_settings = """
================================== PHONES SETTINGS ===============================
                                  [Select]
                                  1.  Language
                                  2.  Cell info display
                                  3.  Welcome note
                                  4.  Network selection
                                  5.  Confirm SIM service actions
                                  0.  Back
                                  99. Home
===================================================================================
"""

                while True:
                    print(phone_settings)
                    phone = input("Input Number Choice: ")

                    match phone:
                        case "99":
                            return
                        case "0":
                            break

                        case "1":   print("Language")
                        case "2":   print("Cell info display")
                        case "3":   print("Welcome note")
                        case "4":   print("Network selection")
                        case "5":   print("Confirm SIM service actions")
                        case _:     print("Invalid")

            case "3":
                print("Security settings")

                security_settings = """
================================== SECURITY SETTINGS ===============================
                                  [Select]
                                  1.  PIN code request
                                  2.  Call barring service
                                  3.  Fixed dialling
                                  4.  Closed user group
                                  5.  Security level
                                  6.  Change access codes
                                  0.  Back
                                  99. Home
====================================================================================
"""

                while True:
                    print(security_settings)
                    security = input("Input Number Choice: ")

                    match security:
                        case "99":
                            return
                        case "0":
                            break

                        case "1":   print("PIN code request")
                        case "2":   print("Call barring service")
                        case "3":   print("Fixed dialling")
                        case "4":   print("Closed user group")
                        case "5":   print("Security level")
                        case "6":   print("Change access codes")
                        case _:     print("Invalid")

            case "4":
                print("Restore factory setting")
            case _:
                print("Invalid")

def music_menu():
    music = """
============================== MUSIC ================================
                           Press[Menu] and then [select]
                           1. Music player
                           2. Radio
                           3. Recorder
                           4. Track list
                           0. Back
                           99. Home
======================================================================
"""

    while True:
        print(music)
        music_menu_choice = input("Input Number Choice: ")

        match music_menu_choice:
            case "99":
                return
            case "0":
                break

            case "1":   print("Music player")
            case "2":   print("Radio")
            case "3":   print("Recorder")
            case "4":   print("Track list")
            case _:     print("Invalid")

def clock_menu():
    clock = """
============================== CLOCK ================================
                           Press[Menu] and then [select]
                           1. Alarm clock
                           2. Clock settings
                           3. Date setting
                           4. Stopwatch
                           5. Countdown timer
                           6. Auto update of date and time
                           0. Back
                           99. Home
======================================================================
"""

    while True:
        print(clock)
        clock_menu_choice = input("Input Number Choice: ")

        match clock_menu_choice:
            case "99":
                return
            case "0":
                break

            case "1":   print("Alarm clock")
            case "2":   print("Clock settings")
            case "3":   print("Date setting")
            case "4":   print("Stopwatch")
            case "5":   print("Countdown timer")
            case "6":   print("Auto update of date and time")
            case _:     print("Invalid")

main_menu()
