"""
### GET HEAD
```python

# READ data from URL
@app.get('/url/path'):
async def get_method():
requests.get(url='/url/path')
```

### READ, DELETE
 - data from URL method with Query
 - url = 'https://url/path?query_data=value&age=57'

```python

@app.get('/url/path/{query_data}'):
async def get_method_query(query_data: dict=Query({ 'query_data':'value', 'age':56 }):
requests.get(url=u'/url/path', param={ 'query_data':'value', 'age':56 })
```

### READ, DELETE
 - data from URL method with Query
 - url = 'https://url/path?query_data=value'

```python

@app.get('/url/path/{query_data}'):
async def get_method_query(query_data: str=''):
requests.get(url=/url/path, param={ 'query_data':'value'})
```

### UPDATE [ put, patch]
 - send data from URL method query and json
 - 'https://url/path?query_data=value'
 - only in put, patch

``` python

@app.put('/url/path/{query_data}'):
async def put_method_query(query_data: str='' , payload: dict = Body(...)):
requests.put(url=/url/path?query_data=value, data=json.dumps(payload))
```

### CREATE [ post ]
 - data from URL method with Query and Body or json
 - send data from URL method query and json
 - payload = {'id':'45', 'value':'hello world'}
 - table_dame = {"table_name":"global_chat"}

```python

@app.post('/url/path'):
async def get_method_query(query_data: dict=Query() , payload: dict = Body(...)):
requests.post(url=/url/path, param=table_name, json=json.dumps(payload)

```
"""
