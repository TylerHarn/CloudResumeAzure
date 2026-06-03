import unittest
import json
from unittest.mock import patch, MagicMock
import azure.functions as func

class TestVisitorCounter(unittest.TestCase):

    @patch("function_app.TableServiceClient")
    @patch.dict("os.environ", {"COSMOS_CONNECTION_STRING": "fake_conn"})
    def test_count_increments(self, mock_client):
        mock_table = MagicMock()
        mock_table.get_entity.return_value = {
            "PartitionKey": "visitors", "RowKey": "count", "Count": 5
        }
        mock_client.from_connection_string.return_value \
            .get_table_client.return_value = mock_table

        from function_app import main
        req = func.HttpRequest(
            method="POST", body=b"", url="/api/visitor_counter", params={}
        )
        response = main(req)
        body = json.loads(response.get_body())

        self.assertEqual(body["count"], 6)
        mock_table.update_entity.assert_called_once()

    @patch("function_app.TableServiceClient")
    @patch.dict("os.environ", {"COSMOS_CONNECTION_STRING": "fake_conn"})
    def test_returns_json(self, mock_client):
        mock_table = MagicMock()
        mock_table.get_entity.return_value = {
            "PartitionKey": "visitors", "RowKey": "count", "Count": 10
        }
        mock_client.from_connection_string.return_value \
            .get_table_client.return_value = mock_table

        from function_app import main
        req = func.HttpRequest(
            method="GET", body=b"", url="/api/visitor_counter", params={}
        )
        response = main(req)
        self.assertEqual(response.mimetype, "application/json")

if __name__ == "__main__":
    unittest.main()