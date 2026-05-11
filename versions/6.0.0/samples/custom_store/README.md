Custom Store Token Store Persistence
------------------------------------
Our Python SDK comes with built-in support for File Persistence, which stores your tokens in a file at a location of your choosing, and DB Persistence, which stores your tokens in a MySQL database. However, if these options don't align with your specific requirements, or if you want to use a database other than MySQL or any other storage method, you can leverage Custom Persistence, where you can define your own storage logic through the TokenStore class. To do this, you need to implement the TokenStore interface and override its methods accordingly.

We have added examples for three different types using custom persistence:

### 1. [SQLite3 DB](custom_store_sqlite.py): 

In this case, the tokens are persisted in a file on disk. The data in this database persists even after the program exits, as long as the file is not deleted.

The sqlite3.connect('zohooauth.db') command in Python is used to create a connection to an SQLite database stored in a file called zohooauth.db. 

Persistent Database:
 - The database is stored on disk in the file zohooauth.db.
 - The data in this database persists even after the program exits, as long as the file is not deleted.
 - If the zohooauth.db file does not exist, it will be created.
 - If the zohooauth.db file already exists, the command will open a connection to this existing database.

Initialization Sample Code:
```python
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", refresh_token="refresh_token")
            store = CustomStoreSQLite()
            Initializer.initialize(environment=environment, token=token, store=store)
        except Exception as ex:
            print(ex)
```
Please check out the complete sample code [here](custom_store_sqlite.py).

### 2. [In-Memory SQLite3 DB](custom_store_in_memory.py)

In this case, the tokens are persisted in the RAM, and not on disk. Once the connection to the DB is closed, the DB and all its data will be deleted.

The sqlite3.connect(':memory:') command in Python is used to create an in-memory SQLite database. This type of database resides entirely in RAM and does not persist to disk. Here are the key points about using an in-memory SQLite database:

Temporary Database:
 - The database exists only while the connection is open.
 - Once the connection is closed, the database and all its data are lost.

Initialization Sample Code:
```python
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", refresh_token="refresh_token")
            store = CustomStore()
            Initializer.initialize(environment=environment, token=token, store=store)
        except Exception as ex:
            print(ex)
```
Please check out the complete sample code [here](custom_store_in_memory.py).

### 3. [Custom Store List](custom_store_list.py)

In this case, the token details are stored in a list object. The data exists only while the app is running.

The token details stored in list.

Temporary Storage:
 - The data exists only while the app is running.

Initialization Sample Code:
```python
        try:
            environment = USDataCenter.PRODUCTION()
            token = OAuthToken(client_id="client_id", client_secret="client_secret", refresh_token="refresh_token")
            store = CustomStoreList()
            Initializer.initialize(environment=environment, token=token, store=store)
        except Exception as ex:
            print(ex)
```
Please check out the complete sample code [here](custom_store_list.py).