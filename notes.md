# Additional Notes

## Django uses MVT (Model View Template) Design Pattern: 
To Structure a Web App into Layers.

- Model: Handles data

- View: Processes requests and contains business logic

- Template: Defines how data is presented


## Relationship Among Models:

- Many-to-one: (ForeignKey) Defines a many-to-one relationship between two models.

- One-to-one: Similar to a ForeignKey, but it ensures only one related object can exist.

- Many-to-many: Defines a many-to-many relationship between two models.


----
### The VIEW:

The view processes the web request from the user and returns a web response.
Typically, the view accesses the model and decides what data to send back to the user.
It contains the application's business logic, which determines how to access the model. 
The view also typically uses a template to build the response containing the data that is sent back to the user.

### How a view works:

- The view is the server-side component that receives an HTTP request and returns and HTTP response.
- When the browser sends an HTTP request to the application, a view defined in the application receives the 
request, runs the business logic to process the request, and returns an HTTP response.

### Types of views

- Views can be implemented in Django using a function or a class.

#### _Function-based view_:

is a simple Python function that takes an object of type HttpRequest as its first parameter.  
The object contains the data from the incoming HTTP request. The function defines all the code that
implements the business logic from the view. When the function finishes running, the function returns
an object of type HttpResponse.

#### _Class-based view_:

This class defines properties and methods that give you the ability to respond to different HTTP request methods.