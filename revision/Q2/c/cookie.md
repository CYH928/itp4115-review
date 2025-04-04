# Set cookie
```python
from flask import Flask, render_template
app = Flask(__name__)

app.setcookie('loginname', value='lwl123', max_age=86400, secure=True)
```
### Question: 
How to implement Cookie in Python? please write down a code sample for a cookie with name **loginname** and value **lwl123** with expiry date of **1 day**. 

### Answer:
```setcookie('loginname', value='lwl123', max_age=86400, secure=True)```

### Solve: 
1 day = 60 sec * 60 min * 24 hours \
**86400s** = 60 * 60 * 24

---
# Delete Cookie
```python
app.setcookie('loginname', '', expires=0)
```
