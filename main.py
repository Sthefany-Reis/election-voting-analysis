#This import csv function creates table-like objects from the items in the Excel csv file
import csv

#Class for all Constituency elements
class Constituency:
    def __init__(self, name, region, country, ctype):
        self.cName = name
        self.cRegion = region
        self.cCountry = country
        self.cType = ctype
        self.description = {
            'Constituency name': self.cName,
            'Region name': self.cRegion,
            'Country name': self.cCountry,
            'Constituency type': self.cType
        }

    def __str__(self):
        return f'{self.cName}, {self.cRegion}, {self.cCountry}, {self.cType}'

    def get_description(self):
        return self.description

#Reading CSV file and creating Constituency objects
def Read_Constituency():
    with open("FullDataFor20241.csv", newline="") as csvfile:
        reading = csv.DictReader(csvfile)

        #Loop through each row in the CSV
        for row in reading:
        #Ensure you access the correct column names from the CSV file
            constituency = Constituency(
                 name=row['Constituency name'],  #Match the exact column name
                 region=row['Region name'],
                 country=row['Country name'],
                 ctype=row['Constituency type']
            )
            #Print the description dictionary of each constituency
            print(constituency.get_description())

#Class for all MP elements
class MP:
    def __init__(self, firstparty, secondparty, firstname, surname, votes, gender):
        self.mFirstParty = firstparty
        self.mSecondParty = secondparty
        self.mFirstName = firstname
        self.mSurname = surname
        self.mVotes = votes
        self.mGender = gender
        self.description = {
            'First party': self.mFirstParty,
            'Second party': self.mSecondParty,
            'Member first name': self.mFirstName,
            'Member surname': self.mSurname,
            'Valid votes': self.mVotes,
            'Member gender': self.mGender
        }

    def __str__(self):
        return f'{self.mFirstParty}, {self.mSecondParty}, {self.mFirstName}, {self.mSurname}, {self.mVotes}, {self.mGender}'

    def get_description(self):
        return self.description

#Reading CSV file and creating MP objects
def Read_MP():
    with open("FullDataFor20241.csv", newline="") as csvfile:
        reading = csv.DictReader(csvfile)
        for row in reading:
            mp = MP(
                firstparty=row['First party'],
                secondparty=row['Second party'],
                firstname=row['Member first name'],  #Match the exact column name
                surname=row['Member surname'],
                votes=row['Valid votes'],
                gender=row['Member gender']
            )
            print(mp.get_description())
    
#Class for all Party elements
class Party:
    def __init__(self, firstname, surname, name, Con, Lab, LD, RUK, Green, SNP, PC):
        self.pFirstName = firstname
        self.pSurname = surname
        self.pName = name
        self.CON = Con
        self.LAB = Lab
        self.LD = LD
        self.RUK = RUK
        self.GREEN = Green
        self.SNP = SNP
        self.PC = PC
        self.description = {
            'Member first name': self.pFirstName,
            'Member surname': self.pSurname,
            'Constituency name': self.pName,
            'Con': self.CON,
            'Lab': self.LAB,
            'LD': self.LD,
            'RUK': self.RUK,
            'Green': self.GREEN,
            'SNP': self.SNP,
            'PC': self.PC
        }

    def __str__(self):
        return f'{self.pFirstName}, {self.pSurname}, {self.pName}, {self.CON}, {self.LAB}, {self.LD}, {self.RUK}, {self.GREEN}, {self.SNP}, {self.PC}'

    def get_description(self):
        return self.description
    
def Read_Party():
    with open("FullDataFor20241.csv", newline="") as csvfile:
        reading = csv.DictReader(csvfile)
        for row in reading:
            party = Party(
                firstname=row['Member first name'],
                surname=row['Member surname'],
                name=row['Constituency name'],
                Con=row['Con'],
                Lab=row['Lab'],
                LD=row['LD'],      #Match the exact column name
                RUK=row['RUK'],
                Green=row['Green'],
                SNP=row['SNP'],
                PC=row['PC']
            )
            print(party.get_description())
    
