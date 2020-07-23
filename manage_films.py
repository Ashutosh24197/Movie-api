from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def home():

    req = request.get_json()
    movie_data=req["Movie data"]

    result = manage_movie(movie_data)
    

    return jsonify(result), 200


# Function which find the maxprofit and the selcted movies list

def manage_movie(movies_data ):
    
    month = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    
    # Converting string date to list of int for better comparison
            # date[0] : day
            # date[1] : month
    for movie in movies_data:
        start = movie['Start']
        start = start.split()
        movie['Start'] = [int(start[0]), month[start[1].lower()]]

        end = movie['End']
        end = end.split()
        movie['End'] = [int(end[0]), month[end[1].lower()]]

    
    movies_list = [0 for i in movies_data]
    i = 0
    end = [0, 0]

    movies_list = manage(movies_data, movies_list, i, end) # call recursive function

    result_list = []
    for i in range(len(movies_list)):
        if movies_list[i]==1:
            result_list.append(movies_data[i])

    month = {1:'jan', 2:'fab', 3:'mar', 4:'apr', 5:'may', 6:'jun', 7:'jul', 8:'aug', 9:'sep', 10:'oct', 11:'nov', 12:'dec'}

    #Converting back date to string data
    for movie in result_list:
        start = movie['Start']
        start[0] = str(start[0])
        start[1] = month[start[1]]
        movie['Start'] = " ".join(start)
        
        end = movie['End']
        end[0]=str(end[0])
        end[1] = month[end[1]]
        movie['End'] = " ".join(end)

    return {'Max Profit':sum(movies_list), 'Movies list':result_list}

# Recursive function which return a list of 0/1
#    0: i'th movie is selcted
#    1: i'th movie is not selected
# Parameters:
# movies_data : list of dictonary of all movies
# movies_list : a list containing record up to i-1'th index that which movie is selected
# i : currect index
# end : end date when upto actor is busy


def manage(movies_data, movies_list, i, end):
    movies_list = movies_list.copy()
    if i+1<len(movies_list):
        #Finding profit without incuding current movie
        l1 = manage(movies_data, movies_list, i+1, end)
        
        # Finding profit if corrent movie can be selected 
        l2 = []
        if movies_data[i]['Start'][0]>end[0] or movies_data[i]['Start'][1]>end[1]:
            movies_list[i] = 1
            end = movies_data[i]['End']
            l2 = manage(movies_data, movies_list, i+1, end)

        if sum(l1)>sum(l2):
            return l1
        else:
            return l2

    else: # at the last index
        if movies_data[i]['Start'][0]>end[0] or movies_data[i]['Start'][1]>end[1]:
            movies_list[i] = 1

        return movies_list


if __name__ == "__main__":
    app.run()