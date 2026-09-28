# API Inspector – Web API Analysis Tool

## 1. Project Overview

**API Inspector** is a simple web-based tool developed using **Python, Flask, JavaScript, HTML, and CSS**.

The application allows users to send HTTP requests to an API and analyze the response. Users can enter an API URL, select an HTTP method, provide a JSON payload, and view the API response.

The project is designed to understand and demonstrate **client-server communication, HTTP methods, JSON payloads, API requests, and API responses**.

---

## 2. Objectives

The main objectives of this project are:

* To understand how REST APIs work.
* To understand client-server communication.
* To send GET and POST requests.
* To work with JSON request and response data.
* To analyze HTTP status codes.
* To display response headers and response time.
* To understand API workflows using Chrome DevTools.
* To provide a simple interface for API testing.

---

## 3. Technologies Used

| Technology      | Purpose                        |
| --------------- | ------------------------------ |
| Python          | Backend programming            |
| Flask           | Web framework                  |
| JavaScript      | Frontend and API communication |
| HTML            | Web page structure             |
| CSS             | User interface                 |
| Requests        | Sending HTTP requests          |
| JSON            | Data exchange format           |
| Chrome DevTools | Network analysis               |
| Git/GitHub      | Version control                |

---

# 4. Project Structure

```text
api-inspector/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── utils/
    ├── __init__.py
    └── api_client.py
```

### File Description

**app.py**

Main Flask application. It receives requests from the frontend and communicates with the API client.

**api_client.py**

Contains the Python logic for sending HTTP requests and processing API responses.

**index.html**

Provides the user interface.

**script.js**

Sends the user's input from the webpage to the Flask backend and displays the result.

**style.css**

Controls the appearance of the dashboard.

**requirements.txt**

Contains the Python packages required to run the project.

---

# 5. How the Application Works

The application follows this workflow:

```text
User
  |
  | API URL + Method + JSON Payload
  ↓
JavaScript Frontend
  |
  | HTTP Request
  ↓
Flask Backend
  |
  | Python Requests Library
  ↓
API Server
  |
  | HTTP Response
  ↓
Flask Backend
  |
  ↓
JavaScript Frontend
  |
  ↓
Result Dashboard
```

---

# 6. Installation Manual

## Step 1 – Install Python

Make sure Python is installed.

Check using:

```bash
python --version
```

Example:

```text
Python 3.12.x
```

---

## Step 2 – Open the Project Folder

Open Git Bash or Command Prompt inside the project folder.

Example:

```bash
cd path/to/api-inspector
```

---

## Step 3 – Install Required Packages

Run:

```bash
pip install -r requirements.txt
```

The required packages are:

```text
Flask
requests
```

---

# 7. Running the Application

Run:

```bash
python app.py
```

The Flask server will start.

You should see:

```text
Running on http://127.0.0.1:5000
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

# 8. How to Use the Application

## Step 1 – Enter API URL

Enter the API endpoint in the URL field.

For testing, you can use:

```text
https://httpbin.org/post
```

---

## Step 2 – Select HTTP Method

Select:

```text
POST
```

---

## Step 3 – Enter JSON Payload

Enter valid JSON.

Example:

```json
{
    "name": "Rithanya",
    "age": 22,
    "course": "Software Engineering"
}
```

---

## Step 4 – Click Send Request

Click:

```text
Send Request
```

The application sends the request to the Flask backend.

---

# 9. Understanding the Result

The application displays information such as:

### Status Code

Example:

```text
200
```

This indicates that the request was successfully processed.

Common status codes:

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 500  | Internal Server Error |

---

### Response Time

Example:

```text
0.42 seconds
```

This represents approximately how long the API request took.

---

### Response Headers

The application displays HTTP response headers returned by the API server.

Example:

```text
Content-Type: application/json
Server: ...
```

---

### Response Body

The API response is displayed in JSON format when the server returns JSON.

Example:

```json
{
    "name": "Rithanya",
    "age": 22,
    "course": "Software Engineering"
}
```

---

# 10. GET Request Example

For a GET request, use an API such as:

```text
https://httpbin.org/get
```

Select:

```text
GET
```

No JSON payload is required.

Click:

```text
Send Request
```

The application will display the API response.

---

# 11. POST Request Example

Use:

```text
https://httpbin.org/post
```

Select:

```text
POST
```

Payload:

```json
{
    "name": "Rithanya",
    "age": 22,
    "department": "Computer Science"
}
```

Click:

```text
Send Request
```

The API returns information about the request.

---

# 12. Chrome DevTools Analysis

Chrome DevTools can be used to understand how the application communicates with the Flask backend.

### Steps

1. Open the application in Chrome.
2. Press `F12`.
3. Open the **Network** tab.
4. Click **Send Request**.
5. Find the request to:

```text
/api/test
```

6. Click the request.

You can inspect:

```text
Request URL
Request Method
Status Code
Request Headers
Request Payload
Response
Response Headers
```

This helps demonstrate the complete HTTP request/response cycle.

---

# 13. Example Request Flow

When the user sends a POST request:

```text
POST /api/test
```

The browser sends:

```json
{
    "url": "https://httpbin.org/post",
    "method": "POST",
    "payload": {
        "name": "Rithanya",
        "age": 22
    }
}
```

Flask receives this information.

The Python backend then sends:

```text
POST → https://httpbin.org/post
```

The API returns a response.

Flask sends the result back to the browser.

The dashboard displays the result.

---

# 14. Learning Outcomes

By completing this project, the developer learns:

* Client-server architecture
* HTTP request/response cycle
* GET and POST methods
* REST API concepts
* JSON data handling
* HTTP status codes
* Request and response headers
* Flask routing
* JavaScript Fetch API
* Python Requests library
* Chrome DevTools Network analysis
* Git and GitHub

---

# 15. Future Enhancements

The project can be extended with:

* PUT and DELETE methods
* Request history
* API response time graphs
* Authentication support for authorized APIs
* Header input section
* JSON formatting and validation
* Export API results
* API collections
* Automated API testing
* Response comparison

---

# 16. Limitations

The current version is intentionally simple and supports basic API testing.

It does not attempt to bypass authentication, access private endpoints, or circumvent security controls.

Testing should be performed only on APIs that are publicly available for testing or systems for which the user has authorization.

---

# 17. GitHub Commands

Initialize the repository:

```bash
git init
```

Add files:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Initial API Inspector project"
```

Connect the GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Rename the branch:

```bash
git branch -M main
```

Push the project:

```bash
git push -u origin main
```

For future changes:

```bash
git add .
git commit -m "Updated API analysis features"
git push
```

---

# 18. Project Summary

**API Inspector** is a beginner-friendly API analysis tool that demonstrates how a web application communicates with backend services through HTTP.

The project combines:

```text
Python
   +
Flask
   +
JavaScript
   +
REST APIs
   +
JSON
   +
Chrome DevTools
   +
GitHub
```

It provides practical experience with the fundamental web technologies required for API development, testing, and workflow analysis.
