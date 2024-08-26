# Task Management API

## Project Overview

This Task Management API is a RESTful API I developed using Flask, it was a guided activity I did to better learn the Flask framework. It allows users to manage tasks through various HTTP methods. Users can perform operations such as retrieving tasks, adding new tasks, updating tasks, and deleting tasks. This API is intended to provide a simple interface for managing task data with operations supported by GET, POST, PATCH, and DELETE methods.

## Installation and Setup

### Prerequisites

- Python 3.x installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).
- Flask installed. You can install it using pip:

  ```bash
  pip install Flask


## Usage

1. Retrieve All Tasks (GET):
   Endpoint:
   ```bash
   GET /tasks
   
   -This returns a list of all tasks.


2. Retrieve a Specific Task (GET):
   Endpoint:
   ```bash
   GET /tasks/<task_id>
   
   -Returns details of a specific task identified by task_id


3. Add a New Task (POST):
   Endpoint:
   
   POST /tasks

   Body:
   {
  "title": "Task Title",
  "description": "Task Description"
   }

   -Adds a new task with the provided title and description. Returns the created task.


4. Update a Task (PATCH):
   Endpoint:
   
   PATCH /tasks/<task_id>
   
   Body:
   {
  "title": "Updated Task Title",
  "description": "Updated Task Description",
  "done": true
   }

   -Updates the specified task with the given data. Only fields provided in the request will be updated.


5. Delete a Task (DELETE):
   Endpoint:
   ```bash
   DELETE /tasks/<task_id>

   -Deletes the task identified by task_id.


## Documentation

This project uses Markdown for documentation. Markdown is a lightweight markup language that is easy to write and read. The README.md file serves as the main documentation, providing an overview of the project, instructions for installation and usage, and additional resources.

### Additional Resources:
https://www.markdownguide.org/
https://flask.palletsprojects.com/en/3.0.x/


## Contact and Collaboration

If you have any questions, suggestions, or would like to collaborate, feel free to contact me:

Email: Matthewsnow35@gmail.com
GitHub: Matthewsnow35

I welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request with your changes.
