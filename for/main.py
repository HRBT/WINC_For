from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

#print('Exercise 1')

def shortest_names(countries):

    short_names_list = []

    for x in countries:
        if len(x) < 5:
            #print(x,'=', len(x))
            short_names_list.append(x)
    return short_names_list


#print('Exercise 2')

def most_vowels(countries):
    vowels = "aeiouAEIOU"
    vowel_counts = []
    
    for x in countries:
        count = 0
        for z in x:
            if z in vowels:
                count += 1
        vowel_counts.append((x, count))
    #print(vowel_counts)
    sorted_list = sorted(vowel_counts, key=lambda x: x[1], reverse=True)
    sorted_strings = [x for x, count in sorted_list][:3]
    #print(sorted_list)
    return sorted_strings


#print('Exercise 3')

def alphabet_set(countries):   
    alphabetical_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    def most_vowels(countries):
        vowels = "aeiouAEIOU"
        vowel_counts = []
    
        for x in countries:
            count = 0
            for z in x:
                if z in vowels:
                    count += 1
            vowel_counts.append((x, count))
    #print(vowel_counts)
        sorted_list = sorted(vowel_counts, key=lambda x: x[1], reverse=True)
        sorted_strings = [x for x, count in sorted_list][:14]
        return sorted_strings
    
    sorted_list = most_vowels(countries)

    for country in sorted_list:
        for i in country:
            if i.lower() in alphabet and country not in alphabetical_list:
                alphabet = alphabet.replace(i.lower(),'')
                alphabetical_list.append(country)
            if alphabet == '':
                break    
    return alphabetical_list


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

#print(get_countries())
#print(countries)

print('Excercise 1')
shortest_names(countries)

print('Excercise 2')
most_vowels(countries)

print('Excercise 3')
#alphabet_set(countries)
alphabet_set(countries)
 
