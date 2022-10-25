import logging
import azure.functions as func
import json


def main(req: func.HttpRequest, docs: func.DocumentList) -> func.HttpResponse:
    userId = req.params.get('dueDate')
    logging.info('Python HTTP trigger function processed a request.')
    if not docs:
        logging.warning("no TODO items found for DueDate")
        return func.HttpResponse(
            "[]",
            status_code=200
        )
    else:
        logging.info("tasks found for due date")
        output=[]
        for doc in docs:
            output.append(doc.to_json())
        logging.info(str(output))
        return func.HttpResponse(
            str(output),  
            status_code=200
        )
