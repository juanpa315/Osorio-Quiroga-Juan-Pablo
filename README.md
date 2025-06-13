## Project description 
- Website for managing employees of a software consulting company.

## HTML Templates

**Base Templates:**
- `baseform.html` - Base form template inherited by all other forms
- `index.html` - Main dashboard with navigation to all modules

**Authentication:**
- `registration/login.html` - System login form

**CRUD Forms:**
- `employee.html` - Employee registration/update form and listing table
- `customer.html` - Customer registration/update form and listing table  
- `coe.html` - Center of Excellence registration/update form and listing table
- `job_positions.html` - Job position registration/update form with salary ranges and listing table

**Features:**
- All forms inherit from `baseform.html` for consistent styling
- Dual-mode forms support both create and update operations using `{% if update %}` conditionals
- Integrated tables display all records with Update action button
- Navigation bar with Home and Logout buttons in top-right corner
- Form validation and postgress database integration for all CRUD operations

**Tests:**
- https://docs.google.com/spreadsheets/d/e/2PACX-1vS5YDwr9_Q9ximQqpVxAQJ9O7MUrKRHWeoYoRTzDOycrlL3r0gZyKsQSy-RUnuB1IrdDrWA8542LyFS/pubhtml

Over python 3.13 execute:
```
poetry install
```
Over the root folder execute:
```
python manage.py runserver
```
Open the local link: http://127.0.0.1:8000/login
user: admin
pass: 1234
