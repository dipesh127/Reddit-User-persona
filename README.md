Reddit User Persona Generator
This project analyzes a Reddit user's activity to generate a persona based on their posts and comments. It uses natural language processing techniques to extract insights about the user's interests, personality, and behavior.
Prerequisites

Python 3.6 or higher
pip (Python package installer)

Installation

Clone the repository:
git clone https://github.com/dipesh127/Reddit-User-persona.git
cd Reddit-User-persona


Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install required libraries:
pip install -r requirements.txt



Obtaining Reddit API Credentials
To use this script, you need to create a Reddit application and obtain API credentials:

Go to Reddit Apps.
Click "Create App" or "Create Another App".
Fill in the form:
Name: Choose a name for your app.
App type: Select "script".
Description: Optional.
About URL: Optional.
Redirect URI: Set to http://localhost:8080.


Click "Create App".
Note down the client ID (under the app name) and client secret.

Usage

Set environment variables:
export REDDIT_CLIENT_ID='your_client_id'
export REDDIT_CLIENT_SECRET='your_client_secret'
export REDDIT_USER_AGENT='reddit_persona_generator by /u/your_reddit_username'

Replace 'your_client_id', 'your_client_secret', and 'your_reddit_username' with your actual values. On Windows, use set instead of export.



To create an account on the Groq console at https://console.groq.com/ for API access, follow these steps:

Visit the Groq Console
Go to https://console.groq.com/.
Sign Up or Log In
If you don’t have an account, click "Sign Up" and complete the registration process by providing the required information.
If you already have an account, click "Log In" and enter your credentials.
Navigate to the API Keys Section
Once logged in, locate the API Keys section. You can typically find this:
In the left-side navigation panel, or
By clicking the three horizontal lines (hamburger menu) in the top right corner and selecting "Developers" from the dropdown menu.
Create an API Key
In the API Keys section, click "Create API Key" or a similar button.
Name Your API Key
Provide a name or description for your API key to help you identify it later (e.g., "My Project API Key").
Generate the API Key
Click "Submit" or "Create" to generate your API key.
Secure Your API Key
Copy the generated API key and store it in a secure location. Treat it like a password—do not share it publicly, as it is used to authenticate your requests to the Groq API.



Run the script:
python main.py <reddit_username>
For example:
python main.py https://www.reddit.com/user/kojied/comments/
        or 
python main.py kojied

This will generate a persona for the specified user and save it in a text file named <username>_persona.txt in the project directory.


Examples
Sample persona files for the following users are included in the repository:
kojied_persona.txt

After generating persona of user we conver it to json file so that we can use it to create an html based persona using html templete for every new reddit users dynamically


These files were generated using the script and serve as references. To generate a persona for a new Reddit user, follow the usage instructions above.




Output Example:

![Alt text](path/to/1.jpg)
![Alt text](path/to/2.jpg)
![Alt text](path/to/3.jpg)
