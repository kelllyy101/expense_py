![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# ExpensePy


ExpensePy Tracker CLI is a command-line tool designed to help users efficiently manage and track their expenses with 10 different categories. With its user-friendly interface and powerful features, this tool allows individuals to record their daily expenditures, categorise expenses, set budget limits, and generate detailed expense reports. The Expense Tracker CLI is built on Python, utilising various libraries and modules to ensure seamless data handling and smooth user interactions. Whether you're a budget-conscious individual or a business owner looking to monitor expenses, this CLI tool provides a convenient and effective solution for keeping financial matters under control with reminders of your budget each time you enter an expense.

![Mockup](/path/to/mockup.png) _(Add mockup)_

## Table of Contents

- [User Experience Design (UX)](#user-experience-design-ux)
- [The Strategy Plane](#the-strategy-plane)
  - [Site Goals](#site-goals)
  - [User Stories](#user-stories)
- [The Scope Plane](#the-scope-plane)
- [The Structure Plane](#the-structure-plane)
- [The Skeleton Plane](#the-skeleton-plane)
  - [Wireframes](#wireframes)
- [Database Design](#database-design)
- [Security](#security)
- [The Surface Plane](#the-surface-plane)
  - [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Differences to Design](#differences-to-design)
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

_(Include information about the overall testing strategy for the website)_

### Test Results

![User Stories Testing](/assets/screenshots/Captura%20de%20pantalla%20(658).png)
![User Stories Testing](/assets/screenshots/Captura%20de%20pantalla%20(660).png)
![User Stories Testing](/assets/screenshots/Captura%20de%20pantalla%20(661).png)
![LightHouse Performance Test](/assets/screenshots/Captura%20de%20pantalla%20(651).png)

<details>
<summary>PEP8 Online Validation - run.py</summary>

![](/assets/screenshots/Captura%20de%20pantalla%20(647).png)

</details>

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