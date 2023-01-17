# TKT_test

1. Why

    This is a technical test project for the web Agency TKT. The objective was to import data from a json file that contains companies data and their financial results for 2017 and 2016, and then display the list of companies and the details of each company.

2. Getting Started

    This project uses the following technologies:

    * Python v3.9 or +

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/) 

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and create a virtual environment <code>python3 -m venv env</code>. This will then set up a a virtual python environment within that directory.

    - Next, on Unix or MacOS, run: <code>source bin/activate</code>, or on Windows: <code>env\Scripts\activate.bat</code>.

    - Then, install the packages you'll need. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file.

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. You can check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details.

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.


4. Testing

    Tests are made with PyTest in the directory /tests. For now, there are only unit tests

    To run Pytest, enter in your terminal: <code>pytest</code>


5. Coverage

If you want to check the coverage report, enter in your terminal: <code>coverage run -m pytest</code> and then: <code>coverage report -m</code>
    
You can also create a coverage html report using the following command in your terminal: <code>coverage html</code>

Then you can check the report in htmlcov/index.html