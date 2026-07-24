# Architecture

## 1. System Overview

PG Guardian is a PostgreSQL operations assistant designed to help DBAs monitor database health, analyze operational metrics, and provide AI-assisted diagnostics.

The system follows a modular architecture where each component has a clearly defined responsibility. This allows new features to be added without affecting existing modules.

---

## 2. System Architecture

```
                PostgreSQL
                     │
                     ▼
          Metrics Collector
                     │
                     ▼
         Health Engine
              │
      ┌───────┴────────┐
      ▼                ▼
 Rule Engine      AI Advisor
      │                │
      └───────┬────────┘
              ▼
      Report Generator
              │
              ▼
   Notification Service

         Scheduler
     (Runs the pipeline)
```

---

## 3. Components

### Metrics Collector

Collects operational metrics from PostgreSQL.

Examples

- pg_stat_activity
- pg_stat_database
- pg_stat_replication
- pg_settings
- pg_stat_wal

---

### Health Assessment

Evaluates collected metrics and determines the current health status of the database.

Examples

- Replication Delay
- Dead Tuples
- Connection Usage
- WAL Generation
- Checkpoint Frequency

---

### Rule Engine

Applies predefined operational rules to determine whether the collected metrics are Normal, Warning, or Critical.

---

### AI Advisor

Provides explanations, possible causes, and recommended DBA actions based on the health assessment.

---

### Report Generator

Generates operational reports.

Supported formats

- HTML
- PDF
- JSON

---

### Notification Service

Sends reports and alerts to administrators.

Supported channels

- Email
- Slack
- Microsoft Teams

---

### Scheduler

Executes the monitoring pipeline at scheduled intervals.

Examples

- Every hour
- Every day
- Custom schedule

---

## 4. Data Flow

The monitoring process follows these steps.

1. Collect PostgreSQL metrics.
2. Evaluate database health.
3. Apply operational rules.
4. Generate AI recommendations if needed.
5. Create reports.
6. Send notifications.

---

## 5. Future Architecture

Planned features

- Backup Verification
- HA Monitoring
- WAL Analysis
- EXPLAIN Analyzer
- Parameter Advisor
- Capacity Forecast
- Index Advisor
- PostgreSQL Log Analyzer
