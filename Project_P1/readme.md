# IT Service Desk Management System

A Flask-based IT Service Desk Management System for managing support tickets, assignments, SLA tracking, comments, attachments, feedback, and role-based access control.

## Features

- User registration and login
- Role-based access control
- Employee, Support Agent, and Admin roles
- Ticket creation and management
- Ticket assignment
- Ticket status workflow
- Ticket comments
- File attachments
- SLA rules and SLA breach tracking
- Feedback and ticket ratings
- User activation and deactivation
- Ticket history and audit tracking
- Pagination and filtering
- REST APIs
- JWT authentication for APIs
- Global API error handling

## User Roles

### Employee

Employees can:

- Create tickets
- View their own tickets
- View ticket details
- Add comments
- Upload attachments
- Submit feedback

### Support Agent

Support Agents can:

- View assigned tickets
- Update ticket status
- Add comments
- Upload attachments
- View SLA information

### Admin

Admins can:

- View all tickets
- Create Support Agents
- Assign tickets
- Manage users
- Activate or deactivate users
- View SLA breaches
- View reports
- Filter and paginate tickets

## Ticket Workflow

```text
Open
  ↓
Assigned
  ↓
In Progress
  ↓
Resolved
  ↓
Closed