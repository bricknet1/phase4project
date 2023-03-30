# Slammr

## Finally, social media for criminals.

## Disclaimer

This was created for entertainment purposes only. The creators of this app do not condone criminal activity in any way. Do not, under any circumstances, break any laws or do anything that may cause harm to yourself or others. Your actions are your own responsibility.

## Description

This is a single-page application using React, Python, Flask, and SQLAlchemy to create a social media site exclusively for the use of criminals. Users can:
- Log into / create their account
- Create a profile with a bio, photo, and list of crimes they've committed (from a pre-set list of crimes)
- View posts written by all users
- Write posts that will be visible to all users
- View profiles of other users
- Add/remove other users as a friend
- Send direct messages to other users
- Log out of their account

Users with admin privelages can:
- Add to / edit / delete crimes from the pre-set list of crimes

## Installation

Open the terminal and run this command:
```
pipenv install; pipenv shell
```
Then navigate to the "server" directory, then run each of these commaands in sequence to initiate the back end:
```
flask db init
flask db revision --autogenerate
flask db upgrade
python seed.py
python app.py
```
Open an additional terminal and navigate to the "client" directory, then run the following commands in sequence to initiate the front end:
```
npm install
npm start
```

## Functionality

### React Components

#### App.js
The parent component responsible for rendering the correct child components, as well as checking the authorization of a given user.

#### Crimes.js
This component allows users with admin privelages to add and delete crimes to the main list of crimes. This will affect the crimes that a user can choose when updating their own list of crimes.

#### CrimesList.js
This component renders a list of the crimes and individual user will display on their profile. It also allows them to add and delete crimes from their saved list. The user can Include the date the crime was committed, whether they were caught, and whether they were convicted.

#### EditCrime.js
This component allows users with admin privelages to edit the details of a specific crime.

#### Home.js
This is the main landing page of the app. It renders the posts written by all users, 5 at a time, with the newest post first. Users can click on a post to see the profile of the user who wrote it.

#### Login.js
Users can login or create a new account if they don't already have one.

#### NavBar.js
This is responsible for rendering the logo in the top-left corner, the user's photo toward the right side, and the menu in the top-right corner. The menu will slide out from the right side when the menu icon is clicked.

#### NewPost.js
Users can write new posts in this component, which will then be saved to the database and will be rendered within the Home component.

#### Profile.js
This component will display all of the details of a given user, including:
- Photo
- Name
- Bio
- Friends
- Crimes
- A button to add/remove the user as a friend
- A button to edit the profile if it belongs to the active user
- The history of Direct Messages between the given user and the active user, as well as a form to send a new DM to the given user

### Python files

#### app.py
This is responsible for running the live database and creating all of the CRUD paths needed for the front end to run properly.

#### config.py
This establishes several shared imports that the other Python files need. It also contains the key code for encrypting password data.

#### models.py
This is responsible for generating all of the tables and table relationships in the database.

#### seed.py
This generates seed data for testing purposes.

## Roadmap
Future additions include:
- Ability to "like" posts
- Ability to search for other users by name or crimes
- Significant refactoring of code, particularly with the Profile.js component

## Authors
This project was created by [Kyle Schneider](https://github.com/schnyle) and [Nick Johnson](https://github.com/bricknet1) while attending the Flatiron School's Software Engineering Immersive Bootcamp.