from fastapi import FastAPI, HTTPException, Body, Query
from library_mysql import module_sqlite

app = FastAPI()
app.title = "Welcome to flet-box ApiChat"
app.version = "0.1"


instance = module_sqlite(
    path_db="/data/data/com.termux/files/home/storage/shared/database.db"
)
data_key = [
    "id",
    "sender",
    "content",
    "group_chat",
    "receiver_private",
    "timestamp",
    "edited",
    "confirmed",
    "reply_to",
    "type",
    "device",
    "visibility",
    "language",
]


def raice_error(status_code: int = 404, detail: str = "Page Don't not exit"):
    return HTTPException(status_code=status_code, detail=detail)


# PARAMETROS QUERY viaja por el url [ GET, DELETE, HEAD ]
# una sola consulta existe?
@app.head("/chat/data/document/{doc_name}", tags=["check-status"])
async def get_document_path(doc_name: str = ""):
    """
    ### doc_name necesario ponerlo porque es la llave del diccionary

    - chat/document?doc_name=[value]

    ```python
    requests.get(url='chat/document', params={'doc_name':'javier'})
    ```
    """
    print(doc_name)
    return {"doc_name": doc_name}


# PARAMETROS QUERY viaja por el url [ GET, DELETE, HEAD ]
# una sola consulta existe?
@app.head("/chat/data/{group}/{user}", tags=["check-status"])
async def check_status_user(group: str = "", user: str = ""):
    """
     ###  solamente recive dos parametro por url - path

     - Chat/[group]/[user]

    ```python
    requests.get(url='chat/{group}/{user}')
    ```
    `"""
    # print(group, user)
    check_status = instance.read_table_values_where(
        table_name=group.strip(""), read_data_where=("sender", user)
    )
    # print(response)
    return check_status


# PARAMETROS QUERY viaja por el url [ GET, DELETE, HEAD ]
# una sola consulta existe?
@app.head("/chat/users/registered", tags=["check-status"])
async def get_dump_list_users(group: str = ""):
    """
     ###  solamente recive dos parametro por url - path

     - Chat/[group]

    ```python
    requests.get(url="/chat/users/registered")
    ```
    `"""
    # print(group, message)
    check_status = instance.read_all_table_and_columns(table_name="api_users")

    if check_status[0]:
        return (True, [_["user_name"] for _ in check_status[1]])

    return check_status


# user PATH
@app.get("/", tags=["client-status"])
async def get_chat():
    return {
        "message": "Welcome to chat-bot Api server",
        "documentation": "https://192.168.43.1:8000/docs",
    }


@app.get("/favicon.ico", tags=["client-status"])
async def get_favico():
    return {"message": "icon.png"}


@app.get("/{documentation}", tags=["client-status"])
async def get_wrong_path(documentation: str):
    return {"documentation": "this documentation aren't preparate yet"}


# PARAMETROS QUERY viaja por el url [ GET, DELETE, get ]
# una sola consulta existe?
@app.get("/chat/data/users/messages", tags=["client-status"])
async def get_dump_message_users(group: str = ""):
    """
     ###  solamente recive dos parametro por url - path

     - Chat/[group]

    ```python
    requests.get(url="/chat/users/registered")
    ```
    `"""
    # print(group, message)
    check_status = instance.read_all_table_and_columns(table_name=group.strip(""))

    return check_status


# PARAMETROS QUERY viaja por el url [ GET, DELETE ]
@app.get("/chat/message/{group_name}/{chat_id}", tags=["client-status"])
async def get_message_id(group_name: str = "public", chat_id: str = "chat-id"):
    """
    ### user_name necesario ponerlo porque es la llave del diccionary

    -  chat/message?user_name=[value]&content=[value]

    ```python
    requests.get(
        url='chat/message',
        params={'user_name':'javier', 'content': 'hello world' }
    )
    ```
    """
    check_status = instance.read_table_values_where(
        table_name=group_name.strip(""), read_data_where=("id", chat_id.strip(""))
    )

    return check_status


