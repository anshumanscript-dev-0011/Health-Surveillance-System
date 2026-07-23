# API Design

## Authentication APIs

| Method | Endpoint                   | Description            | Access        |
| ------ | -------------------------- | ---------------------- | ------------- |
| POST   | /api/auth/login/           | User login             | Public        |
| POST   | /api/auth/logout/          | User logout            | Authenticated |
| POST   | /api/auth/refresh/         | Refresh access token   | Authenticated |
| POST   | /api/auth/change-password/ | Change password        | Authenticated |
| POST   | /api/auth/forgot-password/ | Request password reset | Public        |

---

## User APIs

| Method | Endpoint         | Description | Access      |
| ------ | ---------------- | ----------- | ----------- |
| GET    | /api/users/      | List users  | Super Admin |
| POST   | /api/users/      | Create user | Super Admin |
| GET    | /api/users/{id}/ | View user   | Super Admin |
| PUT    | /api/users/{id}/ | Update user | Super Admin |
| DELETE | /api/users/{id}/ | Delete user | Super Admin |

---

## Patient APIs

| Method | Endpoint            | Description      | Access                |
| ------ | ------------------- | ---------------- | --------------------- |
| GET    | /api/patients/      | List patients    | Health Worker, Doctor |
| POST   | /api/patients/      | Register patient | Health Worker         |
| GET    | /api/patients/{id}/ | Patient details  | Health Worker, Doctor |
| PUT    | /api/patients/{id}/ | Update patient   | Health Worker         |
| DELETE | /api/patients/{id}/ | Delete patient   | Super Admin           |

---

## Disease APIs

| Method | Endpoint            | Description           | Access                |
| ------ | ------------------- | --------------------- | --------------------- |
| GET    | /api/diseases/      | List diseases         | Authenticated         |
| POST   | /api/diseases/      | Create disease report | Health Worker, Doctor |
| GET    | /api/diseases/{id}/ | Disease details       | Authenticated         |
| PUT    | /api/diseases/{id}/ | Update disease report | Doctor                |
| DELETE | /api/diseases/{id}/ | Delete report         | Super Admin           |

---

## Dashboard APIs

| Method | Endpoint                    | Description             | Access         |
| ------ | --------------------------- | ----------------------- | -------------- |
| GET    | /api/dashboard/overview/    | Dashboard summary       | Health Officer |
| GET    | /api/dashboard/trends/      | Disease trends          | Health Officer |
| GET    | /api/dashboard/predictions/ | AI outbreak predictions | Health Officer |
| GET    | /api/dashboard/alerts/      | Active alerts           | Health Officer |

---

## Notification APIs

| Method | Endpoint                      | Description          | Access        |
| ------ | ----------------------------- | -------------------- | ------------- |
| GET    | /api/notifications/           | List notifications   | Authenticated |
| GET    | /api/notifications/{id}/      | Notification details | Authenticated |
| PUT    | /api/notifications/{id}/read/ | Mark as read         | Authenticated |
| DELETE | /api/notifications/{id}/      | Delete notification  | Authenticated |

---

## Error Responses

| Status Code               | Description                       |
| ------------------------- | --------------------------------- |
| 200 OK                    | Request completed successfully    |
| 201 Created               | Resource created successfully     |
| 204 No Content            | Resource deleted successfully     |
| 400 Bad Request           | Invalid request data              |
| 401 Unauthorized          | Authentication required           |
| 403 Forbidden             | User lacks permission             |
| 404 Not Found             | Requested resource does not exist |
| 405 Method Not Allowed    | HTTP method not supported         |
| 409 Conflict              | Duplicate or conflicting resource |
| 500 Internal Server Error | Unexpected server error           |