def option_4():
    print("\nWould you like to:")
    print("1 - Type in MP's full name to locate constituency")
    print("2 - Type in constituency to find out who is the MP")
    print("3 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-3): "))
            
            if option == 1:
                while True:
                    #Option to find constituency by MP's full name
                    first_name = input("\nEnter MP's first name: ").strip()
                    surname = input("Enter MP's surname: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Member first name'].strip().lower() == first_name.lower() and \
                               row['Member surname'].strip().lower() == surname.lower():
                                result = f"\nMP {first_name} {surname} represents the constituency: {row['Constituency name']}"
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo MP found with the given full name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another MP? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return

            elif option == 2:
                while True:
                    #Option to find MP by constituency
                    constituency_name = input("\nEnter the constituency name: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Constituency name'].strip().lower() == constituency_name.lower():
                                result = f"\nThe MP for {constituency_name} is {row['Member first name']} {row['Member surname']}"
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo constituency found with the given name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another constituency? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return

            elif option == 3:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def option_5():
    print("\nWould you like to:")
    print("1 - Type in MP's full name to locate the region")
    print("2 - Type in the region to find out who is the MP")
    print("3 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-3): "))
            
            if option == 1:
                while True:
                    #Option to find Region by MP's full name
                    first_name = input("\nEnter MP's first name: ").strip()
                    surname = input("Enter MP's surname: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Member first name'].strip().lower() == first_name.lower() and \
                               row['Member surname'].strip().lower() == surname.lower():
                                result = f"\nMP {first_name} {surname} represents the region: {row['Region name']}"
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo MP found with the given full name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another MP? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return
            
            elif option == 2:
                while True:
                    #Option to find MP by Region name
                    region_name = input("\nEnter the region name: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Region name'].strip().lower() == region_name.lower():
                                result = f"\nThe MP for {region_name} is {row['Member first name']} {row['Member surname']}"
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo region found with the given name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another region? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return
            
            elif option == 3:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return
            
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
def option_6():
    print("\nWould you like to:")
    print("1 - Type in MP's full name to find out how many Valid votes they received")
    print("2 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-2): "))
            
            if option == 1:
                while True:
                    first_name = input("\nEnter MP's first name: ").strip()
                    surname = input("Enter MP's surname: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Member first name'].strip().lower() == first_name.lower() and \
                               row['Member surname'].strip().lower() == surname.lower():
                                result = f"\nMP {first_name} {surname} has {row['Valid votes']} Valid votes."
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo MP found with the given full name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another MP? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return

            elif option == 2:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
def option_7():
    print("\nWould you like to see the Total Votes for:")
    print("1 - Conservatives Party")
    print("2 - Labour Party")
    print("3 - Liberal Democrats Party")
    print("4 - Reform UK Party")
    print("5 - Green Party")
    print("6 - Scottish National Party")
    print("7 - Plaid Cymru Party")
    print("8 - Return to the main menu")

    party_columns = {
        1: ("Conservatives", "Con"),
        2: ("Labour", "Lab"),
        3: ("Liberal Democrats", "LD"),
        4: ("Reform UK", "RUK"),
        5: ("Green Party", "Green"),
        6: ("Scottish National Party", "SNP"),
        7: ("Plaid Cymru", "PC")
    }

    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-8): "))
            
            if option in party_columns:
                party_name, column_name = party_columns[option]
                total_votes = 0
                
                with open("FullDataFor20241.csv", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        try:
                            total_votes += int(row[column_name])
                        except ValueError:
                            print(f"Invalid vote data found for {party_name}. Skipping row.")
                
                result = f"\nThe total votes for the {party_name} are: {total_votes}"
                print(result)
                
                #Append result to the file
                with open("Results.txt", "a") as results_file:
                    results_file.write(str(result) + "\n")

                #Ask if the user wants to view another party's votes
                repeat = input("\nWould you like to see votes for another party? (yes/no): ").strip().lower()
                if repeat == 'no':
                    print("\nReturning to the main menu...")
                    
                    #Log returning to the main menu
                    with open("Results.txt", "a") as results_file:
                        results_file.write("Returned to the main menu...\n")
                    return

            elif option == 8:
                #Return to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please select a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            
            #Log the error to the file
            with open("Results.txt", "a") as results_file:
                results_file.write(error_message + "\n")

def option_8():
    print("\nIn the UK, to be elected as a Member of Parliament (MP) in a general election,",
          "a candidate must win the most votes in their constituency (a simple majority, not an absolute one)")

    #Log the information to the Results.txt file
    result = "\nIn the UK, to be elected as a Member of Parliament (MP) in a general election, a candidate must win the most votes in their constituency (a simple majority, not an absolute one)"
    
    with open("Results.txt", "a") as results_file:
        results_file.write(result + "\n")
    
    return

def option_9():
    print("\nWould you like to see the Gender Comparison (Male/Female) for:")
    print("1 - Conservatives Party")
    print("2 - Labour Party")
    print("3 - Liberal Democrats Party")
    print("4 - Reform UK Party")
    print("5 - Green Party")
    print("6 - Scottish National Party")
    print("7 - Plaid Cymru Party")
    print("8 - Return to the main menu")

    party_columns = {
        1: ("Conservatives", "Con"),
        2: ("Labour", "Lab"),
        3: ("Liberal Democrats", "LD"),
        4: ("Reform UK", "RUK"),
        5: ("Green Party", "Green"),
        6: ("Scottish National Party", "SNP"),
        7: ("Plaid Cymru", "PC")
    }

    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-8): "))
            
            if option in party_columns:
                party_name, column_name = party_columns[option]
                male_count = 0
                female_count = 0

                with open("FullDataFor20241.csv", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        try:
                            if int(row[column_name]) > 0:  #Check if the party received votes in this constituency
                                gender = row['Member gender'].strip().lower()
                                if gender == 'male':
                                    male_count += 1
                                elif gender == 'female':
                                    female_count += 1
                        except ValueError:
                            print(f"Invalid data found for {party_name}. Skipping row.")

                total = male_count + female_count
                result = f"\nFor the {party_name}:"
                if total > 0:
                    male_percentage = (male_count / total) * 100
                    female_percentage = (female_count / total) * 100
                    result += f"\nMale MPs: {male_percentage:.2f}%"
                    result += f"\nFemale MPs: {female_percentage:.2f}%"
                else:
                    result += f"\nNo data available for the {party_name} MPs."
                
                print(result)

                #Append result to the file
                with open("Results.txt", "a") as results_file:
                    results_file.write(result + "\n")

                #Ask if the user wants to view another party's gender comparison
                repeat = input("\nWould you like to see gender comparison for another party? (yes/no): ").strip().lower()
                if repeat == 'no':
                    print("\nReturning to the main menu...")
                    
                    #Log returning to the main menu
                    with open("Results.txt", "a") as results_file:
                        results_file.write("Returned to the main menu...\n")
                    return

            elif option == 8:
                #Return to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please select a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            
            #Log the error to the file
            with open("Results.txt", "a") as results_file:
                results_file.write(error_message + "\n")
    
def option_10():
    print("\nWould you like to:")
    print("1 - Type in MP's full name to locate Party")
    print("2 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-2): "))
            
            if option == 1:
                while True:
                    #Option to find Party by MP's full name
                    first_name = input("\nEnter MP's first name: ").strip()
                    surname = input("Enter MP's surname: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Member first name'].strip().lower() == first_name.lower() and \
                               row['Member surname'].strip().lower() == surname.lower():
                                result = f"\nMP {first_name} {surname} represents the Party: {row['First party']}"
                                print(result)
                                found = True
                                break
                        if not found:
                            result = "\nNo MP found with the given full name. Please try again."
                            print(result)

                    #Append result to the file
                    with open("Results.txt", "a") as results_file:
                        results_file.write(result + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another MP? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("Returned to the main menu...\n")
                        return

            elif option == 2:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            
            #Log the error to the file
            with open("Results.txt", "a") as results_file:
                results_file.write(error_message + "\n")

def option_11():
    print("\nWould you like to:")
    print("1 - Find out what Region your Constituency is in")
    print("2 - Find out what Constituencies are in your Region")
    print("3 - Go back to the main menu")

    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-3): "))

            if option == 1:
                while True:
                    #Option to find Region by Constituency
                    constituency_name = input("\nEnter the constituency name: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Constituency name'].strip().lower() == constituency_name.lower():
                                result = f"\nThe Constituency for {constituency_name} is {row['Region name']}"
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as csvfile:
                                    csvfile.write(str(result) + "\n")
                                    
                                found = True
                                break
                        if not found:
                            result = "\nNo constituency found with the given name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as csvfile:
                                csvfile.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another Constituency? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as csvfile:
                            csvfile.write("\nReturned to the main menu...")
                        return

            elif option == 2:
                while True:
                    #Option to find Constituencies by Region name
                    region_name = input("\nEnter Region name: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        constituencies = []   #List to store constituency names
                        for row in reader:
                            if row['Region name'].strip().lower() == region_name.lower():
                                constituencies.append(row['Constituency name'])
                        
                        if constituencies:
                            result = f"The Region {region_name} represents these Constituencies:"
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as csvfile:
                                csvfile.write(str(result) + "\n")
                                
                            for constituency in constituencies:
                                result = f"- {constituency}"
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as csvfile:
                                    csvfile.write(str(result) + "\n")
                        else:
                            result = "No Region found with the given name or no constituencies in this Region. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as csvfile:
                                csvfile.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("Would you like to search for another Region? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as csvfile:
                            csvfile.write("Returned to the main menu...\n")
                        return

            elif option == 3:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as csvfile:
                    csvfile.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def option_12():
    print("\nWould you like to:")
    print("1 - Find out the most voted party in a constituency")
    print("2 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-2): "))
            
            if option == 1:
                while True:
                    #Option to find the most voted party by constituency
                    constituency_name = input("\nEnter the name of the constituency: ").strip()

                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        party_votes = {}
                        found = False
                        
                        for row in reader:
                            #Check if the row contains the constituency we're interested in
                            if row['Constituency name'].strip().lower() == constituency_name.lower():
                                found = True
                                party_name = row['First party'].strip()
                                try:
                                    # Add the votes to the dictionary
                                    votes = int(row['Valid votes'])
                                    if party_name in party_votes:
                                        party_votes[party_name] += votes
                                    else:
                                        party_votes[party_name] = votes
                                except ValueError:
                                    print(f"Invalid vote data for {party_name} in {constituency_name}. Skipping row.")
                        
                        if found:
                            #Find the party with the most votes
                            most_voted_party = max(party_votes, key=party_votes.get)
                            result = f"\nThe most voted party in {constituency_name} is: {most_voted_party} with {party_votes[most_voted_party]} votes."
                            print(result)
                            
                            #Log the result to Results.txt
                            with open("Results.txt", "a") as results_file:
                                results_file.write(result + "\n")
                        else:
                            result = f"\nNo data found for the constituency {constituency_name}. Please try again."
                            print(result)
                            
                            #Log the result to Results.txt
                            with open("Results.txt", "a") as results_file:
                                results_file.write(result + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another constituency? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("Returned to the main menu...\n")
                        return

            elif option == 2:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            
            #Log the error to the file
            with open("Results.txt", "a") as results_file:
                results_file.write(error_message + "\n")

def option_13():
    print("\nWould you like to:")
    print("1 - Find out the least voted party in a constituency")
    print("2 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-2): "))
            
            if option == 1:
                while True:
                    #Option to find the least voted party by constituency
                    constituency_name = input("\nEnter the name of the constituency: ").strip()

                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        party_votes = {}
                        found = False
                        
                        for row in reader:
                            #Check if the row contains the constituency we're interested in
                            if row['Constituency name'].strip().lower() == constituency_name.lower():
                                found = True
                                party_name = row['First party'].strip()
                                try:
                                    #Add the votes to the dictionary
                                    votes = int(row['Valid votes'])
                                    if party_name in party_votes:
                                        party_votes[party_name] += votes
                                    else:
                                        party_votes[party_name] = votes
                                except ValueError:
                                    print(f"Invalid vote data for {party_name} in {constituency_name}. Skipping row.")
                        
                        if found:
                            #Find the party with the least votes
                            least_voted_party = min(party_votes, key=party_votes.get)
                            result = f"\nThe least voted party in {constituency_name} is: {least_voted_party} with {party_votes[least_voted_party]} votes."
                            print(result)
                            
                            #Log the result to Results.txt
                            with open("Results.txt", "a") as results_file:
                                results_file.write(result + "\n")
                        else:
                            result = f"\nNo data found for the constituency {constituency_name}. Please try again."
                            print(result)
                            
                            #Log the result to Results.txt
                            with open("Results.txt", "a") as results_file:
                                results_file.write(result + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another constituency? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("Returned to the main menu...\n")
                        return

            elif option == 2:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            
            #Log the error to the file
            with open("Results.txt", "a") as results_file:
                results_file.write(error_message + "\n")
                
def option_14():
    print("\nWould you like to:")
    print("1 - Type in MP's full name to find out their gender")
    print("2 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-2): "))
            
            if option == 1:
                while True:
                    first_name = input("\nEnter MP's first name: ").strip()
                    surname = input("Enter MP's surname: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Member first name'].strip().lower() == first_name.lower() and \
                               row['Member surname'].strip().lower() == surname.lower():
                                result = f"\nMP {first_name} {surname} is {row['Member gender']}."
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo MP found with the given full name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another MP? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return

            elif option == 2:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def option_15():
    print("\nWould you like to:")
    print("1 - Type in Constituency name to find out how many Valid votes it received")
    print("2 - Go back to the main menu")
    
    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-2): "))
            
            if option == 1:
                while True:
                    constituency_name = input("\nEnter Constituency name: ").strip()
                    
                    with open("FullDataFor20241.csv", newline="") as csvfile:
                        reader = csv.DictReader(csvfile)
                        found = False
                        for row in reader:
                            if row['Constituency name'].strip().lower() == constituency_name.lower():
                                result = f"\nThe constituency {constituency_name} has {row['Valid votes']} Valid votes."
                                print(result)
                                
                                #Append result to the file
                                with open("Results.txt", "a") as results_file:
                                    results_file.write(str(result) + "\n")
                                
                                found = True
                                break
                        if not found:
                            result = "\nNo constituency found with the given name. Please try again."
                            print(result)
                            
                            #Append result to the file
                            with open("Results.txt", "a") as results_file:
                                results_file.write(str(result) + "\n")
                    
                    #Ask if the user wants to search again or go back to the menu
                    repeat = input("\nWould you like to search for another Constituency? (yes/no): ").strip().lower()
                    if repeat == 'no':
                        print("\nReturning to the main menu...")
                        
                        #Log returning to the main menu
                        with open("Results.txt", "a") as results_file:
                            results_file.write("\nReturned to the main menu...\n")
                        return

            elif option == 2:
                #Go back to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please enter 1 or 2.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

def option_16():
    print("\nWould you like to see the Votes as a Percentage of Total Votes for:")
    print("1 - Conservatives Party")
    print("2 - Labour Party")
    print("3 - Liberal Democrats Party")
    print("4 - Reform UK Party")
    print("5 - Green Party")
    print("6 - Scottish National Party")
    print("7 - Plaid Cymru Party")
    print("8 - Return to the main menu")

    party_columns = {
        1: ("Conservatives", "Con"),
        2: ("Labour", "Lab"),
        3: ("Liberal Democrats", "LD"),
        4: ("Reform UK", "RUK"),
        5: ("Green Party", "Green"),
        6: ("Scottish National Party", "SNP"),
        7: ("Plaid Cymru", "PC")
    }

    while True:
        try:
            option = int(input("\nEnter the appropriate option (1-8): "))
            
            if option in party_columns:
                party_name, column_name = party_columns[option]
                party_votes = 0
                total_votes = 0
                
                with open("FullDataFor20241.csv", newline="") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        try:
                            party_votes += int(row[column_name])
                            total_votes += int(row['Valid votes'])
                        except ValueError:
                            print(f"Invalid vote data found. Skipping row.")
                
                if total_votes > 0:
                    percentage = (party_votes / total_votes) * 100
                    result = f"\nThe votes for the {party_name} are {party_votes}, which is {percentage:.2f}% of the total votes ({total_votes})."
                else:
                    result = "\nNo valid votes data found to calculate percentages."
                
                print(result)
                
                #Append result to the file
                with open("Results.txt", "a") as results_file:
                    results_file.write(result + "\n")

                #Ask if the user wants to view another party's votes
                repeat = input("\nWould you like to see votes for another party? (yes/no): ").strip().lower()
                if repeat == 'no':
                    print("\nReturning to the main menu...")
                    
                    #Log returning to the main menu
                    with open("Results.txt", "a") as results_file:
                        results_file.write("Returned to the main menu...\n")
                    return

            elif option == 8:
                #Return to the main menu
                print("\nReturning to the main menu...")
                
                #Log returning to the main menu
                with open("Results.txt", "a") as results_file:
                    results_file.write("Returned to the main menu...\n")
                return

            else:
                print("Invalid option. Please select a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            error_message = f"An error occurred: {e}"
            print(error_message)
            
            #Log the error to the file
            with open("Results.txt", "a") as results_file:
                results_file.write(error_message + "\n")

#Welcome message
def welcome_message():
    print("Welcome to the Election Analysis Program!")
    print("\nThis program allows you to view data from the 2024 Voting Analysis Spreadsheet.")
welcome_message()

#Function that shows the user what the shortened down parties stand for
def abbreviation_party():
    part = ["\nHere are what the abbreviated parties stand for and where they are in effect:",
            "Con = Conservatives Party - in effect in the whole UK",
            "Lab = Labour Party - in effect in the whole UK",
            "LD = Liberal Democrats - in effect in the whole UK",
            "RUK = Reform UK Party - in effect in the whole UK",
            "Green = Green Party - in effect in the whole UK",
            "SNP = Scottish National Party - This party is only in effect in Scotland, not the entire UK",
            "PC = Plaid Cymru Party - This party is only in effect in Wales, not the entire UK"]
    print(part[0])
    print(part[1])
    print(part[2])
    print(part[3])
    print(part[4])
    print(part[5])
    print(part[6])
    print(part[7])
  
abbreviation_party()
            
#Displaying the options to choose from
def display_menu():
    print("\nHere are the options of the Election Analysis Program:")
display_menu()

#Menu being shown with options of data to view
def menu():
    options = [
        "\nProgram Menu:",
        "1 - Lists all of the Constituency elements: Constituency name and type, Region name, Country name",
        "2 - Lists all of the MP elements: First and second party of the MP, as well as the MP's full name and gender, Valid votes also mentioned",
        "3 - Lists all of the Party elements: MP's full name and their Constituency name, as well as all the votes received from all the parties in the UK",
        "4 - Find an MP's full name and Constituency",
        "5 - Find an MP's full name and Region",
        "6 - Find an MP's full name and Valid votes they have received",
        "7 - Find out the Total votes for a specific party",
        "8 - Votes needed to be elected as a candidate",  #Creating the menu using lists in Arrays
        "9 - Find out the Percentage of male and female MPs by party",
        "10 - Find an MP's full name and Party",
        "11 - Lists Constituencies by region",
        "12 - Find the Most voted party in a constituency",
        "13 - Find the Least voted party in a constituency",
        "14 - Find an MP's Gender",
        "15 - Find a Constituency's Valid votes",
        "16 - Find out the Total votes for a specific party as a percentage",
        "17 - Exit the program"
    ]

    for option in options:
        print(option)

    while True:
        try:
            choice = int(input("\nEnter your choice (1-17): "))  #Asking the user to input an option number

            if choice == 1:
                print("\nListing all Constituency data:")
                Read_Constituency()
            elif choice == 2:
                print("\nListing all MP data:")
                Read_MP()
            elif choice == 3:
                print("\nListing all Party data:")
                Read_Party()
            elif choice == 4:
                print("\nFinding an MP's full name and Constituency:")
                option_4()
            elif choice == 5:
                print("\nFinding an MP's full name and Region:")
                option_5()
            elif choice == 6:
                print("\nFinding an MP's full name and Valid votes:")
                option_6()
            elif choice == 7:
                print("\nCalculating total votes for a specific party:")
                option_7()
            elif choice == 8:
                print("\nCalculating votes needed for election:")
                option_8()
            elif choice == 9:
                print("\nCalculating percentage of male and female MPs by party:")
                option_9()
            elif choice == 10:
                print("\nFinding an MP's full name and Party:")
                option_10()
            elif choice == 11:
                print("\nListing constituencies by region:")
                option_11()
            elif choice == 12:
                print("\nFinding the most voted party in a constituency:")
                option_12()
            elif choice == 13:
                print("\nFinding the least voted party in a constituency:")
                option_13()
            elif choice == 14:
                print("\nListing MPs by gender:")
                option_14()
            elif choice == 15:
                print("\nFinding a Constituency's Valid votes:")
                option_15()
            elif choice == 16:
                print("\nCalculating total votes for a specific party as a percentage:")
                option_16()
            elif choice == 17:
                print("\nExiting the program ------------------------------------------")
                print("\nGoodbye and thank you for using the Election Analysis Program!")
                break  #Ends the program
            else:
                print("\nInvalid option. Please choose between 1 and 17.")

        except ValueError:
            print("\nInvalid input. Please enter a number.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")

menu()
