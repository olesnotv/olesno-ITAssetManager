# PROJECT 01 - IT Asset Manager
*README made by ChatGPT*
## Scenario
Novatech Solutions is a small IT company with 35 employees. The company owns various IT assets, including desktop computers, laptops, monitors, printers and smartphones.

Currently, information about these assets is stored in multiple Excel spreadsheets. As the company grows, managing this inventory becomes increasingly difficult. The IT department struggles to locate equipment, identify its current owner and determine which devices are available for use.

Your role is to develop a small inventory management application that centralizes all IT asset information and simplifies the daily work of the IT department.

Your application must run directly in a terminal and allow IT staff to manage the company's equipment without relying on external databases or complex infrastructure.

## Technical environment
The application must be developed using Python 3. Data will be stored locally in JSON files, allowing information to persist between application sessions.

The program must be compatible with both Windows and Linux. External Python libraries are not required, although you may use standard Python modules such as json, os, datetime and uuid.

The application must have a command-line interface (CLI), with a clear menu allowing users to interact with its different functionalities.

## Functional requirement
The first requirement is to implement an asset registration system. IT staff must be able to add new equipment to the inventory by entering its unique identifier, name, category, brand, model, serial number, purchase date and current status.

Once equipment has been registered, users must be able to display the entire inventory in a readable format. They must also be able to search for specific equipment using either its asset ID or its serial number.

The application must provide an editing feature so that existing asset information can be updated. Similarly, users must be able to delete equipment from the inventory, provided they confirm the operation beforehand.

Another important requirement concerns equipment assignments. IT staff must be able to associate an asset with an employee using their employee ID. The application must keep track of whether equipment is available or currently assigned.

Finally, the application must include a statistics feature. It should display the total number of registered assets, their distribution by category and the number of available and assigned devices.

## Business constraints 
The company has established several rules that must be respected throughout the development process.

Every asset must have a unique identifier, and no two assets may share the same serial number. Equipment that is already assigned to an employee cannot be assigned to another employee until it has been made available again.

When an asset is deleted, it must disappear from the inventory and must no longer be accessible through the application's search functionality.

The application must also handle incorrect user input gracefully. Invalid information, unexpected input or missing data must never cause the program to crash.

All inventory information must be saved automatically so that closing and restarting the application does not result in data loss.

## Developement requirements
The source code must be organized into several Python files, with a clear separation between the application's main interface, inventory management and data storage.

You are expected to use functions to structure your code, dictionaries and lists to manipulate information, and exception handling to manage potential errors.

The application must remain simple and understandable. Avoid unnecessary complexity and prioritize readable, maintainable code.

No graphical interface or external database should be implemented for this first version.
