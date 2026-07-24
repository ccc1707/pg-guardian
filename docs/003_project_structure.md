# Project Structure

## Overview

PG Guardian is organized into modular components.

Each directory has a dedicated responsibility, making the project easier to maintain and extend.

```
pg-guardian/
│
├── app/
│   ├── advisor/
│   ├── api/
│   ├── checks/
│   ├── collector/
│   ├── config/
│   ├── database/
│   ├── notification/
│   ├── report/
│   ├── scheduler/
│   └── utils/
│
├── docker/
├── docs/
├── scripts/
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Directory Description

### app/

Contains the main application source code.

---

### collector/

Collects operational metrics from PostgreSQL and the operating system.

Examples

- PostgreSQL statistics
- Replication status
- WAL information
- System metrics

---

### checks/

Evaluates collected metrics and determines database health.

Examples

- Replication check
- Backup check
- Vacuum check
- WAL check
- Connection check

---

### advisor/

Provides AI-assisted explanations and recommended actions.

---

### report/

Generates operational reports.

Supported formats

- HTML
- PDF
- JSON

---

### notification/

Sends alerts and reports.

Supported channels

- Email
- Slack
- Microsoft Teams

---

### scheduler/

Schedules periodic monitoring tasks.

Examples

- Every hour
- Daily health check
- Weekly report

---

### database/

Manages PostgreSQL database connections.

---

### api/

Provides REST API endpoints.

Future versions will use FastAPI.

---

### config/

Stores project configuration files.

Examples

- Database settings
- Notification settings
- AI settings

---

### utils/

Shared utility functions used across the project.

---

### docker/

Docker-related configuration.

---

### docs/

Project documentation.

---

### tests/

Unit and integration tests.

---

### scripts/

Utility scripts for development and deployment.
