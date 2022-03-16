#making use of user defined/created module 
from load_dataset import load_data


def user_min_max(user_id):
    '''
    Parameters: None
    Purpose: Reads the data and get the min and max transaction amount for a provided user
    Return: maximum and minimum transaction amount of the user
    '''
    data = load_data()
    list_amount = []
    for index in data[user_id]:
        list_amount.append(index[2])
    return f'User with id {user_id} has a maximum transaction amount of {max(list_amount)} and a minimum trasaction amount of {min(list_amount)}'


def location_centroid(user_id):
    '''
    Parameters: None
    Purpose: Reads the data and get the location centroid for a provided user
    Return: location centroid of the user
    '''

    data = load_data()
    x_coordinates = []
    y_coordinates = []
    summed_coordinates = []
    for index in data[user_id]:
        x_coordinates.append(float(index[3]))
        y_coordinates.append(float(index[4]))
    summed_coordinates.append(x_coordinates)
    summed_coordinates.append(y_coordinates)
    centroid = [sum(summed_coordinates[0])/len(summed_coordinates[0]),sum(summed_coordinates[1])/len(summed_coordinates[1])]
    return centroid

def distance_from_centroid(user_id, transaction_id):
    '''
    Parameters: None
    Purpose: Reads the data and get the location centroid for a provided user
    Return: location centroid of the user
    '''
    data = load_data()
    x_coordinates = []
    y_coordinates = []
    summed_coordinates = []
    for index in data[user_id]:
        x_coordinates.append(float(index[3]))
        y_coordinates.append(float(index[4]))
    summed_coordinates.append(x_coordinates)
    summed_coordinates.append(y_coordinates)
    centroid = [sum(summed_coordinates[0])/len(summed_coordinates[0]),sum(summed_coordinates[1])/len(summed_coordinates[1])]
    
    transaction_location = []
    for i in data.values():
        for j in i:
            if j[0] == str(transaction_id):
                transaction_x_coord = float(j[3])
                transaction_y_coord = float(j[4])
                transaction_location.append(transaction_x_coord)
                transaction_location.append(transaction_x_coord)
    distance_from_centroid = ( (transaction_location[0] - centroid[0])**2 + (transaction_location[1] - centroid[1])**2 ) ** 0.5
    
    return distance_from_centroid

def var_transaction_user(user_id):
    data = load_data()
    list_amount = []
    for index in data[user_id]:
        list_amount.append(float(index[2]))
    n = len(list_amount)
    mean = sum(list_amount) / n
    deviations = [(x - mean) ** 2 for x in list_amount]
    variance = sum(deviations) / n
    return variance

def std_transaction_user(user_id):
    '''
    Parameters: None
    Purpose: calculates the standard deviatioin of transaction for a provided user
    Return: standard deviation of transaction amount
    '''
    var = var_transaction_user(user_id)
    std_dev = var ** (1/2)
    return std_dev

def transaction_status(transaction_id):
    '''
    Parameters: transaction identity
    Purpose: determines whether a transaction is fraudulent or not and 
    Return: the transaction status and the transaction identities
    '''
    data = load_data()
    for i in data.values():
        for j in i:
            if j[0] == str(transaction_id):
                return {
                    'status of the transaction':j[-1],
                    'description of transaction':j[1],
                }

def distance_between_transaction_user(user_id):
    '''
    Parameters: user id
    Purpose: takes the id of two different transactions and find the distance between them
    Return: the distance between the two different transactions
    '''
    data = load_data()
    print('Choose the two respective transactions id from the list below')
    for index in data[user_id]:
        print(index[0], end=',')
    id_1 = input('\n enter the first transaction id from the list above ')
    id_2 = input('enter the second transaction id from the list above ')
    ids_coordinates = []
    for ids in [id_1, id_2]:
        for i in data.values():
            for j in i:
                if j[0] == str(ids):
                    id_coordinates = [float(j[3]), float(j[4])]
                    ids_coordinates.append(id_coordinates)
    distance = ((ids_coordinates[0][0] - ids_coordinates[1][0])**2 + (ids_coordinates[0][1] - ids_coordinates[1][1])**2)**0.5
    return distance


def distance_between_transaction_any_user(user_id1, user_id2):
    '''
    Parameters: user id
    Purpose: takes the id of two different transactions and find the distance between them
    Return: the distance between the two different transactions
    '''
    data = load_data()
    transaction_ids = []
    ids_coordinates = []
    for user_id in [user_id1, user_id2]:
        print(f'Choose one of the transactions id from the user {user_id} below')
        for index in data[user_id]:
            print(index[0], end=',')
        tran_id = input('\n enter one transaction id from the list above ')
        transaction_ids.append(tran_id)
    for ids in transaction_ids:
        for i in data.values():
            for j in i:
                if j[0] == str(ids):
                    id_coordinates = [float(j[3]), float(j[4])]
                    ids_coordinates.append(id_coordinates)
    distance = ((ids_coordinates[0][0] - ids_coordinates[1][0])**2 + (ids_coordinates[0][1] - ids_coordinates[1][1])**2)**0.5
    return distance

min_max = user_min_max('21')
location_centroid = location_centroid('21')
distance_from_centroid1 = distance_from_centroid('21', '500004')
var_amount = var_transaction_user('21')
std_amount = std_transaction_user('21')
status = transaction_status('500002')
distance1 = distance_between_transaction_user('21')
distance2 = distance_between_transaction_any_user('21','22')

print(min_max)
print(location_centroid)
print(distance_from_centroid1)
print(var_amount)
print(std_amount)
print(status)
print(distance1)
print(distance2)
