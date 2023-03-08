# this project is for e-commerce and i have known hw to make a urls and templates 
# routing .
# now i have created the first model to be the category model and this model takes care 
# of all the product categories ; it has a name , slug for urls, describtion, image, 
# go there to get more information about this model 
# 
# secondly, The user login model which in follow come with django, comes with login as username
# instead of email and password, therfore i have to customize my own user model , to use email
# as login form. to do this , i have to create a new app for my custom user model. check for 
# the app to see the details. 

# NOTe: after creating the custom user model, i need to go back to the settings.py to tell django 
# i am using a custon user model. 
#FORMAT: in settings.py , right under the WSGI, write this code below
# AUTH_USER_MODEL = 'account.account' 
# that is the model app.model name 

# and before we migrate this new user model to the database, we need to delete the old database,
# so that there will be no mixed up, also remember to register your models any time we create a
#  new 
# model


# after in have created my custom user model , i discoverd my password is chnagable from 
# the database but i want it to me read only and also populate some of my account details
# on the display page of the account for clearer reading.
# 
# to do this follow the procedure below.  
# on the admin.py for account , import useradmin from django.contib.auth.admin,
# then create a class  , this class will contain some details and later you pass the class 
# name and argument into the registered model youb want to edit,. go to the admin.py to 
# see the details
# further changes were made also to test the database changes, these chnges were still
# on the admin.py and self explanatory.
# 
# for the categories app again .. when in create a new category, i want the slug to be auto
# populated as i type the category name.
# to do this, we go to the category app, on the category admin.py , create a class
# categoryAdmin, under the class ...... go to the admin.py to see the details. 

