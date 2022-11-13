import re


def distinguish_house_from_add(string1:str,string2:str)->dict:
    # assuming street name has more than letters than house name
    # returning true if string1 has more alphabetic characters False if not
    counter_string1 = 0
    counter_string2 = 0
    # Using regular expressions to find out which string containts more alphabetic characters
    for c in string1:
        if re.search('[A-Za-z]',c):
            counter_string1+=1
    for c in string2:
        if re.search('[A-Za-z]',c):
            counter_string2+=1
    if counter_string1>counter_string2:
        return True
    else:
        return False


def removing_non_alphabetic_char(addr:str)->str:
    unwanted_char = ["?","!","_","#","_","|","(",")","[","]"]
    for item in unwanted_char:
        addr = addr.replace(item,'')
    # checking for multiple successive commas and removing them
    tmp = re.findall(',{2,}| {2,}',addr)
    for t in tmp:
        addr = addr.replace(t,' ')
    return addr



def string_to_json(addr:str)->dict:
    # removing cleaning the string from unwanted characters
    addr = removing_non_alphabetic_char(addr)
    # removing No,N°,no, number,num,Number,nummer,Nummer
    list_of_unwanted_words = [" No "," N° "," no "," number "," nummer "," Nummer ",' num '," Num " ]
    for item in list_of_unwanted_words:
        addr = addr.replace(item,'')

    #checking simple scenario
    if len(addr.split())==2:
        results = distinguish_house_from_add(addr.split()[0],addr.split()[1])
        if results:
            print({"street":addr.split()[0],"housenumber":addr.split()[1]})
            return
        else:
            print({"street":addr.split()[1],"housenumber":addr.split()[0]})
        return
    # splitting using comma then
    if len(addr.split(','))==2 :
        results = distinguish_house_from_add(addr.split(',')[0],addr.split(',')[1])
        if results:
            print({"street":addr.split(',')[0],"housenumber":addr.split(',')[1]})
            return
        else:
            print({"street":addr.split(',')[1],"housenumber":addr.split(',')[0]})
        return
    # more complex cases where we have a longer add
    tmp_list = addr.split()
    for i in range(0,len(tmp_list)):
        # search for number
        if re.match(pattern='^[0-9]',string=tmp_list[i]):
            number_index = i
    tmp_dict = {}
    #split string into two the street name should be taller in number of characters
    string_left = ' '.join(tmp_list[:number_index])
    string_right = ' '.join(tmp_list[number_index:])
    if distinguish_house_from_add(string_left,string_right):
        tmp_dict["street"] = string_left
        tmp_dict["housenumber"] = string_right
        print(tmp_dict)
        return
    else:

        tmp_dict["street"] =' '.join(tmp_list[number_index+1:])
        tmp_dict["housenumber"] = ''.join(tmp_list[0:number_index+1])
        print(tmp_dict)
        return

