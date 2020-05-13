# Consistent Hashing and RHW Hashing

The distributed cache you implemented in the midterm is based on naive modula hashing to shard the data.

# References
http://mlwiki.org/index.php/Consistent_Hashing#Virtual_Nodes

https://docs.openstack.org/swift/latest/ring_background.html

https://medium.com/i0exception/rendezvous-hashing-8c00e2fb58b0

## Part I.

Implement Rendezvous hashing to shard the data.

Output:
```
(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_client_rhw.py
Connecting to server at 127.0.0.1:4001
b'd0df71363130955e493c24ac0d296a75'
Connecting to server at 127.0.0.1:4001
b'1c84c3d6dec3775654c4573ca4df1064'
Connecting to server at 127.0.0.1:4003
b'e52f43cd2c23bb2e6296153748382764'
Connecting to server at 127.0.0.1:4002
b'9aa0c932fb8eba9a72a6ae60064a0507'
Connecting to server at 127.0.0.1:4003
b'6aaae4a8f8468ef61e78b4ced80fa140'
Connecting to server at 127.0.0.1:4001
b'd0df71363130955e493c24ac0d296a75'
Number of Users=6
Number of Users Cached=5
e52f43cd2c23bb2e6296153748382764
Connecting to server at 127.0.0.1:4003
b'{"name": "Irish Rackers", "email": "irackers@gmail.com", "age": 22}'
1c84c3d6dec3775654c4573ca4df1064
Connecting to server at 127.0.0.1:4001
b'{"name": "Bari Pushard", "email": "bpushard@gmail.com", "age": 21}'
6aaae4a8f8468ef61e78b4ced80fa140
Connecting to server at 127.0.0.1:4003
b'{"name": "Lisbeth Stacker", "email": "lstacker@gmail.com", "age": 24}'
9aa0c932fb8eba9a72a6ae60064a0507
Connecting to server at 127.0.0.1:4002
b'{"name": "Agueda Letsinger", "email": "aletsinger@gmail.com", "age": 23}'
d0df71363130955e493c24ac0d296a75
Connecting to server at 127.0.0.1:4001
b'{"name": "John Smith", "email": "jsmith@gmail.com", "age": 20}'

__________________________________________________________________________________________________________________________

(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 1
Cache Server[1] started at 127.0.0.1:4001
('127.0.0.1', 51446):size=176
operation=PUT
id=d0df71363130955e493c24ac0d296a75
payload={'name': 'John Smith', 'email': 'jsmith@gmail.com', 'age': 20}
('127.0.0.1', 50021):size=180
operation=PUT
id=1c84c3d6dec3775654c4573ca4df1064
payload={'name': 'Bari Pushard', 'email': 'bpushard@gmail.com', 'age': 21}
('127.0.0.1', 55127):size=176
operation=PUT
id=d0df71363130955e493c24ac0d296a75
payload={'name': 'John Smith', 'email': 'jsmith@gmail.com', 'age': 20}
('127.0.0.1', 57930):size=82
operation=GET
id=1c84c3d6dec3775654c4573ca4df1064
payload=None
('127.0.0.1', 53482):size=82
operation=GET
id=d0df71363130955e493c24ac0d296a75
payload=None

(base) MacBook-Pro:cmpe273-assignment3 deepav$ cd /Users/deepav/Documents/CMPE-273-sithu/github/cmpe273-assignment4
(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 2
Cache Server[2] started at 127.0.0.1:4002
('127.0.0.1', 51196):size=186
operation=PUT
id=9aa0c932fb8eba9a72a6ae60064a0507
payload={'name': 'Agueda Letsinger', 'email': 'aletsinger@gmail.com', 'age': 23}
('127.0.0.1', 56058):size=82
operation=GET
id=9aa0c932fb8eba9a72a6ae60064a0507
payload=None


(base) MacBook-Pro:cmpe273-assignment3 deepav$ cd /Users/deepav/Documents/CMPE-273-sithu/github/cmpe273-assignment4
(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 3
Cache Server[3] started at 127.0.0.1:4003
('127.0.0.1', 61597):size=181
operation=PUT
id=e52f43cd2c23bb2e6296153748382764
payload={'name': 'Irish Rackers', 'email': 'irackers@gmail.com', 'age': 22}
('127.0.0.1', 61114):size=183
operation=PUT
id=6aaae4a8f8468ef61e78b4ced80fa140
payload={'name': 'Lisbeth Stacker', 'email': 'lstacker@gmail.com', 'age': 24}
('127.0.0.1', 56066):size=82
operation=GET
id=e52f43cd2c23bb2e6296153748382764
payload=None
('127.0.0.1', 60256):size=82
operation=GET
id=6aaae4a8f8468ef61e78b4ced80fa140
payload=None

```


## Part II.

Implement consistent hashing to shard the data.

Features:

* Add virtual node layer in the consistent hashing.
* Implement virtual node with data replication. 


