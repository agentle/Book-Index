def for_grandpa():
    
    """
    Future Additions:
    1. Mulitple page #s per entry ---------------- DONE -----
    2. Last name then first name ----------------- DONE -----
    3. Corrections to the index (remove data)
    4. Saving an index as a file (.txt?) --------- DONE -----
    5. Naming each index ------------------------- DONE -----
    """
    
    import re
    dict1 = {}
    print()
    
    index_name = input("What is the name of the index you want to create or \
open? (Capitalization is important) ")
    print()
    if not index_name.endswith(".txt"):
        index_name += ".txt"
    
    try:
        file = open(index_name)
        lines = file.readlines()
        print("Continuing the text file " + index_name)
        for line in lines[5:]:
            match = re.match("(\S+)\s---\s([\d\s,]+)", line)
            if not match:
                match = re.match("(\S+,\s\S+)\s---\s([\d\s,]+)", line)
            if match:
                name = match.group(1)
                pages = match.group(2)
                pages = pages[:-1]
                pages += ","
                                
                for page in pages.split():
                    if name in dict1:
                        dict1[name].append(int(page[:-1]))
                        
                    else:
                        list1 = []
                        list1.append(int(page[:-1]))
                        dict1[name] = list1
                        

    
    except FileNotFoundError:
        file = open(index_name, "a+")
        print("Creating a new text file called " + index_name)
    
    
    file.close()
    print()

    
    flag = True
    
    while flag:
        answer1 = input("Do you want to input something? ")
        print()
        
        if answer1.startswith("N") or answer1.startswith("n"):
            flag = False
            
        else:
            answer2 = input("Do you want to input a name, date, or phrase? ")
            print()
            
            if answer2.startswith("N") or answer2.startswith("n"):
                first_name = input("What's their first name? ")
                print()
                last_name = input("What's their last name? ")
                print()
                name = last_name + ", " + first_name
                pages = input(
                    "What pages was the name on? (Ex: 34, 32, 56, 338) ")
                print()
                pages = pages + ","
                
                for page in pages.split():
                    if name in dict1:
                        dict1[name].append(int(page[:-1]))
                        
                    else:
                        list1 = []
                        list1.append(int(page[:-1]))
                        dict1[name] = list1
                    
            elif answer2.startswith("D") or answer2.startswith("d"):
                date = input("What date do you want to input? ")
                print()
                pages = input(
                    "What pages was the date on? (Ex: 34, 32, 56, 338) ")
                print()
                pages += ","
                
                for page in pages.split():
                    if date in dict1:
                        dict1[date].append(int(page[:-1]))
                        
                    else:
                        list1 = []
                        list1.append(int(page[:-1]))
                        dict1[date] = list1
                    
            elif answer2.startswith("P") or answer2.startswith("p"):
                phrase = input("What phrase do you want to input? ")
                print()
                pages = input(
                    "What pages was the phrase on? (Ex: 34, 32, 56, 338) ")
                print()
                pages += ","
                
                for page in pages.split():
                    if phrase in dict1:
                        dict1[phrase].append(int(page[:-1]))
                        
                    else:
                        list1 = []
                        list1.append(int(page[:-1]))
                        dict1[phrase] = list1
            
    file = open(index_name, "w")  # NOTICE: deletes the file and then rewrites
    file.write(index_name)
    file.write("\n\n\n")
    file.write("Name/Date/Phrase --- Page Numbers")
    file.write("\n\n")
    for key, values in sorted(dict1.items()):
        string1 = ""
            
        for value in sorted(values):
            string1 += str(value) + ", "
            
        file.write(key + " --- " + string1[:-2])
        file.write("\n\n")

    print("\n" * 5)
    print(index_name)
    print()
    print()
    print("Name/Date/Phrase --- Page Numbers")
    print()
    for key, values in sorted(dict1.items()):
        string1 = ""
        
        for value in sorted(values):
            string1 += str(value) + ", "
        
        print(key + " --- " + string1[:-2])
        print()
        
for_grandpa()
