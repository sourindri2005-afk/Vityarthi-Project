# Vityarthi-Project
This project is a Humanized Console-Based Inventory Management System designed for a small Clothes Store. This Python program is like a digital notebook or assistant for a clothes store manager. It runs right in your computer's terminal (the text window) and helps you keep track of all the items on your shelves.
1. Project Title
Humanized Clothes Store Inventory Manager (CLI)

2. Overview of the Project
This project is a simple command-line interface (CLI) application built in Python to manage the inventory of a small clothes retail store. It utilizes a Python dictionary as a temporary, in-memory database to store item details (ID, name, price, stock). The system provides a user-friendly, menu-driven interface, allowing the retail manager to perform core inventory operations quickly and efficiently.

The term "Humanized" refers to the conversational and informative outputs, such as providing a status like "Plenty in stock!" or "Running low!" instead of just a raw number.

3. Key Features
The system provides a full suite of basic retail inventory operations, structured around a simple menu:

* Item Creation and Maintenance (CRUD):

  Add a NEW item (Option 1): Allows entry of a unique ID, name, price, and initial stock.

  UPDATE the stock level (Option 4): Manages inventory changes by increasing stock (for deliveries) or safely decreasing stock (for sales), with validation to prevent stock from going   below zero.

  REMOVE an item (Option 5): Permanently deletes a specific product entry by its ID.

* Information and Reporting:

  Check AVAILABILITY (Option 2): Provides status updates based on stock levels (e.g., "Plenty in stock," "Running low," or "SOLD OUT").

  Check PRICE (Option 3): Retrieves and displays the price for a specified Item ID.

  VIEW all items (Option 6): Displays a neatly formatted table summarizing all products currently in the inventory.

* Safety and Usability:

  Input Validation: Uses try-except blocks to handle non-numeric or inappropriate input gracefully, preventing program crashes.

  CLEAR the entire inventory (Option 7): A high-risk operation requiring explicit text confirmation ('YES') to proceed.

* EXIT the system (Option 0): Terminates the program cleanly.

4. Technologies/Tools Used
Category	Component	Description
Language	Python 3	The core programming language used for the entire application logic.
Data Structure	Dictionary (In-Memory)	Used as the temporary database (Inventory) to store product records.
Standard Library	datetime	Used to capture and display the time the inventory was last checked.
Interface	Command Line Interface (CLI)	The primary user interface, relying on the built-in input() and print() functions.

5.Installation and Execution
Since the project uses only the standard Python library, setup is minimal.

Steps to Install and Run
Prerequisite: Ensure Python 3 is installed on your operating system.

Save: Save the complete Python code into a file named, for example, inventory_system.py.

Execute: Open your terminal or command prompt, navigate to the file's location, and run the command:

python inventory_system.py
Use the Menu: The system will start, display the welcome message and the main menu, and prompt you to enter a choice (0-7).

Instructions for Testing
To confirm the functionality of all menu options, test the following scenarios:
Functionality Tests:
Test Option 1 (Add) by adding a new item (e.g., ID 104, 'New Dress', $120.00, 40 stock).
Test Option 4 (Update) by increasing stock for an existing item (delivery) and decreasing stock (sale).Test Option 2 (Check Availability) to confirm all three statuses: "Plenty" (stock > 10), "Low" (stock $\leq 10$ but > 0), and "SOLD OUT" (stock 0).
Test Option 6 (View All) to verify that all items, including the newly added and updated ones, appear correctly in the formatted table.
Test Option 5 (Remove) to successfully delete the item created in the first step.
Guardrail Tests:
Test the main menu input by entering a letter or an invalid number (e.g., 9) to check the error handling.
Test Option 4 (Update) sale reduction to ensure the system prevents stock from dropping below zero (e.g., trying to sell 50 items when only 40 are available).
Test Option 7 (Clear Inventory) first by typing an incorrect confirmation (e.g., 'no') and then by typing the exact confirmation ('YES') to verify the safety mechanism.Exit Test:Test Option 0 to confirm the application shuts down cleanly.

Screenshots:

<img width="362" height="224" alt="Screenshot 2025-11-25 at 12 32 15 AM" src="https://github.com/user-attachments/assets/cf48cad8-d177-4006-8bfb-94319a4d5e92" />

<img width="362" height="224" alt="Screenshot 2025-11-25 at 12 41 52 AM" src="https://github.com/user-attachments/assets/06d0c8a7-5485-46b6-a82e-f240f1c2e276" />

<img width="362" height="224" alt="Screenshot 2025-11-25 at 12 43 49 AM" src="https://github.com/user-attachments/assets/449085b2-487d-4444-83a7-be8ec676f45e" />


<img width="369" height="283" alt="Screenshot 2025-11-25 at 12 53 04 AM" src="https://github.com/user-attachments/assets/8a016b61-9d97-4395-b840-2ebdc93cb6da" />


<img width="451" height="254" alt="Screenshot 2025-11-25 at 12 46 00 AM"
src="https://github.com/user-attachments/assets/6c62cd30-2e40-4197-b39f-e4a48ed7a9eb" />

<img width="498" height="275" alt="Screenshot 2025-11-25 at 12 49 35 AM" src="https://github.com/user-attachments/assets/209f3e65-29d7-4428-8990-9982e1831bb9" />

<img width="369" height="235" alt="Screenshot 2025-11-25 at 12 50 05 AM" src="https://github.com/user-attachments/assets/490d2be5-d84d-41c9-8b14-0c2e8efdcd90" />


<img width="369" height="215" alt="Screenshot 2025-11-25 at 12 50 28 AM" src="https://github.com/user-attachments/assets/746b2ea0-4653-4937-8f6c-433dd9394147" />
