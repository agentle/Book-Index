def for_grandpa():
    
    """
    Future Additions:
    1. Mulitple page #s per entry ---------------- DONE -----
    2. Last name then first name ----------------- DONE -----
    3. Corrections to the index (remove data) ---- DONE -----
    4. Saving an index as a file (.txt?) --------- DONE -----
    5. Naming each index ------------------------- DONE -----
    6. Correcting naming scheme ------------------ DONE -----
    """
    
    import re
    dict1 = {}
    print()
    
    index_name = input("What is the name of the index you want to create or \
open? ")
    print()
    
    if not index_name.endswith(".txt"):
        index_name += ".txt"
    
    try:
        file = open(index_name)
        lines = file.readlines()
        print("Continuing the text file " + index_name)
        for line in lines[5:]:
            match = re.match("(.+)\s\.{4,55}\s([\d\s,]+)", line)
                
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
        answer1 = input('Do you want to input, edit, or save? (Type \
either "input", "edit", or "save") ')
        print()
        
        if answer1.startswith("S") or answer1.startswith("s") or \
        answer1.startswith('"S') or answer1.startswith('"s'):
            flag = False
        
        elif answer1.startswith("E") or answer1.startswith("e") or \
        answer1.startswith('"E') or answer1.startswith('"e'):
            
            to_be_edited = input("Do you want to edit a name, \
date, or phrase? ")
            print()
            
            if to_be_edited.startswith("N") or to_be_edited.startswith("n"):
                name = input("What is their name? ")
                if "," in name:
                    key = name
                else:
                    individual_names = name.split()
                    if len(individual_names) <= 1:
                        key = name
                    else:
                        key = individual_names[-1] + ","
                        individual_names = individual_names[:-1]
                        for i in individual_names:
                            key += " " + i
                            
            elif to_be_edited.startswith("D") or to_be_edited.startswith("d"):
                key = input("What date do you want to edit? ")
                print()
                
            elif to_be_edited.startswith("P") or to_be_edited.startswith("p"):
                key = input("What phrase do you want to edit? (Must be exact) ")
                print()
                
            if key in dict1.keys():
                pages = ""
                for i in sorted(dict1[key]):
                    pages += str(i) + ", "
                pages = pages[:-2]
                
                print("The page numbers associated with that entry are: " + 
                      pages)
                remove = input("Please type here all the page numbers you'd \
like to remove (Ex: 28, 57, 90): ")
                print()
                
                remove += ","
                to_remove = []
                
                for item in remove.split():
                    to_remove.append(int(item[:-1]))
                    
                difference = set(dict1[key]) - set(to_remove)
                del dict1[key]
                dict1[key] = list(difference)
            
            elif key not in dict1.keys():
                print("It looks like the term you entered isn't stored in the \
file. Perhaps you mistyped it?")
                print()                
            
        else:
            answer2 = input("Do you want to input a name, date, or phrase? ")
            print()
            
            if answer2.startswith("N") or answer2.startswith("n"):
                
                initial_name = input("What is their name? ")
                if "," in initial_name:
                    name = initial_name
                    
                else:
                    individual_names = initial_name.split()
                    
                    if len(individual_names) <= 1:
                        name = initial_name
                    else:
                        name = individual_names[-1] + ","
                        individual_names = individual_names[:-1]
                        for i in individual_names:
                            name += " " + i
                            
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
    file.write("Name/Date/Phrase " + 39 * "." + " Page Numbers")
    file.write("\n\n")
    
    for key, values in sorted(dict1.items()):
        string1 = ""
            
        for value in sorted(values):
            string1 += str(value) + ", "
            
        file.write(key + " " + ((55 - int(len(key))) * ".") + " " 
                   + string1[:-2])
        file.write("\n\n")

    print("\n" * 5)
    print(index_name)
    print()
    print()
    print("Name/Date/Phrase " + 39 * "." + " Page Numbers")
    print()
    
    for key, values in sorted(dict1.items()):
        string1 = ""
        
        for value in sorted(values):
            string1 += str(value) + ", "

        print(key + " " + ((55 - int(len(key))) * ".") + " " + string1[:-2])
        print()
        
for_grandpa()