Output
```
(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_client_ch.py
Connecting to server at 127.0.0.1:4001
b'd0df71363130955e493c24ac0d296a75'
Connecting to server at 127.0.0.1:4002
Connecting to server at 127.0.0.1:4000
b'1c84c3d6dec3775654c4573ca4df1064'
Connecting to server at 127.0.0.1:4001
Connecting to server at 127.0.0.1:4000
b'e52f43cd2c23bb2e6296153748382764'
Connecting to server at 127.0.0.1:4001
Connecting to server at 127.0.0.1:4003
b'9aa0c932fb8eba9a72a6ae60064a0507'
Connecting to server at 127.0.0.1:4000
Connecting to server at 127.0.0.1:4000
b'6aaae4a8f8468ef61e78b4ced80fa140'
Connecting to server at 127.0.0.1:4001
Connecting to server at 127.0.0.1:4001
b'd0df71363130955e493c24ac0d296a75'
Connecting to server at 127.0.0.1:4002
Number of Users=6
Number of Users Cached=5
d0df71363130955e493c24ac0d296a75
Connecting to server at 127.0.0.1:4001
b'{"name": "John Smith", "email": "jsmith@gmail.com", "age": 20}'
1c84c3d6dec3775654c4573ca4df1064
Connecting to server at 127.0.0.1:4000
b'{"name": "Bari Pushard", "email": "bpushard@gmail.com", "age": 21}'
6aaae4a8f8468ef61e78b4ced80fa140
Connecting to server at 127.0.0.1:4000
b'{"name": "Lisbeth Stacker", "email": "lstacker@gmail.com", "age": 24}'
e52f43cd2c23bb2e6296153748382764
Connecting to server at 127.0.0.1:4000
b'{"name": "Irish Rackers", "email": "irackers@gmail.com", "age": 22}'
9aa0c932fb8eba9a72a6ae60064a0507
Connecting to server at 127.0.0.1:4003
b'{"name": "Agueda Letsinger", "email": "aletsinger@gmail.com", "age": 23}'

__________________________________________________________________________________________________________________________

(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 0
Cache Server[0] started at 127.0.0.1:4000
('127.0.0.1', 60530):size=180
operation=PUT
id=1c84c3d6dec3775654c4573ca4df1064
payload={'name': 'Bari Pushard', 'email': 'bpushard@gmail.com', 'age': 21}
('127.0.0.1', 59160):size=181
operation=PUT
id=e52f43cd2c23bb2e6296153748382764
payload={'name': 'Irish Rackers', 'email': 'irackers@gmail.com', 'age': 22}
('127.0.0.1', 52434):size=186
operation=PUT
id=9aa0c932fb8eba9a72a6ae60064a0507
payload={'name': 'Agueda Letsinger', 'email': 'aletsinger@gmail.com', 'age': 23}
('127.0.0.1', 58298):size=183
operation=PUT
id=6aaae4a8f8468ef61e78b4ced80fa140
payload={'name': 'Lisbeth Stacker', 'email': 'lstacker@gmail.com', 'age': 24}
('127.0.0.1', 65230):size=82
operation=GET
id=1c84c3d6dec3775654c4573ca4df1064
payload=None
('127.0.0.1', 53267):size=82
operation=GET
id=6aaae4a8f8468ef61e78b4ced80fa140
payload=None
('127.0.0.1', 51194):size=82
operation=GET
id=e52f43cd2c23bb2e6296153748382764
payload=None

(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 1
Cache Server[1] started at 127.0.0.1:4001
('127.0.0.1', 53009):size=176
operation=PUT
id=d0df71363130955e493c24ac0d296a75
payload={'name': 'John Smith', 'email': 'jsmith@gmail.com', 'age': 20}
('127.0.0.1', 65340):size=180
operation=PUT
id=1c84c3d6dec3775654c4573ca4df1064
payload={'name': 'Bari Pushard', 'email': 'bpushard@gmail.com', 'age': 21}
('127.0.0.1', 64371):size=181
operation=PUT
id=e52f43cd2c23bb2e6296153748382764
payload={'name': 'Irish Rackers', 'email': 'irackers@gmail.com', 'age': 22}
('127.0.0.1', 56099):size=183
operation=PUT
id=6aaae4a8f8468ef61e78b4ced80fa140
payload={'name': 'Lisbeth Stacker', 'email': 'lstacker@gmail.com', 'age': 24}
('127.0.0.1', 58182):size=176
operation=PUT
id=d0df71363130955e493c24ac0d296a75
payload={'name': 'John Smith', 'email': 'jsmith@gmail.com', 'age': 20}
('127.0.0.1', 53984):size=82
operation=GET
id=d0df71363130955e493c24ac0d296a75
payload=None

(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 2
Cache Server[2] started at 127.0.0.1:4002
('127.0.0.1', 51955):size=176
operation=PUT
id=d0df71363130955e493c24ac0d296a75
payload={'name': 'John Smith', 'email': 'jsmith@gmail.com', 'age': 20}
('127.0.0.1', 63120):size=176
operation=PUT
id=d0df71363130955e493c24ac0d296a75
payload={'name': 'John Smith', 'email': 'jsmith@gmail.com', 'age': 20}

(base) MacBook-Pro:cmpe273-assignment4 deepav$ python3 cache_server.py 3
Cache Server[3] started at 127.0.0.1:4003
('127.0.0.1', 58666):size=186
operation=PUT
id=9aa0c932fb8eba9a72a6ae60064a0507
payload={'name': 'Agueda Letsinger', 'email': 'aletsinger@gmail.com', 'age': 23}
('127.0.0.1', 64604):size=82
operation=GET
id=9aa0c932fb8eba9a72a6ae60064a0507
payload=None

```
