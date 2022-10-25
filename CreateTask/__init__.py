import logging
import uuid
import datetime
import json
import azure.functions as func


def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    req_body = req.get_json()
    description = req_body.get('description')
    notes = req_body.get('notes')
    dueDate = req_body.get('dueDate')
    id = uuid.uuid4()
    dt = datetime.datetime.utcnow()
    my_dict = {
        "id": str(id),
        "description": str(description),
        "notes": str(notes),
        "dueDate": str(dueDate)
    }
    my_json = json.dumps(my_dict)
    logging.info(my_json)
    doc.set(func.Document.from_json(my_json))
    doc.get()

    return func.HttpResponse(
             "successfully added Task",
             status_code=200
    )
