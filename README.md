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

### Django uses MVT (Model View Template) Pattern

- Model: Handles data

- View: Processes requests and contains business logic

- Template: Defines how data is presented

-----
#### Relationship Among Models: