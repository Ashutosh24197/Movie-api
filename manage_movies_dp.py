from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def home():

    req = request.get_json()
    movie_data=req["Movie data"]

    result = manage_movies(movie_data)
    

    return jsonify(result), 200


# Function which find the maxprofit and the selcted movies list

def manage_movies(movies_data):
    
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

    movies_data = sort_movie(movies_data)

    movies_lists = [[movie['movie']] for movie in movies_data]
    profit_list = [1 for movie in movies_data]
    
    # Dp for finding max profit
    for i in range(1,len(movies_data)):
        for j in range(i):
            if ( movies_data[j]['End'][1]<movies_data[i]['Start'][1] or  # If end month is before start month
            
                ( movies_data[j]['End'][1]==movies_data[i]['Start'][1] and  # or end month is same to start month and day is before
                movies_data[j]['End'][0]<movies_data[i]['Start'][0] )
                
                ) and ((profit_list[j] + 1) > profit_list[i]):
                    
                    profit_list[i] = profit_list[j] + 1
                    
                    movies_lists[i] = [movies_lists[i][0]] + movies_lists[j]
                    
                    
    max_profit = max(profit_list)
    index = profit_list.index(max_profit)
    
    selected_movies = movies_lists[index]
    
    result_list = []
    
    for movie in movies_data:
        if movie['movie'] in selected_movies:
            result_list.append(movie)
                
    month = {1:'jan', 2:'fab', 3:'mar', 4:'apr', 5:'may', 6:'jun', 7:'jul', 8:'aug', 9:'sep', 10:'oct', 11:'nov', 12:'dec'}

    #Converting back, date to string data
    for movie in result_list:

        start = movie['Start']
        start[0] = str(start[0])
        start[1] = month[start[1]]
        movie['Start'] = " ".join(start)
        
        end = movie['End']
        end[0]=str(end[0])
        end[1] = month[end[1]]
        movie['End'] = " ".join(end)

    return {'Max Profit':max_profit, 'Movies list':result_list}
    

# A function which sort the movies in acsending order of there end date
def sort_movie(movies_data):
    for i in range(len(movies_data)-1):
        for j in range(i+1,len(movies_data)):
            if movies_data[j]['End'][0]<movies_data[i]['End'][0] and movies_data[j]['End'][1]<=movies_data[i]['End'][1]:
                    temp = movies_data[i]
                    movies_data[i] = movies_data[j]
                    movies_data[j] = temp
                    
    return movies_data

if __name__ == "__main__":
    app.run()