import logging

import azure.functions as func
from azure.cosmos import CosmosClient
import os



def main(req: func.HttpRequest, doc: func.DocumentList) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    if not doc:
        logging.warning("id not found")
        return func.HttpResponse(
            "TASK ID Not Found",
            status_code=400
        )
    else:
        logging.info("task ID Found")
        id = req.params.get('id')
        conn_string = os.environ['AzureCosmosDBConnectionString']
        url = conn_string.split(";")[0]
        key = conn_string.split(";")[1]
        url = url[url.find('=')+1:]
        key = key[key.find('=')+1:]
        client = CosmosClient(url,key)
        database = client.get_database_client("todo-db-sql-cosmos")
        container = database.get_container_client("todo")
        container.delete_item(id,id)
        return func.HttpResponse(
             "Task deleted",
             status_code=200
        )
