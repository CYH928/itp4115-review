## This question concerns how to define an ORM in Flask 

### Firstly, we need to install Flask migrate module 
```shell
pip install flask-migrate
```
### Secondly, we need to create a migration repository (initialize a database file and migration folder)
```shell
flask db init
```

### Thirdly, we need to create a migration file with comment “Admin Table”
```shell
flask db migrate -m "Admin Table"
```

<!-- Write down 3 commands of the above steps. -->