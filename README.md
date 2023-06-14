# AirBnB Clone - Command Interpreter
## Project Description

This project aims to build an AirBnB clone web application by developing a command interpreter using Python. The command interpreter serves as a management system for AirBnB objects, allowing users to create, update, delete, and retrieve data related to various entities such as users, states, cities, places, and more. The project encompasses several tasks, including implementing a parent class for initialization and serialization, creating a serialization flow, defining classes for AirBnB entities, building a file storage engine, and validating classes and storage engine with unittests.

## Command Interpreter

The command interpreter is a command-line interface that provides interaction with the AirBnB clone and enables users to manage the objects within the application.

To start the command interpreter, follow these steps:

    Clone the project repository from GitHub.
    Ensure that Python 3 is installed on your system.
    Open a terminal and navigate to the project directory.
    Run the command ./console.py to launch the command interpreter.

## How to Use the Command Interpreter

Once the command interpreter is running, you can use the following commands to interact with the AirBnB objects:

    create: Create a new instance of an object.
    show: Display detailed information about a specific object.
    destroy: Delete an object from the system.
    all: Retrieve all objects or all objects of a specific class.
    update: Update the attributes of an object.
    help: Show available commands or describe specific command functionality.
    quit: Exit the command interpreter.

To execute a command, simply type the command followed by the necessary arguments or options and press Enter.
## Examples

Here are some examples to demonstrate the usage of the command interpreter:

    Creating a new user: 'create <class_name>'


(hbnb) create User

Output: bf452b8c-35b3-4b2e-a15f-3092d8e4ef15

    Showing information about a place: 'show <class_name> <instance_id>'


(hbnb) show Place bf452b8c-35b3-4b2e-a15f-3092d8e4ef15

Output:


[Place] (bf452b8c-35b3-4b2e-a15f-3092d8e4ef15) {
    created_at: 2023-06-08 10:30:00,
    updated_at: 2023-06-08 10:30:00,
    id: bf452b8c-35b3-4b2e-a15f-3092d8e4ef15,
    ...
}

    Updating the name of a city: 'update <class_name> <instance_id> <variable_name> "<variable_value>"'


(hbnb) update City bf452b8c-35b3-4b2e-a15f-3092d8e4ef15 name "New City Name"

Output: (No output)

    Listing all objects: 'all'


(hbnb) all

Output:

["[BaseModel] (0eb4d19f-e54e-40fc-9ed8-74a72c468f54) {'id': '0eb4d19f-e54e-40fc-9ed8-74a72c468f54', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 13, 445268), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 13, 445283)}", "[User] (92c8391f-1a16-4f7a-9818-e94cafa23c2b) {'id': '92c8391f-1a16-4f7a-9818-e94cafa23c2b', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 16, 139695), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 16, 139715)}", "[City] (59872cd1-0692-40a2-8bd8-65184643a1fd) {'id': '59872cd1-0692-40a2-8bd8-65184643a1fd', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 18, 575985), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 18, 575999)}", "[Place] (ae50374c-3e75-4e7d-b120-13711cca53a8) {'id': 'ae50374c-3e75-4e7d-b120-13711cca53a8', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 21, 143996), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 21, 144011)}", "[State] (92a677f3-fd9f-4993-9f9b-823f490bff13) {'id': '92a677f3-fd9f-4993-9f9b-823f490bff13', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 24, 369156), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 24, 369170)}", "[Amenity] (8f7ab8c0-bff4-4dc1-b59a-81907ca7fe4a) {'id': '8f7ab8c0-bff4-4dc1-b59a-81907ca7fe4a', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 27, 317225), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 27, 317242)}"]

    Listing all objects of a class: 'all <class_name>'

(hbnb) all User

Output:

["[User] (92c8391f-1a16-4f7a-9818-e94cafa23c2b) {'id': '92c8391f-1a16-4f7a-9818-e94cafa23c2b', 'created_at': datetime.datetime(2023, 6, 13, 18, 51, 16, 139695), 'updated_at': datetime.datetime(2023, 6, 13, 18, 51, 16, 139715)}", "[User] (16b4c285-50a2-4f76-829c-ef608b172f0d) {'id': '16b4c285-50a2-4f76-829c-ef608b172f0d', 'created_at': datetime.datetime(2023, 6, 13, 18, 52, 46, 727189), 'updated_at': datetime.datetime(2023, 6, 13, 18, 52, 46, 727201)}", "[User] (3fb22a23-61ae-466d-8a1d-680ba1559e0f) {'id': '3fb22a23-61ae-466d-8a1d-680ba1559e0f', 'created_at': datetime.datetime(2023, 6, 13, 18, 52, 49, 56112), 'updated_at': datetime.datetime(2023, 6, 13, 18, 52, 49, 56132)}", "[User] (812d1dd1-36c3-40fb-bf70-ea11473e4b79) {'id': '812d1dd1-36c3-40fb-bf70-ea11473e4b79', 'created_at': datetime.datetime(2023, 6, 13, 18, 52, 51, 260066), 'updated_at': datetime.datetime(2023, 6, 13, 18, 52, 51, 260079)}"]
