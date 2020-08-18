# MoodFlask

This is a web application which allows users to register or login to their account and enter their daily github commits along with their moods and other to-do lists. The web app suggests media and other entertainments based on mood. The app lets the user to make a to-do list. The app also shows a streak based on github commits.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Python3, pip and MongoDB
You can download and find the instructions to install them through these links:

* [Python3](https://www.python.org/downloads/)
* [Pip](https://pip.pypa.io/en/stable/installing/)
* [MongoDB](https://docs.mongodb.com/manual/administration/install-community/)

### Installing
To install the other necessary packages: 
* Navigate to the repository on your terminal
* Install all other dependencies:
```bash
pip install -r requirements.txt
```
** In case of failure of above command due to version mismatch of any dependency, comment out the particular dependency in 'requirements.txt' and install manually using the command below and re run the above command:
```bash
pip install <failed-dependency-name>
```

## Running the project and using the app
* Start the mongo service:
```bash
sudo systemctl start mongod
```
* Navigate to the "Scripts" folder inside the "package" folder 
* Then run the flask server:
```bash
flask run
```
* Open any browser and go to localhost:5000/
* Register or login
* Go to moods tab, enter how you are feeling and submit

## Future of the project

The future of the application involves suggestions to user based on their mood. For instance, suggesting links to youtube videos, articles or any other form of entertainment to cheer the user up if they register themselves as sad for the day.

If this were a production application, I would have migrated the web app to a cloud platform to handle more traffic and data storage.
