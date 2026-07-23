# User Roles

## Super Admin

### Responsibilities

* Manage the entire system.
* Create, update, and deactivate user accounts.
* Assign roles and permissions.
* Configure system settings.
* Monitor system health and activity.
* View audit logs.
* Manage districts, health centers, and hospitals.

### Accessible Modules

* Authentication
* User Management
* Health Center Management
* Dashboard
* Reports
* Audit Logs
* System Settings

### Permissions

* Full access to all modules.
* Create, Read, Update, Delete (CRUD) on every resource.
* Manage roles and permissions.
* Configure application settings.

---

## Health Officer

### Responsibilities

* Monitor disease trends across assigned regions.
* Review disease reports submitted by health workers and hospitals.
* Analyze dashboards and AI predictions.
* Generate surveillance reports.
* Coordinate outbreak response.
* Monitor multiple health centers.

### Accessible Modules

* Dashboard
* Disease Reports
* Analytics
* Notifications
* Reports

### Permissions

* View all reports within assigned jurisdiction.
* Verify disease reports.
* Generate reports.
* View AI predictions and alerts.
* Cannot manage system users or application settings.

---

## Health Worker

### Responsibilities

* Conduct field visits.
* Register patients.
* Collect symptoms and health information.
* Submit disease reports.
* Update patient follow-up information.
* Record community health surveys.
* Report suspected disease outbreaks.

### Accessible Modules

* Patient Management
* Disease Reporting
* Notifications
* Personal Profile

### Permissions

* Create patient records.
* Update assigned patient records.
* Submit disease reports.
* View own submitted reports.
* Cannot access analytics dashboards.
* Cannot manage users or system settings.

---

## Doctor

### Responsibilities

* Diagnose patients.
* Confirm disease cases.
* Update patient diagnosis.
* Prescribe treatment information.
* Review patient medical history.
* Approve disease reports when necessary.

### Accessible Modules

* Patient Management
* Disease Reporting
* Laboratory Reports
* Notifications

### Permissions

* View patient records.
* Update diagnosis.
* Confirm disease cases.
* Access laboratory results.
* Cannot manage users or administrative settings.

---

## Lab Staff

### Responsibilities

* Perform laboratory tests.
* Upload laboratory reports.
* Verify diagnostic results.
* Update test status.
* Support disease confirmation.

### Accessible Modules

* Laboratory Reports
* Disease Reporting
* Notifications

### Permissions

* Upload laboratory reports.
* Update test results.
* View assigned patient information.
* Cannot modify patient registration details.
* Cannot access administrative modules.

---

## Citizen

### Responsibilities

* View public health advisories.
* Receive emergency notifications.
* View awareness campaigns.
* Submit self-health assessments (future enhancement).

### Accessible Modules

* Public Dashboard
* Health Advisories
* Notifications

### Permissions

* View public information only.
* Submit self-assessment forms (future).
* Cannot access confidential health records.

---

# Permissions Matrix

| Module              | Super Admin | Health Officer | Health Worker | Doctor | Lab Staff | Citizen |
| ------------------- | :---------: | :------------: | :-----------: | :----: | :-------: | :-----: |
| Authentication      |      ✅      |        ✅       |       ✅       |    ✅   |     ✅     |    ✅    |
| User Management     |      ✅      |        ❌       |       ❌       |    ❌   |     ❌     |    ❌    |
| Patient Management  |      ✅      |       👁️      |       ✅       |    ✅   |    👁️    |    ❌    |
| Disease Reporting   |      ✅      |       👁️      |       ✅       |    ✅   |     ✅     |    ❌    |
| Laboratory Reports  |      ✅      |       👁️      |       ❌       |   👁️  |     ✅     |    ❌    |
| Analytics Dashboard |      ✅      |        ✅       |       ❌       |   👁️  |     ❌     |    ❌    |
| AI Predictions      |      ✅      |        ✅       |       ❌       |   👁️  |     ❌     |    ❌    |
| Notifications       |      ✅      |        ✅       |       ✅       |    ✅   |     ✅     |    ✅    |
| Reports             |      ✅      |        ✅       |      👁️      |   👁️  |    👁️    |    ❌    |
| Audit Logs          |      ✅      |       👁️      |       ❌       |    ❌   |     ❌     |    ❌    |
| System Settings     |      ✅      |        ❌       |       ❌       |    ❌   |     ❌     |    ❌    |

### Legend

* ✅ Full Access
* 👁️ View Only
* ❌ No Access
