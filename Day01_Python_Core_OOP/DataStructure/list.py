
#create List
languages = ["java","python","html","react"];
#Accessing List
print("First Language:",languages[0]);
print("Last Language:",languages[-1]);
#add List elements
languages.append(".net");
#inserting at a specific position
languages.insert(0,"angular");
#update elements
languages[2]="Python 3";
#removing elements
languages.remove("java");

#iterating through list
for language in languages:
    print(language);

#list length
print("Total Languages:",len(languages));

print(languages);