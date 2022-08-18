# 0x11. Python - Network #1

## Tasks

## Requirements
- You don’t need to error check arguments passed to the script (number or type)
Tasks 0 - 3 :
- You must use a `with` statement
- You must use the package `urllib` and `sys`
- You are not allowed to import any packages other than `urllib` and `sys`
Tasks 4 - 9:
- You must use the packages `requests` and `sys`
- You are not allow to import other packages than `requests` and `sys`

### 0. What's my status? #0
Write a Python script that fetches https://intranet.hbtn.io/status

### 1. Response header value #0
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
- The value of this variable is different for each request

### 2. POST an email #0
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)
- The email must be sent in the `email` variable

### 3. Error code #0
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).
- You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` followed by the HTTP status code

### 4. What's my status? #1
Write a Python script that fetches `https://intranet.hbtn.io/status`

### 5. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
- The value of this variable is different for each request

### 6. POST an email #1
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
- The email must be sent in the variable `email`

### 7. Error code #1
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.
- If the HTTP status code is greater than or equal to 400, print: `Error code:` followed by the value of the HTTP status code

### 8. Search API
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
- The letter must be sent in the variable `q`
- If no argument is given, set `q=""`
- If the response body is properly JSON formatted and not empty, display the `id` and `name` like this: `[<id>] <name>`
- Otherwise:
  - Display `Not a valid JSON` if the JSON is invalid
  - Display `No result` if the JSON is empty

### 9. My GitHub!
Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your `id`
- You must use Basic Authentication with a personal access token as password to access to your information (only `read:user` permission is needed)
- The first argument will be your `username`
- The second argument will be your `password` (in your case, a personal access token as password)
