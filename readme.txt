# The mongodb server is being run locally on port 27017

###################################################### Task 1  ######################################################################

## For task 1, the script that parses and ingests the db_works_test.csv file in MongoDB is the python script: main.py

## The requirements for the scripts are the pymongo and csv libraries,
To install the requirement using the pip package manager:
run the command
# pip install pymongo

## To run the script:

#1: Start the MongoDB server
#2: Run the main.py script after installing the pymongo package. The script ingests the data in the database.



###################################################### Task 2  ######################################################################
## For task 2, a Restful API has been designed with Python and the Flask framework. The api returns a JSON object of the
## right owners metadata corresponding to the ISWC parameter.
## If the api is queried for an ISWC code that does not exist in the database, it returns a {'error': 'Not found'} JSON
## object


## The requirements for the scripts are flask and flask_pymongo.

To install the requirement using the pip package manager:

# pip install flask
# pip install flask_pymongo

#1 Start the MongoDB server
#2 Run the app.py script. This fires up a development server running on: http://127.0.0.1:5000/
#2 The api endpoint can be accessed at ->  http://127.0.0.1:5000/api/<iswc_code> where <iswc_code> is the ISWC code
## whose right_owners is to be returned

## The api that queries the Mongo collection is exposed at the endpoint Endpoint ->/api/<iswc_code>
## To test the API, open your command line and  run: curl http://127.0.0.1:5000/api/T-042088917-3.


