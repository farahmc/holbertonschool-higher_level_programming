# 0x10. Python - Network #0

## Tasks

## Requirements
- You have to use `curl`

### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
- The size must be displayed in bytes

### 1. cURL to the end
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
- Display only body of a `200` status code response

### 2. cURL Method
Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response

### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
- A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`

### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
- A variable `email` must be sent with the value `test@gmail.com`
- A variable `subject` must be sent with the value `I will always be here for PLD`

## Advanced Tasks

### 6. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
- You are not allowed to use any pipe, redirection, etc.
- You are not allowed to use `;` and `&&`

### 7. cURL a JSON file
Write a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
- Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request

### 8. Catch me if you can!
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` that causes the server to respond with a message containing `You got me!`, in the body of the response.
- You are not allow to use `echo`, `cat`, etc. to display the final result
