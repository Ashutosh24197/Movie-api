# Movie-api
An api which return the max profit and a list of selected movies of given data of movies on which an actor can work in a year.

# Description

A movie actor wants to make the max. money by picking the right movies in a given year.



# Rules:

Consider that the actor gets a fixed amount of 1 Crore for each movie that he does, irrespective of the duration of the money. 

Movies have a contract where the actor is not allowed to work on other movies whose date conflicts with the selected movies date. For example if the actor have selected a movie from 10th Jan to 20th Jan (both dates inclusive) then actor can’t select any movies which has a start or end date between 10th to 20th Jan.

Actor is not worried about optimization of less work and more money. His aim is to get the max. money even if he has to work for all the days of the year.



A REST API where actor can submit the data containing the list of movies with movie name, start date and end date and the API should return the total amount that he can make along with the final list of movies to select.

# Sample Input

{
    "Movie data":[
        {
        "movie":"Bala" ,
        "Start":"8 Jan",
        "End":"28 jan"
        },
        {
        "movie":"Rock" ,
        "Start":"20 Jan",
        "End":"30 jan"
        },
        {
        "movie":"PolicyMaker" ,
        "Start":"29 Jan",
        "End":"16 Feb"
        },
        {
        "movie":"Brave" ,
        "Start":"02 Feb",
        "End":"14 feb"
        },
        {
        "movie":"Drive" ,
        "Start":"10 Feb",
        "End":"18 Feb"
        },
        {
        "movie":"Race",
        "Start":"15 Feb",
        "End":"28 Feb"
        }]
}

# Sample Outhput

{
  "Max Profit": 3,
  "Movies list": [
    {
      "End": "28 jan",
      "Start": "8 jan",
      "movie": "Bala"
    },
    {
      "End": "14 fab",
      "Start": "2 fab",
      "movie": "Brave"
    },
    {
      "End": "28 fab",
      "Start": "15 fab",
      "movie": "Race"
    }
  ]
}

