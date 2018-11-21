[![Build Status](https://travis-ci.org/matthenge/senditAPI.svg?branch=develop)](https://travis-ci.org/matthenge/senditAPI)
[![Coverage Status](https://coveralls.io/repos/github/matthenge/senditAPI/badge.svg?branch=ch-update-readme-161892938)](https://coveralls.io/github/matthenge/senditAPI?branch=ch-update-readme-161892938)
[![Maintainability](https://api.codeclimate.com/v1/badges/ce3cc4349922e5a7c860/maintainability)](https://codeclimate.com/github/matthenge/senditAPI/maintainability)

# sendIT

SendIT is a courier services application that allows users to register and place an order to have a parcel delivered. Users can also update the destination of an undelivered parcel or cancel the delivery order all together. 


## Getting started
These instructions will get you a copy of the project running on your local machine for development and testing puposes.


## Prerequisites

	.Python 3.6

	.Postman

	.Git


## Installing

.Clone this repository from [here](https://github.com/matthenge/senditAPI) 
	
.To test the API locally, set up a virtual environment in the root folder 
    - virtualenv venv
	
.Activate the virtual environment through; source venv/bin/activate via the terminal
	
.Run the export FLASK_APP=run.py command via the terminal
	
.Install dependencies through pip install -r requirements.txt
	
.Run tests through pytest
	
.Test the endpoints though Postman 
	
    -To create a new order, use http://127.0.0.1:5000/api/v1/parcel
		
      Hearder: Content-Type: application/json
			
      example request: 
			
      {"pickup_location" : "kenol", "destination" : "kajiado", "price" : "1000", "user_id" : "50"}
			
    -To register a new user, use http://127.0.0.1:5000/api/v1/user
		
        Hearder: Content-Type: application/json
			
        example request:
			
        {"firstname" : "red", "lastname" : "jon", "username" : "tigertiger", "email":"redjon@ymail.com", "password": "serial"}
    -To fetch all parcels, http://127.0.0.1:5000/api/v1/parcels
    
        Hearder: Content-Type: application/json
	
    -To fetch specific parcel order use http://127.0.0.1:5000/api/v1/parce/100
    
        Hearder: Content-Type: application/json
	
    -To fetch all parcel orders by one user, use http://127.0.0.1:5000/api/v1/parc/2
    
        Hearder: Content-Type: application/json
	
    -To cancel a parcel order use http://127.0.0.1:5000/api/v1/parce/100
    
        Hearder: Content-Type: application/json
	
   -The endpoints are;
   
        POST /api/v1/parcel
	
        GET /api/v1/parcels
	
        GET /api/v1/parce/<order_id>
	
        GET /api/v1/parc/<user_id>
	
        PUT /api/v1/parce/<order_id>
	
        POST /api/v1/user
	
        GET /api/v1/users/<user_id>
	
        
## Built with

    .Python 3
    
    .Flask-Restful
    
    .Flask
    
    
## Author

James Maruhi
