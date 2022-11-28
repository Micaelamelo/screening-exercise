BlueNode cleanses the data that represents containers and commodities that travel through the network of global ports. 

There are a few standards for how this data should be represented and these standards are widely adopted. However, the data going into these standardized data formats is not consistent, that is, many of the fields are free text where vastly different data can be input. The lack of standardized data is the reason that cleansing is needed. 

This exercise provides you with a dataset of raw container and commodity records that need cleansing. 

 

*Step 1:* Review the current Pull Request providing feedback to the developer 

*Step 2:* Check out the branch that the PR belongs to and implement your suggestions 

*Step 2.1:* 

Fix port cleansing (if you did not already!) 

The current code attempts to cleanse the two port fields:  

*port_of_loading 
*port_of_discharge 

However, the results are not great. Sometimes the cleanser reports that a Port does not exist when it is easy to find in the lookup data. Find a way to make it better. 

A properly cleansed port should be formatted:  

“PORT_NAME, PORT_COUNTRY”  _or_  “HALIFAX, CANADA”   

You have been provided with a table of all global ports.  Use this table to cleanse the port name. Additionally, the lookup table does not provide the full country name, only the country code. Use the pycountry library to get the full country name. 

https://pypi.org/project/pycountry/ 

 

*Documentation* 
Document your code in a way that you think makes it easy for us to understand. 

*Unit Tests* 
Add unit tests to test your final code.  Use any testing framework that you prefer. We want to see that you can know how to use a test framework and can write quality tests. 

*Using Git* 
We are interested to see how you use git to organize your commits.   

*Step 3:* 
*Update the README to let us know how to run your code and test. 
*Create a new PR for your final submission. 

Estimated time to complete ~3 hours
 

*Bonus* 

We will use bonus work to evaluate deeper technical abilities. Choose any that you feel demonstrate your abilities.  

An hs code is the unique identifier for a commodity. These codes are one of the most important pieces of data that BlueNode cleanses. The raw data provided could have better hs codes. 

*Add a linter like flake8 to the project and use it to make your code clean (~1 hour)

*Hs codes are always formatted with 4 digits to the left of the decimal point and from 2 to 8 digits to the right.  There are always an even number of places filled in the hs code so the valid options are XXXX.XX, XXXX.XXXX, XXXX.XXXXXX, and XXXX.XXXXXXXX.  Create a formatter for hs codes.  Example: 710.2 would become 0710.2 and 0710 would become 0710.00.  Additionally, spreadsheet applications strip leading zeros, find a way to force the hs code to be interpreted as a string. (~1 hour)

*Train a classifier to use the commodity description keywords in the hs codes file to identify the correct hs code. (~2 hours)

*Demonstrate the use of a design pattern.  Singleton, Command, Delegate, and Observer are some possibilities. (~1-2 hours)
