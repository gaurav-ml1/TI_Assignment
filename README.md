# TI_Assignment

Problem:-
1) Create a simple Category model using DRF with following fields : Id,name,parent,is_featured,image,is_active,description
2) Create CRUD APIs for the same.
3) Validate input at every event/API.
4) Implement ordering and filtering.
5) GET API should take params to return :
Ex. /abc.com?params=id|name|is_featured : this should return Array of JSON object with specified keys, along with an <b>authenticated key mentioning user authentication status</b>.
6) Send emails to ​naveen.kumar1@timesinternet.in​ after 15 minutes of each post request. This should not be a part of the request / response cycle.

Solution:-

Task #1, #2, #3, #4 will cover through bellow api.

API:- http://35.227.56.33/api/v1/category/

Method:- GET, POST, DELETE, UPDATE

Content-Type:- Application/Json

Task #5 and #6 will be cover through this api-

API:- http://35.227.56.33/api/v1/category/?params=id|name|description

Method:- GET

Content-type:- Application/json


Note:- authenticated key mentioning user authentication status"- I could not understand it.