# PARAMETROS BODY viaja como json[ POST, PUT ] pero mas usado POST para
# llenar base datos porque es mucha informacion
@app.post("/chat/message/add/{group_name}", tags=["editing-status"])
async def post_add_message(group_name: str = "public", payload: dict = Body(...)):
    """
    ### necesario todo se manda al servidor

    - json.dumps() , chat/add

    ```python
    json_data = {
        "id":"22",
        "sender":"javier",
        "reciver":"False",
        "content":"hello world",
        "group_chat":"global",
        "receiver_private":"False",
        "timestamp":"[time spand]",
        "edited":"False",
        "confirmed":"True",
        "reply_to":"False",
        "type":"chat",
        "device":"Sansung A13",
        "visibility":"True",
        "language":"es"
    }
    requests.post(url='chat/testing', json=json.dumps(json_data))
    ```
    """
    if not payload:
        return (False, "table name and query params can't by empty")

    check_status = instance.create_values_in_table_where(
        table_name=group_name.strip(""), column_data=tuple(payload.values())
    )

    return check_status


# PARAMETROS BODY viaja como json[ POST, PUT, PATCH] pero mas usado PUT para
# Actualizar base datos pocos datos
@app.put("/chat/message/update/{group_name}", tags=["editing-status"])
async def put_update_chat(group_name: str = "global_chat", payload: dict = Body(...)):
    """
    ### necesario todo se manda al servidor en forma de data == formulario

    - chat/add , data

    ```python
    json_data = {'id':'1' ,'content':'hello world'}
    requests.post(url='chat/testing', data=json.dumps(json_data))
    ```
    """
    print(payload)
    check_status = instance.update_table_values_where(
        table_name=group_name.strip(""),
        change_data_where=("id", payload.get("id", False)),
        by_data=("content", payload.get("content", False)),
    )
    return check_status


# PARAMETROS BODY viaja como json[ POST, PUT, PATCH] pero mas usado PUT para
# Actualizar base datos un datos en concreto
@app.patch("/chat/nessage/update/{group_name}", tags=["editing-status"])
async def patch_change_path(group_name: str = "global_chat", payload: dict = Body(...)):
    """
    ### necesario todo se manda al servidor en forma de data == formulario

    - chat/add , data = { 'content': 'hello world'} => json.dumps()

    ```python
    requests.patch(url='chat/testing', data=json.dumps({'content':'javier' }))
    ```
    """

    status_code = instance.update_table_values_where(
        table_name=group_name.strip(""),
        change_data_where=("id", payload.get("id", False)),
        by_data=("content", payload.get("content", False)),
    )
    return status_code


# PARAMETROS QUERY viaja por el url [ GET, DELETE ]
@app.delete("/chat/message/delete", tags=["editing-status"])
async def delete_id_path(payload: dict = Body(...)):
    """
    ### group_name necesario ponerlo porque es la llave del diccionary

    - chat/delete?group_name=[value]&chat_id=[value]
    ```python

    json_data = {"group_name":"global_chat" , "id": "2"}
    requests.get(url='chat/delete', params=json_data)
    ```
    """
    status_code = instance.remove_table_values_where(
        # table_name=group_name.strip(''), remove_data_where=chat_id.values()
        table_name=payload.get("group_name", False),
        remove_data_where=("id", payload.get("id", False)),
    )

    return status_code


# PARAMETROS QUERY viaja por el url [ GET, DELETE, get ]
# una sola consulta existe?
@app.get("/server/info/get-table-names", tags=["admin-privilege"])
async def get_data_tables():
    """
     ###  solamente recive dos parametro por url - path

     - Chat/[group]

    ```python
    requests.get(url="/chat/users/registered")
    ```
    `"""
    # print(group, message)
    check_status = instance.read_tables_from_database()

    return check_status


