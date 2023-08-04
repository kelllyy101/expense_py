![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# ExpensePy


ExpensePy Tracker CLI is a command-line tool designed to help users efficiently manage and track their expenses with 10 differen categories. With its user-friendly interface and powerful features, this tool allows individuals to record their daily expenditures, categorise expenses, set budget limits, and generate detailed expense reports. The Expense Tracker CLI is built on Python, utilising various libraries and modules to ensure seamless data handling and smooth user interactions. Whether you're a budget-conscious individual or a business owner looking to monitor expenses, this CLI tool provides a convenient and effective solution for keeping financial matters under control with reminders of your budget each time you enter an expense.

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
  - [GitHub Pages](#github-pages)
  
## User Experience Design (UX)

### The Strategy Plane

#### Site Goals
Site Goals:

1. Efficient Expense Tracking: The primary goal of the Expense Tracker CLI is to provide users with a streamlined and efficient way to track their expenses. Users should be able to easily record their expenditures, categorise them, and view a summary of their spending patterns.

2. Simplified Budget Management: The tool aims to simplify budget management for individuals and businesses alike. Users can set budget limits for different expense categories and receive notifications when they are nearing or exceeding these limits.

3. Customisable Categories: The Expense Tracker CLI offers the flexibility to create custom expense categories to align with users' specific financial needs and preferences. This allows for more accurate expense tracking and analysis.

4. Insightful Expense Reports: The tool generates detailed and insightful expense reports, providing users with a comprehensive overview of their spending habits over specific time periods. These reports can help users identify areas where they can cut back or optimise their expenses.

5. Data Security and Privacy: Ensuring the security and privacy of users' financial data is a top priority. The Expense Tracker CLI implements robust data encryption and protection measures to safeguard sensitive information.

6. Cross-Platform Compatibility: The CLI is designed to be cross-platform compatible, allowing users to access and use the expense tracking tool on various operating systems and through Google Spreadsheets.

7. User-Friendly Interface: The CLI offers a user-friendly interface with clear instructions and intuitive commands, making it accessible to individuals with varying levels of technical expertise.

8. Offline Accessibility: The Expense Tracker CLI allows users to manage their expenses even in offline mode. Data synchronisation and updates can occur once the user regains an internet connection.

9. Open-Source and Extensible: The tool is developed as an open-source project, encouraging contributions from the community and enabling users to extend its functionality to suit their unique needs.

10. Continuous Improvement: The Expense Tracker CLI strives for continuous improvement based on user feedback and evolving financial requirements. Regular updates and enhancements ensure that the tool remains relevant and effective.

#### User Stories

User Stories for the Expense Tracker CLI:

1. As a user, I want the main purpose of the Expense Tracker CLI to be clear so that I immediately understand its intended functionality upon launching the application.

2. As a user, I want to navigate the Expense Tracker CLI effortlessly so that I can access different features and functionalities with ease. The CLI should provide clear and concise commands for adding expenses, viewing reports, and managing budget categories.

3. As a user, I want the Expense Tracker CLI to be responsive and adapt to different devices, including mobile phones, tablets, and desktop computers. This ensures that I can conveniently track my expenses regardless of the device I am using.

4. As a user, I want to be able to register an account with the Expense Tracker CLI so that I can personalise my expense tracking experience. Having an account would enable me to store and access my expense data securely.

5. As a user, I want to search and filter expenses based on custom criteria to find specific transactions quickly. The CLI should support filtering by date, category, amount range, and other relevant parameters.

6. As a user, I want a way to contact the developer or support team behind the Expense Tracker CLI to get my questions or concerns addressed promptly. Having a support channel within the application ensures that I can seek assistance when needed.

7. As a user, I want the Expense Tracker CLI to provide a seamless navigation experience, allowing me to return to the main menu or home screen without relying on browser buttons. This ensures a smooth user experience and prevents unnecessary disruptions while using the tool.

## The Scope Plane

Features planned:

Scope Plane for the Expense Tracker CLI:

The Expense Tracker CLI aims to provide a comprehensive and user-friendly tool for individuals to track their expenses efficiently. The following features are planned for implementation:

1. User Authentication: Implement user registration and login functionality, allowing users to create accounts to store and manage their expense data securely.

2. Expense Management: Users can add, edit, and delete individual expense records. Each expense will include details such as the date, amount, category, description, and any additional notes.

3. Budget Categories: Users can set up custom budget categories to organise their expenses effectively. The CLI will allow users to add, edit, and delete budget categories as needed.

4. Expense Reports: Generate detailed reports that provide insights into spending patterns, including summaries based on categories, time periods, and total expenses.

5. Filtering and Searching: Implement the ability to filter and search expenses based on specific criteria, such as date range, category, or keyword. This functionality will help users find relevant transactions quickly.

6. Currency Support: Ensure the Expense Tracker CLI supports different currencies to accommodate users from various regions.

7. User-Friendly Interface: Design an intuitive and user-friendly command-line interface that makes it easy for users to interact with the expense tracker efficiently.

8. Data Persistence: Utilize file or database storage to save and retrieve user expense data, ensuring that the information is available across multiple sessions.

9. Budget Alerts: Optionally, provide users with budget alerts or notifications when their spending approaches or exceeds predefined limits.

10. Data Visualisation: Consider incorporating data visualisation options to present expense data graphically, offering users a visual representation of their financial data.

By focusing on these features, the Expense Tracker CLI will offer a powerful and versatile expense management solution for users to maintain control over their financial activities and make informed decisions regarding their spending habits.

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

## Technologies

- HTML
- CSS
- JavaScript
- Materialize CSS Framework
- MongoDB (Database)
- Flask (Python Framework)
- EmailJS
- Heroku
- GitHub

## Testing

### Test Strategy

_(Include information about the overall testing strategy for the website)_

### Test Results

_(Include a summary of the test results)_

## Deployment

### Project Creation

The Expense Tracker is a CLI-based budget management application written in Python. It allows users to track their expenses, categorize them, and monitor their budget for the month. Users can input the amount spent, the expense category, and a name for the expense, and the application will calculate the remaining budget for the month and the daily budget for the rest of the month.

### GitHub Pages

_(Include information about how the website was deployed to GitHub Pages)_
