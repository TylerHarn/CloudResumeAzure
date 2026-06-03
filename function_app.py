import logging, json, os
import azure.functions as func
from azure.data.tables import TableServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        conn_str = os.environ["COSMOS_CONNECTION_STRING"]
        service = TableServiceClient.from_connection_string(conn_str)
        table = service.get_table_client("VisitorCount")

        entity = table.get_entity(partition_key="visitors", row_key="count")
        new_count = entity["Count"] + 1
        entity["Count"] = new_count
        table.update_entity(entity)

        return func.HttpResponse(
            json.dumps({"count": new_count}),
            mimetype="application/json",
            headers={"Access-Control-Allow-Origin": "*"}
        )
    except Exception as e:
        logging.error(e)
        return func.HttpResponse("Error", status_code=500)