# _**Sharebite Backend Assessment**_

## How to run this application:

1. Run the start.sh script which will start mysql container  on your local machine
   ```bash
    bash start.sh
    ```
   
2. Create a virtual environment using the command: 
    ```
    virtualenv venv
   ```
   
3. Activate the virtual environment using the command: 
    ```
    source venv/bin/activate
   ```

4. Install all the requirements: 
    ```
    pip3 install -r requirements.txt
   ```
   
5. Make  migrations: 
    ```
    python3 manage.py makemigrations
   ```
   
6. Migrate Changes: 
    ```
    python3 manage.py migrate
   ```
   
7. Run the application:
    ```
    python3 manage.py runserver
   ```


## API Endpoint:

URL:
    ```
    http://127.0.0.1:8000/api/
    ```

METHOD:
    ```
    GET
    ```