# PARAMETROS QUERY viaja por el url [ GET, DELETE, get ]
# una sola consulta existe?
@app.get("/server/info/get-table-names-structure", tags=["admin-privilege"])
async def get_data_tables_structure(table_name: str = Query()):
    """
         ###  solamente recive dos parametro por url - path
    }
         - Chat/[group]

        ```python
        requests.get(url="/chat/users/registered")
        ```
        `"""
    # print(group, message)
    check_status = instance.check_table_name_structure(table_name=table_name.strip(""))

    return check_status


# PARAMETROS BODY viaja como json[ POST, PUT, PATCH] pero mas usado PUT para
# Crear nuevi chat datos
@app.post("/server/info/create-table-columns", tags=["admin-privilege"])
async def create_database(table_name: str = Query(), payload: dict = Body(...)):
    """
    ### necesario todo se manda al servidor en forma de data == formulario

    - cjson.dumps() chat/add , data

    ```python
    table_dame = {
        "table_name":"global_chat"
    }

    json_data = {
        "id":"TEXT",
        "sender":"TEXT",
        "reciver":"TEXT",
        "content":"TEXT",
        "group_chat":"TEXT",
        "receiver_private":"TEXT",
        "timestamp":"TEXT",
        "edited":"TEXT",
        "confirmed":"TEXT",
        "reply_to":"TEXT",
        "type":"TEXT",
        "device":"TEXT",
        "visibility":"TEXT",
        "language":"TEXT"
    }

    requests.post(
        url='create_database?table_name=[value]', data=json.dumps(json_data)
    )
    ```
    """
    if not table_name and not payload:
        return (False, "table name and query params can't by empty")

    status_code = instance.create_table(
        table_name=table_name.strip(""), column_data=payload
    )

    return status_code


# PARAMETROS QUERY viaja por el url [ GET, DELETE, get ]
# una sola consulta existe?
@app.put("/server/rename-table-names-structure", tags=["admin-privilege"])
async def rename_table_structure(payload: dict = Body()):
    """
     ###  solamente recive dos parametro por url - path
    }
     - Chat/[group]

    ```python
    payload = {
        "old_table":"name_of_current_table",
        "new_table":"name_new_table"
    }
    requests.post(url="/server/rename-table-names-structure")
    ```
    `"""
    # print(group, message)
    check_status = instance.rename_table(
        old_table_name=payload.get("old_table", False),
        new_table_name=payload.get("new_table", False),
    )

    return check_status


# PARAMETROS QUERY viaja por el url [ GET, DELETE, get ]
# una sola consulta existe?
@app.put("/server/rename-column-name-structure", tags=["admin-privilege"])
async def rename_column_structure(payload: dict = Body()):
    """
     ###  solamente recive dos parametro por url - path
    }
     - Chat/[group]

    ```python
    payload = {
        "table_name":"table_name",
        "old_column":"name_of_current_column",
        "new_column":"name_new_column"
    }
    requests.post(url="/server/rename-column-name-structure")
    ```
    `"""
    # print(group, message)
    check_status = instance.rename_value_in_table(
        table_name=payload.get("table_name", False),
        old_column_name=payload.get("old_column", False),
        new_column_name=payload.get("new_column", False),
    )

    return check_status


# PARAMETROS QUERY viaja por el url [ GET, DELETE ]
@app.delete("/server/delete-table-name", tags=["admin-privilege"])
async def delet_table_name(table_name: str = Query()):
    """
    ### group_name necesario ponerlo porque es la llave del diccionary

    - chat/delete?group_name=[value]&chat_id=[value]
    ```python

    json_data = {'group_name':'javier' , 'chat_id': 'hello world'}
    requests.get(url='chat/delete', params=json_data)
    ```
    """
    status_code = instance.remove_table(table_name=table_name.strip(""))

    return status_code
