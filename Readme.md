# Task Api

### Requirements

- Version - `Python 3.10.5`

### Running the Api Manually

- Install the dependencies from the requirements.txt
    
    ```powershell
    pip install -r requirements.txt
    ```
    
- Create a .env file. The file must contain these configurations
    
    ```
    SQLALCHEMY_DATABASE_URI="DB_URI"
    DEBUG = "DEBUG_CONDITION"
    ```
    
- Create the database instance
    
    ```powershell
    python
    from api import db , app
    with app.app_context():
    	db.create_all()
    ```
    
- Run the api
    
    ```powershell
    python app.py
    ```
    

### Running the api using provided docker image

```powershell
docker run -p 5000:5000 todo-api
```

### Routes

The postman workspace link given below

[Postman](https://elements.getpostman.com/redirect?entityId=22889337-1f01b83f-60ff-4fc0-8b7f-3e934460073b&entityType=collection)