# CST8916 Midterm REST API

## Project Setup
In this setup we have the:
- .gitignore file to ensuure certain files are not tracked
- CST8916API.py file that is used to define the students list and all of the GET , POST , PUT and DELETE methods
- requirements.txt file that is used to download all of the necessary requirements to run the API
- test-api.http file that is used to test the API given the defined methods in the .py file

## Environment configuration 
For the environment configuration we put the PORT number in the .env file which is set to PORT=8000

## How to run the service locally
To run the API on your local machine:
1. Clone the repository with the following command:
   ```
   git clone https://github.comhttps://github.com/jaelendsetosta-AC/CST8916Midterm.git
   ```
2. Navigate to the project directory:
   ```
   cd CST8916Midterm
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the Application:
   ```
   python3 CST8916API.py
   ```

 5. The api will be running at http://127.0.0.1:8000
 6. Use test-api.http to test the REST API using the REST Client extension in Visual Studio Code.
   
