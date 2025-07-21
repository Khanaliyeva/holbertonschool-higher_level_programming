# test_03_http_server.py
import urllib.request
import json

def test_get(path, expected_status, expected_keyword):
    try:
        with urllib.request.urlopen(f"http://localhost:8000{path}") as response:
            status = response.getcode()
            content = response.read().decode()
            assert status == expected_status, f"{path} returned {status}, expected {expected_status}"
            assert expected_keyword in content, f"{path} response missing expected keyword: '{expected_keyword}'"
            print(f"Test {path}: OK")
    except Exception as e:
        print(f"Test {path}: FAIL - {e}")

# Testlər
test_get("/", 200, "Hello")
test_get("/data", 200, "John")
test_get("/status", 200, "OK")
test_get("/undefined", 404, "Endpoint not found")
