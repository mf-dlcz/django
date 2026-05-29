# django

## Setup

1. Create and activate virtual environment:
    ```bash
    python3 -m venv .venv
    source venv/bin/activate
    ```
2. Install Django package:
    ```bash
    pip install django
    ```
3. Run migrations:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
4. Start the server:
    ```bash
    python3 manage.py runserver
    ```

## Apps

### pets_app

Models:
- `Breed` - stores breed name, weight, and height
- `VaccinationCard` - tracks rabies, hepatitis, borrelia, and distemper vaccination dates
- `Pet` - stores pet info (name, gender, birth, owner, weight, height) linked to a `Breed` and `VaccinationCard`
- `VetVisit` - records vet visits with date and notes, linked to a `Pet`

## Notes

- `venv/` is excluded from version control via `.gitignore`

## Additional Notes

### Django uses MVT (Model View Template) Design Pattern: 
To Structure a Web App into Layers.

- Model: Handles data

- View: Processes requests and contains business logic

- Template: Defines how data is presented


#### Relationship Among Models:

- Many-to-one: (ForeignKey) Defines a many-to-one relationship between two models.

- One-to-one: Similar to a ForeignKey, but it ensures only one related object can exist.

- Many-to-many: Defines a many-to-many relationship between two models.


----
#### The VIEW:
The view processes the web request from the user and returns a web response.
Typically, the view accesses the model and decides what data to send back to the user.
It contains the application's business logic, which determines how to access the model. 
The view also typically uses a template to build the response containing the data that is sent back to the user.

#### How a view works:
- The view is the server-side component that receives an HTTP request and returns and HTTP response.