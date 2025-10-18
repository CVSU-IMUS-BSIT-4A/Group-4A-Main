# LabAct - ITEC111

## Project Overview
**Subject:** ITEC 111  
**Group:** Team Group 4A 
**Repository:** Group-4A-Main   

## Team Members
- **Moral, Andrie B.**
- **Abelita, Czyrell Gwen R.**
- **Gangan, Demrose Carla C.**
- **Aranzasu, Darryl Jedidiah A.**
- **Aranzasu, Darrylene Kaela A.**
- **Relox, Nathaniel**

## FastAPI Inventory Management API

A FastAPI-based REST API for managing inventory operations. This API provides a complete set of CRUD operations (Create, Read, Update, Delete) with proper HTTP status codes, error handling, and data validation.

## Features
- **Full CRUD Operations** for inventory items
- **Proper HTTP Status Codes** (200, 201, 204, 400, 404)
- **Data Validation** using Pydantic models
- **Error Handling** with descriptive messages
- **Auto-generated Documentation** (Swagger UI & ReDoc)
- **Duplicate Name Prevention** for items
- **Optional Fields Support** in updates

## Prerequisites
- Python 3.6 or higher (for FastAPI compatibility)
- FastAPI (for building the REST API)
- Uvicorn (ASGI server for running the FastAPI application)
- Pydantic (for data validation and serialization)
- typing (standard library for type hints)

## Activity Compliance

### API Implementation
- ✅ GET endpoints with proper responses
- ✅ POST endpoint with 201 Created status
- ✅ PUT endpoint with validation
- ✅ DELETE endpoint with 204 No Content
- ✅ Error handling (404, 400)
- ✅ Duplicate prevention
- ✅ FastAPI Response handling

## API Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/` | Hello World endpoint | 200 |
| GET | `/items` | List all inventory items | 200 |
| GET | `/items/{item_id}` | Get specific item | 200, 404 |
| POST | `/items/` | Create new item | 201, 400 |
| PUT | `/items/{item_id}` | Update existing item | 200, 404, 400 |
| DELETE | `/items/{item_id}` | Delete item | 204, 404 |

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/CVSU-IMUS-BSIT-4A/Group-4A-Main.git
cd Group-4A-Main
```

2. **Install dependencies**
```bash
pip install fastapi uvicorn pydantic
```

### Running the Application
```bash
uvicorn lab1:app --reload
```

The API will be available at: `http://localhost:8000`

### API Documentation
Once running, access:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Quick Test Examples

**Create an item:**
```bash
curl -X POST "http://localhost:8000/items/" \
  -H "Content-Type: application/json" \
  -d '{"Name": "New CPU", "Price": 5000.0, "Description": "New processor"}'
```

**Update an item:**
```bash
curl -X PUT "http://localhost:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{"Name": "Updated CPU", "Price": 6000.0}'
```

**Delete an item:**
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

## HTTP Status Codes

### Success Responses
- **200 OK** - Successful GET/PUT requests
- **201 Created** - Successful item creation
- **204 No Content** - Successful deletion

### Client Error Responses
- **400 Bad Request** - Duplicate item or invalid data
- **404 Not Found** - Item doesn't exist

## Data Models

### ItemIn (POST)
```json
{
  "Name": "string",
  "Price": 0.0,
  "Description": "string"
}
```

### ItemUpdate (PUT - all fields optional)
```json
{
  "Name": "string",
  "Price": 0.0,
  "Description": "string"
}
```

## Project Structure
```
Group-4A-Main/
│
├── lab1.py        # Main FastAPI application
├── readme.md            # This file
└── .API_Testing         # Testing Guide
└── .git/               # Git repository
```

## Initial Data
The API comes with pre-populated items including:

1. **Intel Core i5-11400F** - 6-core 11th Gen Intel processor (₱9,500)
   - Ideal for mid-range gaming and productivity

2. **AMD Ryzen 5 5600G** - 6-core CPU with integrated graphics (₱9,800)
   - Great for budget gaming PCs

3. **AMD Ryzen 7 5800X** - 8-core high-performance CPU (₱16,500)
   - Perfect for gaming and heavy multitasking workloads

4. **Intel Core i7-12700K** - 12th Gen Intel processor (₱21,000)
   - Features hybrid architecture for top-tier performance

5. **NVIDIA GeForce RTX 3060** - Mid-range graphics card (₱23,000)
   - Capable of ray tracing and smooth 1080p/1440p gaming

6. **Corsair Vengeance LPX 16GB DDR4** - High-speed memory kit (₱4,500)
   - Optimized for gaming PCs and workstation builds

## Learning Outcomes
- REST API development with FastAPI
- HTTP status code implementation
- CRUD operations design
- Data validation using Pydantic
- Error handling patterns
- API documentation with Swagger/ReDoc

