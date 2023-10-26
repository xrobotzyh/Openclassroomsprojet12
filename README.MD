# OpenClassrooms Projet P12

## Objectif
Epic Events is a company specializing in event management, ranging from parties and professional gatherings to off-site activities for our clients. We are currently in the process of developing a Customer Relationship Management (CRM) software to enhance our operations.

Our CRM software is designed to efficiently collect and manage client data, as well as event-related information. Moreover, it streamlines communication among various departments within our organization. This initiative is aimed at optimizing our workflow, providing superior services to our clients, and ensuring the success of their events.

## Local Configuration
## Installation
### Getting the project on your local machine.
1. Clone the repository to your local machine.
```bash
git clone https://github.com/xrobotzyh/OpenClassRoomsProjet12.git
```
2.Navigate to the cloned directory.
```bash
cd OpenClassRoomsProjet12
```

### Create a virtual environment
1.Create a virtual environment named "env".
```bash
python3 -m venv env
```

### Activate and install your virtual environment
Activate the newly created virtual environment "env".
```bash
source env/bin/activate
```
Install the packages listed in requirements.txt.
```bash
pip install -r requirements.txt
```

### Project Database Restoration

To restore the database from the backup file:

1.Ensure you have MySQL installed and a database with the same name as your original database.
2.Run the following command to restore the database:
```bash
mysql -u your_username -p your_database_name < EpicEvent_backup.sql
```
Replace your_username with your MySQL username and your_database_name with your database name. 
```bash
python manage.py migrate
```

## Usage
### Start the serveur
```bash
python manage.py runserver
```
### Navigation
Access the site on your browser using the URL http://127.0.0.1:8000/

## Test
Use the following information to test
```bash
| User name             | password      |
|-----------------------|---------------|
| management01          | 123456789    | 

```

## Thanks!