# API Testing Guide - Inventory Management API v1.0

## Complete API Endpoints

### 1. *GET /* - Root Endpoint (Hello World)
*Status Code:* 200 OK
URL: http://localhost:8000/
Method: GET
*Response Example:*
```json
{
    "message": "Hello World"
}
```

### 2. *GET /items* - List All Items
*Status Code:* 200 OK
URL: http://localhost:8000/items
Method: GET
*Response Example:*
```json
{
    "count": 6,
    "items": {
        "1": {
            "Name": "Intel i5 11th Gen",
            "Price": 10000.0,
            "Description": "Intel i5 11th Gen is a processor..."
        }
    }
}
```

### 3. *GET /items/{item_id}* - Get Specific Item
*Status Code:* 200 OK (Success) | 404 Not Found (Item doesn't exist)
URL: http://localhost:8000/items/1
Method: GET
*Success Response:*
```json
{
    "Name": "Intel i5 11th Gen",
    "Price": 10000.0,
    "Description": "Intel i5 11th Gen is a processor that is used in laptops and desktops."
}
```
*Error Response (404):*
```json
{
    "detail": "Item not found"
}
```

### 4. *POST /items/* - Create New Item
*Status Code:* 201 Created (Success) | 400 Bad Request (Duplicate)
URL: http://localhost:8000/items/
Method: POST
Content-Type: application/json
*Request Body:*
```json
{
    "Name": "New Product",
    "Price": 999.99,
    "Description": "Description of the new product"
}
```
*Success Response (201):*
```json
{
    "id": 7,
    "Name": "New Product",
    "Price": 999.99,
    "Description": "Description of the new product"
}
```
*Error Response (400):*
```json
{
    "detail": "Item already Exist"
}
```

### 5. *PUT /items/{item_id}* - Update Item
*Status Code:* 200 OK (Success) | 404 Not Found | 400 Bad Request (Duplicate name)
URL: http://localhost:8000/items/1
Method: PUT
Content-Type: application/json
*Request Body (all fields optional):*
```json
{
    "Name": "Updated Name",
    "Price": 123.45,
    "Description": "Updated description"
}
```
*Success Response (200):*
```json
{
    "id": 1,
    "Name": "Updated Name",
    "Price": 123.45,
    "Description": "Updated description"
}
```

### 6. *DELETE /items/{item_id}* - Delete Item
*Status Code:* 204 No Content (Success) | 404 Not Found
URL: http://localhost:8000/items/1
Method: DELETE
*Success Response:* Empty body (204 No Content)
*Error Response (404):*
```json
{
    "detail": "Item not found"
}
```

---

## Testing Scenarios

### Scenario 1: Complete CRUD Flow
1. POST /items/ - Create new item (201)
2. GET /items/{item_id} - Verify creation (200)
3. PUT /items/{item_id} - Update item (200)
4. GET /items/{item_id} - Verify update (200)
5. DELETE /items/{item_id} - Remove item (204)
6. GET /items/{item_id} - Verify deletion (404)

### Scenario 2: Data Validation
1. Try creating item with empty name (400)
2. Try creating item with negative price (400)
3. Try creating duplicate item name (400)
4. Try updating to existing item name (400)

---

## HTTP Status Code Summary

| Status Code | Meaning | Used In |
|-------------|---------|---------|
| *200 OK* | Success with response body | GET, PUT |
| *201 Created* | Resource created successfully | POST |
| *204 No Content* | Success, no response body | DELETE |
| *400 Bad Request* | Invalid data or duplicate | POST, PUT |
| *404 Not Found* | Resource doesn't exist | GET, PUT, DELETE |

---

## Testing Tools

### 1. *Swagger UI (Recommended)*
- URL: http://localhost:8000/docs
- Interactive testing interface
- Auto-generated documentation
- Real-time response viewing

### 2. *PowerShell Commands*
```powershell
# GET all items
Invoke-RestMethod -Uri "http://localhost:8000/items" -Method Get

# POST new item
$body = @{
    Name = "Test Product"
    Price = 999.99
    Description = "Test description"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/items/" -Method Post -Body $body -ContentType "application/json"

# DELETE item
Invoke-RestMethod -Uri "http://localhost:8000/items/1" -Method Delete
```

### 3. *Python Requests*
```python
import requests

# Create item
response = requests.post(
    "http://localhost:8000/items/",
    json={
        "Name": "Test Product",
        "Price": 999.99,
        "Description": "Test description"
    }
)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
```

---

## Data Model Requirements

### ItemIn Model
- Name: Required, non-empty string
- Price: Required, number >= 0
- Description: Optional string

### ItemUpdate Model
- Name: Optional, non-empty string if provided
- Price: Optional, number >= 0 if provided
- Description: Optional string

---

## Setup Instructions

1. Ensure Python 3.x is installed
2. Install required packages:
   ```powershell
   pip install fastapi uvicorn
   ```
3. Start the server:
   ```powershell
   uvicorn lab1:app --reload
   ```
4. Access API at http://localhost:8000
5. Access Swagger UI at http://localhost:8000/docs

---

## Testing Checklist

- [ ] Verify all CRUD operations
- [ ] Test data validation rules
- [ ] Check error responses
- [ ] Validate status codes
- [ ] Test edge cases
- [ ] Confirm unique name constraint
- [ ] Verify optional fields behavior