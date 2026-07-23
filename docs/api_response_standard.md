# API Response Standard

## Overview

To maintain consistency across the Smart Health Surveillance & Early Warning System, every API response must follow a standardized JSON structure. This ensures predictable communication between the frontend and backend, simplifies error handling, and improves maintainability.

---

# Success Response

All successful API requests should return the following format:

```json
{
    "success": true,
    "message": "Operation completed successfully.",
    "data": {}
}
```

### Response Fields

| Field   | Type                  | Description                                   |
| ------- | --------------------- | --------------------------------------------- |
| success | Boolean               | Indicates whether the request was successful. |
| message | String                | Human-readable success message.               |
| data    | Object / Array / Null | Response payload returned by the API.         |

---

## Example: Create Patient

**HTTP Status:** `201 Created`

```json
{
    "success": true,
    "message": "Patient registered successfully.",
    "data": {
        "id": 101,
        "name": "Rahul Kumar",
        "age": 35,
        "gender": "Male"
    }
}
```

---

## Example: Get Patient Details

**HTTP Status:** `200 OK`

```json
{
    "success": true,
    "message": "Patient retrieved successfully.",
    "data": {
        "id": 101,
        "name": "Rahul Kumar",
        "age": 35,
        "gender": "Male"
    }
}
```

---

## Example: List Patients

**HTTP Status:** `200 OK`

```json
{
    "success": true,
    "message": "Patients retrieved successfully.",
    "data": [
        {
            "id": 101,
            "name": "Rahul Kumar"
        },
        {
            "id": 102,
            "name": "Anita Singh"
        }
    ]
}
```

---

# Pagination Response

For paginated endpoints, return pagination information inside the `data` object.

**HTTP Status:** `200 OK`

```json
{
    "success": true,
    "message": "Patients retrieved successfully.",
    "data": {
        "count": 150,
        "next": "/api/v1/patients/?page=2",
        "previous": null,
        "results": [
            {
                "id": 101,
                "name": "Rahul Kumar"
            }
        ]
    }
}
```

---

# Error Response

All failed API requests should return the following format:

```json
{
    "success": false,
    "message": "Validation failed.",
    "errors": {}
}
```

### Response Fields

| Field   | Type           | Description                         |
| ------- | -------------- | ----------------------------------- |
| success | Boolean        | Always `false` for failed requests. |
| message | String         | General description of the error.   |
| errors  | Object / Array | Detailed error information.         |

---

## Validation Error

**HTTP Status:** `400 Bad Request`

```json
{
    "success": false,
    "message": "Validation failed.",
    "errors": {
        "email": [
            "This field is required."
        ]
    }
}
```

---

## Authentication Error

**HTTP Status:** `401 Unauthorized`

```json
{
    "success": false,
    "message": "Authentication credentials were not provided.",
    "errors": {}
}
```

---

## Authorization Error

**HTTP Status:** `403 Forbidden`

```json
{
    "success": false,
    "message": "You do not have permission to perform this action.",
    "errors": {}
}
```

---

## Resource Not Found

**HTTP Status:** `404 Not Found`

```json
{
    "success": false,
    "message": "Patient not found.",
    "errors": {}
}
```

---

## Conflict Error

**HTTP Status:** `409 Conflict`

```json
{
    "success": false,
    "message": "A patient with this identifier already exists.",
    "errors": {}
}
```

---

## Internal Server Error

**HTTP Status:** `500 Internal Server Error`

```json
{
    "success": false,
    "message": "An unexpected error occurred. Please try again later.",
    "errors": {}
}
```

---

# HTTP Status Codes

| Status Code | Description           | Usage                               |
| ----------- | --------------------- | ----------------------------------- |
| 200         | OK                    | Request completed successfully      |
| 201         | Created               | Resource created successfully       |
| 204         | No Content            | Resource deleted successfully       |
| 400         | Bad Request           | Invalid input or validation failure |
| 401         | Unauthorized          | Authentication required             |
| 403         | Forbidden             | User does not have permission       |
| 404         | Not Found             | Requested resource does not exist   |
| 405         | Method Not Allowed    | HTTP method not supported           |
| 409         | Conflict              | Duplicate or conflicting resource   |
| 500         | Internal Server Error | Unexpected server error             |

---

# API Response Guidelines

* Every response must be valid JSON.
* Always include the `success` field.
* Always include the `message` field.
* Return business data inside the `data` field for successful requests.
* Return detailed validation or processing issues inside the `errors` field for failed requests.
* Use the appropriate HTTP status code for every response.
* Avoid exposing internal exception details, database errors, or stack traces in production responses.
* Keep response messages simple, clear, and consistent across all APIs.

---

# Future Improvements

As the project grows, the response format may be extended to include additional metadata such as:

* Request ID (for tracing)
* API Version
* Response Timestamp (UTC)
* Execution Time
* Rate Limit Information
* Pagination Metadata
* Correlation ID for distributed services

These enhancements can be added without changing the core response structure.
