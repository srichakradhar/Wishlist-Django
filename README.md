Welcome to your first exercise with Django REST Framework. While working through the different exercises, you would create API's for posting birthday wishes and retrieving them.

 

In this exercise, you will create a serializer and use it to build your API. You are provided with

a model `Wish`
data added to the model for testing your API
Appropriate URL conf
 

As part of this exercise, you should do the following

1. In serializers.py

create a serializer `WishSerializer` using the model `Wish`.
Declare all the fields from the model
 

2. In views.py

define a method wish_list which lists all wishes using 'GET' or creates a new wish using 'POST'
For GET method, create an object instance, use WishSerializer and serialize it and then send the response as a `JSONResponse`.
For POST method, use the JSONParser to parse the request data, serialize it, check for valid serializer instance.  If valid instance, return the JSONResponse of the serialized data, else return the JSONResponse of the serialization errors.
define a method wish_detail which retrieves a wish using 'GET' , updates a wish using 'PUT' or deletes a wish using 'DELETE'
For GET method, serialize the object `wish` and return the serialized data as JSONResponse.
For PUT method, use the JSONParser to parse the request data, serialize it, check for valid serializer instance.  If valid instance, return the JSONResponse of the serialized data, else return the JSONResponse of the serialization errors.
For DELETE method, delete the object and return a HTTPResponse with status 204.
 

To test your code, use the URL

/wishes/ to retrieve all the wishes
/wishes/{id}/ to retrieve a specific wish detail.