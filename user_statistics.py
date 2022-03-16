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
    return f'User with id {user_id} has a maximum transaction amount of {max(list_holder)} and a minimum trasaction amount of {min(list_holder)}'


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
        x_coordinates.append(index[4])
        y_coordinates.append(index[5])
    summed_coordinates.append(x_coordinates, y_coordinates)
    centroid = (sum(summed_coordinates[0])/len(summed_coordinates[0]),sum(summed_coordinates[1])/len(summed_coordinates[1]))
    return centroid

def distance_from_centroid(user_id, transaction_id):
    '''
    Parameters: None
    Purpose: Reads the data and get the location centroid for a provided user
    Return: location centroid of the user
    '''
    data = load_data()
    centroid = location_centroid(user_id)
    transaction_location = []
    for i in data.values():
        for j in i:
            if j[0] == str(transaction_id):
                transaction_x_coord = j[3]
                transaction_y_coord = j[4]
                transaction_location.append(transaction_x_coord)
                transaction_location.append(transaction_x_coord)
    distance_from_centroid = ( (transaction_location[0] - centroid[0])**2 + (transaction_location[1] - centroid[1])**2 ) ** 0.5
    
    return distance_from_centroid

def var_transaction_user(user_id):
    data = load_data()
    list_amount = []
    for index in data[user_id]:
        list_amount.append(index[2])
    n = len(list_amount)
    mean = sum(list_amount) / n
    deviations = [(x - mean) ** 2 for x in data]
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
                    'description of transaction':j[1]
                }

def distance_between_transaction_user(user_id):
    '''
    Parameters: transaction id1 and transaction id2
    Purpose: takes the id of two different transactions and find the distance between them
    Return: the distance between the two different transactions
    '''
    data = load_data()
    for index in data[user_id]:
        print('Choose the two respective transactions id from the list below')
        print(index[0], end=',')
    id_1 = input('enter the first transaction id from the list above')
    id_2 = input('enter the second transaction id from the list above')
    ids_coordinates = []
    for ids in [id_1, id_2]:
        for i in data.values():
            for j in i:
                if j[0] == str(ids):
                    id_coordinates = [j[3], j[4]]
                    ids_coordinates.append(id_coordinates)
    distance = ((ids_coordinates[0][0] - ids_coordinates[1][0])**2 + (ids_coordinates[0][1] - ids_coordinates[1][1])**2)**0.5
    return distance

