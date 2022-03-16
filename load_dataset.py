def load_data():
    '''
    Parameters: None
    Purpose: Opens the file name safely and creates the dictionary.
    Return: dictionary containing user id as key and a list of lists containing the neighbourhood, gender, and neuter/spay status. 
    '''
    #try-except clause to catch errors for wrong file name
    try:
        with open('datasets/test.txt', 'r') as file:
            lines = [line.rstrip() for line in file] #read from csv line by line, rstrip helps to remove '\n' at the end of line
            results = {}
            for line in lines:
                words = line.split(':')
                if words[0] in results:
                    list_list = [words[1], words[2], words[3], words[4],words[5], words[6]]
                    results[words[0]].append(list_list)
                else:
                    list_list = []
                    list_list.append([words[1], words[2], words[3], words[4],words[5], words[6]])
                    results[words[0]] = list_list
            return results
    except:
        print(f'The file does not exist or is corrupt')


