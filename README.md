![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# ExpensePy


ExpensePy Tracker CLI is a command-line tool designed to help users efficiently manage and track their expenses with 10 different categories. With its user-friendly interface and powerful features, this tool allows individuals to record their daily expenditures, categorise expenses, set budget limits, and generate detailed expense reports. The Expense Tracker CLI is built on Python, utilising various libraries and modules to ensure seamless data handling and smooth user interactions. Whether you're a budget-conscious individual or a business owner looking to monitor expenses, this CLI tool provides a convenient and effective solution for keeping financial matters under control with reminders of your budget each time you enter an expense.

![Mockup of ExpensePy](/assets/screenshots/Captura%20de%20pantalla%20(662).png)

## Table of Contents

- [User Experience Design (UX)](#user-experience-design-ux)
- [The Strategy Plane](#the-strategy-plane)
  - [Site Goals](#site-goals)
  - [User Stories](#user-stories)
- [The Scope Plane](#the-scope-plane)
- [The Structure Plane](#the-structure-plane)
  - [Main Structure](#main-menu)
- [The Skeleton Plane](#the-skeleton-plane)
  - [Wireframes](#wireframes)
- [The Surface Plane](#the-surface-plane)
  - [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Technologies](#technologies)
- [Testing](#testing)
  - [Test Strategy](#test-strategy)
  - [Test Results](#test-results)
- [Deployment](#deployment)
  - [Project Creation](#project-creation)
  - [Software](#software)
  - [Media and Credits](#media-and-credits)
- [Thanks to](#thanks-to)

  
## User Experience Design (UX)
The Expense Tracker project aims to provide users with a straightforward and efficient way to manage their expenses and monitor their budget. The user experience is designed to be intuitive, with clear prompts and informative displays that guide users through the process of entering expenses and analyzing their spending habits. 

The project's codebase encapsulates these UX principles, offering a seamless experience for users to manage their finances effectively. The utilization of emojis, color-coded messages, and clear menus contributes to a user-friendly interface that encourages users to make informed financial decisions.

### The Strategy Plane
The project's UX strategy revolves around simplicity, clarity, and functionality:

Expense Input: Users can easily input their expenses by providing a name, amount, and selecting a category from a predefined list. This minimizes user effort while ensuring that all necessary information is captured.

Budget Awareness: The application promotes budget awareness by displaying the remaining budget for the month and the daily budget for the remaining days. These figures are presented in a way that users can quickly assess their spending status.

Category Summaries: Users can view summarized expenses by category, allowing them to identify areas where they are spending the most. The amounts are presented clearly, aiding quick comprehension.

Budget Feedback: Users receive immediate feedback based on their budget adherence. If they are staying within budget, a positive message is displayed in green. If they exceed their budget, a warning message is shown in red, emphasizing the need for adjustment.

Menu Navigation: The application employs a menu-driven approach for easy navigation. Users are presented with options to add expenses, view expense summaries, adjust their budget, or exit the tracker.

The project's codebase encapsulates these UX principles, offering a seamless experience for users to manage their finances effectively. The utilization of emojis, color-coded messages, and clear menus contributes to a user-friendly interface that encourages users to make informed financial decisions.

#### Site Goals
Site Goals:

1. Efficient Expense Tracking: The primary goal of the Expense Tracker CLI is to provide users with a streamlined and efficient way to track their expenses. Users should be able to easily record their expenditures, categorise them, and view a summary of their spending patterns.

2. Simplified Budget Management: The tool aims to simplify budget management for individuals and businesses alike. Users can set budget limits for different expense categories and receive notifications when they are nearing or exceeding these limits.

3. Customisable Categories: The Expense Tracker CLI offers the flexibility to create custom expense categories to align with users' specific financial needs and preferences. This allows for more accurate expense tracking and analysis.

4. Insightful Expense Reports: The tool generates detailed and insightful expense reports, providing users with a comprehensive overview of their spending habits over specific time periods. These reports can help users identify areas where they can cut back or optimise their expenses.

5. Cross-Platform Compatibility: The CLI is designed to be cross-platform compatible, allowing users to access and use the expense tracking tool on various operating systems and through Google Spreadsheets.

6. User-Friendly Interface: The CLI offers a user-friendly interface with clear instructions and intuitive commands, making it accessible to individuals with varying levels of technical expertise.


#### User Stories

User Stories for the Expense Tracker CLI:

1. As a user, I want the main purpose of the Expense Tracker CLI to be clear so that I immediately understand its intended functionality upon launching the application.

2. As a user, I want to navigate the Expense Tracker CLI effortlessly so that I can access different features and functionalities with ease. The CLI should provide clear and concise commands for adding expenses, viewing reports, and managing budget categories.

3. As a user, I want the Expense Tracker CLI to be responsive and adapt to different devices, including mobile phones, tablets, and desktop computers. This ensures that I can conveniently track my expenses regardless of the device I am using.

4. As a user, I want to view and filter expenses based on their category.

5. As a user, I want to be able to add a budget, and adjust it whenever I like, as well as wanting to see budget reminders when I add expenses to keep me on track.

6. As a user, I want the Expense Tracker CLI to provide a seamless navigation experience, allowing me to choose actions from the menu or exit the app without relying on browser buttons. 

## The Scope Plane

Features planned:

Scope Plane for the Expense Tracker CLI:

The Expense Tracker CLI aims to provide a comprehensive and user-friendly tool for individuals to track their expenses efficiently. The following features are planned for implementation:

1. Expense Management: Users can add, edit, and delete individual expense records. Each expense will include details such as the date, amount, category and description.

3. Budget Categories: Users can set up custom budget categories to organise their expenses effectively. The CLI will allow users to add, edit, and delete budget categories as needed.

4. Expense Reports: Generate detailed reports that provide insights into spending patterns, including summaries based on categories, time periods, and total expenses.

5. Filtering and Searching: Implement the ability to filter and search expenses based on specific criteria, such as date range, category, or keyword. This functionality will help users find relevant transactions quickly.

6. User-Friendly Interface: Design an intuitive and user-friendly command-line interface that makes it easy for users to interact with the expense tracker efficiently.

7. Data Persistence: Utilise file to save and retrieve user expense data, ensuring that the information is available across multiple sessions.

8. Budget Alerts: Optionally, provide users with budget alerts or notifications when their spending approaches or exceeds predefined limits.


## The Structure Plane
User Experience and Navigation
Title Display:

Upon launching the CLI, display a colored title: "ExpensePy - The Best Expense Tracker App."
### Main Menu:

After the title, present the main menu options:
"1. Add Expense 💸💰"
"2. View Expenses 👀📜"
"3. Adjust Budget 📊✏️"
"4. Exit Tracker 👋"
Navigation Loop:

Use a loop to continuously prompt the user for their choice until they choose to exit.
Adding Expense
Get Expense Details:

When the user selects "1" from the main menu, prompt for:
Expense name
Expense amount (with validation for positive numbers)
Select Expense Category:

Display the list of expense categories.
Prompt the user to select a category by entering a number within the valid range (1-10).
Expense Object Creation:

Create an Expense object with the provided name, validated amount, and selected category.
Save the expense to the CSV file.
Viewing Expenses
Display Expenses by Category:

When the user selects "2" from the main menu, read and parse the CSV file.
Group expenses by category and calculate the total amount spent in each category.
Calculate Total Spent:

Calculate the total amount spent across all categories.
Remaining Budget and Budget Per Day:

Calculate the remaining budget based on the initial budget and total spent.
Calculate the budget per day based on the remaining budget and days left in the month.
Display Results:

Display the grouped expenses with category totals.
Show the total spent this month.
Display remaining budget, budget per day, and corresponding color-coded messages based on budget status.
Adjusting Budget
Prompt for New Budget:

When the user selects "3" from the main menu, prompt for a new budget amount.
Validation and Update:

Use try-except to handle invalid input for the new budget (positive numbers only).
If the input is valid, update the global budget variable.
Exiting the App
Exiting Prompt:

When the user selects "4" from the main menu, display a goodbye message and exit the app.
Prompt Continue:

After each action, prompt the user if they want to perform another action (y/n).
If yes, display the main menu; if no, exit the app.

## The Skeleton Plane

ExpensePy the Best Expense Tracker App


**         MAIN MENU          **
********************************
1. First option is for the user to add expense(user experience simple, quick and efficient)

E.g Running Expense Tracker!
    Getting Users Expense#

**         SHOW EXPENSE       **
********************************
2. They will be prompted to give the expense a name, amount and  category

E.g Enter expense name: food
    Enter expense amount: 343
    You've entered food, 343.0

**         BUDGET         **
********************************
3. Remaining budget for the month will appear, with different coloured prompts, depending on whether or not user is sticking to budget.

E.g Remaining days in the current month: 23
    Budget per day: 💲50.30
    You have 💲1157.00 remaining this month! 📅
    Your spending is on track. Keep it up! 💪


**         MAIN MENU          **
********************************
4. User will be prompted to add another action or exit tracker with either a y or n value.

E.g Expense Tracker Menu:
    1. Add Expense 💸💰
    2. View Expenses 👀📜
    3. Adjust Budget 📊✏️
    4. Exit Tracker 👋
    Enter your choice (1/2/3/4): 

  5. The menu will keep appearing until the user decides to exit the app.


## The Surface Plane
The "Surface Plane" involves the design and user interface aspects of your Expense Tracker CLI.

### Design
I utilised color formatting with the colorama library for visually appealing outputs.
Provide clear and informative prompts, messages, and error handling.
Implement loops for repeated interactions and user-friendliness.
Maintain a simple and intuitive user experience.

### Colour Scheme
The color scheme incorporates colorama's color formatting to enhance the user experience. For example:
Title and important information: Blue
Positive messages: Green
Warning and budget alerts: Red and yellow
Emojis for added user experience

### Typography
Font choices are not applicable in a text-based CLI application.


## Features
### Existing Features
- User-friendly CLI interface
- Expense entry with amount, category, and name
- Budget tracking with remaining budget and daily budget calculation
- Expense summary by category
- Data persistence with CSV file storage


### Future Features

- User sign-up functionality.
- Sign in / Sign out functionality.
- Profile page showing basic user information and events created by the user with modification ability.
- Site-wide footer containing contact information, Copyright info, and Site Links.
- Currency Support so Expense Tracker CLI supports different currencies to accommodate users from various regions.
- Data Visualisation to incorporate data visualisation options to present expense data graphically, offering users a visual representation of their financial data.

## Technologies

- Python
- pip for installing Python packages.
- Heroku
- GitHub

## Testing

### Test Strategy
1. Code Structure and Style Testing (PEP8):
I ran my code through a PEP8 linter to ensure it adhered to Python's style guidelines.
I corrected any formatting issues or violations reported by the linter.

2. Functionality Testing with Print Statements:
I inserted print statements at key points in my code to confirm the execution flow.
For example, I added print statements at the beginning of each function to ensure they were being called.
I ran the app and verified that the print statements showed up at the expected points.

3.User Testing (Creator as User):
I pretended I was a user and went through various scenarios to test the app's functionality.
I added expenses, viewed expenses by category, adjusted the budget, and exited the app.
I tested with both valid and invalid inputs to ensure the app handled them gracefully.

4. End-to-End Testing:
I created test cases that simulated the entire user journey from start to finish.
This included scenarios like adding expenses, viewing expenses, and adjusting the budget in one go.
I also inputted symbols, letters and numbers to test user input validation, ensuring that it will be handled appropriately, for example, an error message when a symbol is entered for an amount float value.

E.g Enter expense amount: ///
    Please enter valid numbers for the expense amount.
    Enter expense amount: 

5. Budget Adjustment Testing:
I tested the budget adjustment functionality.
I checked that the budget was updated correctly and that I received appropriate feedback.

E.g Enter the new budget: 23232
    Budget adjusted to: 23232.00 💰📊

6. Error Handling Testing:
I intentionally input incorrect data (e.g., non-numeric values) to test the app's error handling.
I verified that the app displayed meaningful error messages and handled the errors gracefully.

E.g Invalid choice. Please choose a valid option (1/2/3/4)

7. Integration Testing:
I tested the interactions between different functions and components of the app.
I verified that data flowed correctly and the app behaved as expected.

8.Visual Testing (Lighthouse or Similar Tools):
I used tools like Lighthouse to evaluate web accessibility, performance, and best practices since I planned to deploy the app on a web platform.
I addressed any issues identified by the tool to enhance the app's overall quality.

9. User Experience Testing:
I ensured that the app's prompts and messages were clear and user-friendly.
I tested the navigation flow to ensure users could easily move between different features.

10. Manual Testing of Different Scenarios:
I tested various combinations of actions to identify any potential conflicts or unexpected behavior.
For example, I added expenses, adjusted the budget, viewed expenses, and exited the app in different orders.

11. Boundary Testing:
I tested the app with extreme inputs, such as very large or very small values for expenses and budget.
I verified that the app handled these inputs without crashing or producing incorrect results.

E.g You've spent 💲234234342343243904.00 this month!

12. Cross-Platform Testing:
I tested the app on different platforms (Windows, macOS, Linux) to ensure compatibility.
I verified that the app ran and behaved consistently on all platforms.

13. Documentation Review:
I reviewed my README and other documentation to ensure they accurately reflected the app's features and usage instructions.

### Test Results

![User Stories Testing](/assets/screenshots/Captura%20de%20pantalla%20(658).png)
![User Stories Testing](/assets/screenshots/Captura%20de%20pantalla%20(660).png)
![User Stories Testing](/assets/screenshots/Captura%20de%20pantalla%20(661).png)
![LightHouse Performance Test](/assets/screenshots/Captura%20de%20pantalla%20(651).png)

<details>
<summary>PEP8 Online Validation - run.py</summary>

![](/assets/screenshots/Captura%20de%20pantalla%20(647).png)

</details>

I've ensured that my code is error-free and all validation checks have been implemented, meeting the requirements for documenting logic planning, addressing validation errors, and performing manual code testing.

## Deployment
Heroku is a platform that allows you to deploy and host your applications, which is what I used for this expense tracker and these are the following steps I took:

1. I signed up for a Heroku account at https://www.heroku.com/.

2. I installed the Heroku Command Line Interface (CLI) on your system. This CLI tool lets you manage and deploy your Heroku apps from the command line.

3. I ensured your project is in a Git repository. 

4. A requirements.txt file and a Procfile was added from Code Institute's template so the project would deploy successfully.

5. I created a new Heroku app using the Heroku CLI after I logged into my account and made sure my Git repository was connected.

7. Before creating the app, I added two buildpacks from the Settings tab making sure to add heroku/python first, followed by heroku/nodejs.

8. I deployed my project to Heroku by pushing your Git repository to Heroku's remote, that will update with every git push, as chosen by me in the settings, successfully integrating and deploying my project for use through the Heroku URL.


### Project Creation

The Expense Tracker is a CLI-based budget management application written in Python. It allows users to track their expenses, categorize them, and monitor their budget for the month. Users can input the amount spent, the expense category, and a name for the expense, and the application will calculate the remaining budget for the month and the daily budget for the rest of the month.


## Software

- Text editor (Visual Studio Code + Code Anywhere)
- Heroku
- Version control system (Git)

## Media and Credits

The development of ExpensePy was made possible with the help of various resources and inspirations from different CLI projects using Python. The following sources were instrumental in the creation of this project:

- [Code Institute](https://codeinstitute.net/ie): For their videos and guidance, especially with Python.

- [Code Academy](https://www.codecademy.com/): For basic concepts on Python.

- [PythonTutor](https://pythontutor.com/visualize.html#mode=edit): CodePen provided inspiration and ideas for implementing certain features and design elements.

- [Python Geeks](https://pythongeeks.org/python-expense-tracker/): valuable insite to an expense tracker using python.

- NeuaralNine (YouTube channel): https://www.youtube.com/watch?v=tMLsR0_2yIE

- Various online forums and communities: Contributions and discussions from the web development community on platforms like Stack Overflow, Reddit, and GitHub provided valuable insights and solutions to specific challenges encountered during the development process.

## Thanks to
I would like to express my gratitude to Code Institute and my mentor for their exceptional web development curriculum and to my mentor for their invaluable guidance and support throughout this project. Thank you for providing the resources and expertise that have helped me grow as a developer.