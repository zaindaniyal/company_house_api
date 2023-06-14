# Company House Data Analysis
This Python script fetches and analyses data from the CompanyHouse API. It answers several interesting questions about the companies matching the search term "sono", including their status, average life, first limited-partnership creation date, those having "vate" in their titles, and finally the sum of digits derived from the premises part of the address for each company type.

## Configuration
To run the script, you'll need to add your API Key for CompanyHouse API. Add it to the script as follows:
```
api_key = 'your-api-key'
```

## Test Cases
The following test cases are included in the **test.py** file:
1. `test_get_company_information_success`: This test verifies the success scenario of the get_company_information function. It mocks the API response and checks if the function returns the expected number of results.

2. `test_get_company_information_error`: This test verifies the error scenario of the get_company_information function. It mocks an error response from the API and ensures that the function returns None.

Feel free to modify or add more test cases as needed.
## Getting Started

1. Clone this repository:

   ```bash
   git clone <repository_url>

2. Initializing a virtual environment:

    ```bash
    python -m venv .venv

3. Activating the virtual environment:

* For Windows
    ```bash
    cd .venv/scripts
    .\activate

* For MacOS
    ```bash
    source .venv/bin/activate

4. Activating the virtual environment:

    ```bash
    cd .venv/scripts
    .\activate

5. Installing requirements:

    ```bash
    pip install -r requirements.txt

6. Running the main pipeline:

    ```bash
    python main.py

7. Running the unit tests:

    ```bash
    python -m unittest .\test.py

8. Running the entire project at once:
* For Windows:
    ```bash
    .\run.bat

* For MacOS:
    ```bash
    chmod +x run.sh
    ./run.sh
## Script Overview
This script will generate output for the following questions:

1. How many companies are there which match the search term “sono”?
2. Of these, how many are active?
3. Of those dissolved, what is the average life of the company (incorporation date to cessation date) in days?
4. When was the first limited-partnership created?
5. Which companies also have “vate” in their title?
6. Taking the digits from the premises part of the address to make a number for each company (e.g. 6-8 = 68, 14b = 14, 1st Floor 45 Main St= 145 etc), what is the sum for each company type?

## Understanding the Output
The script prints the answers to these questions directly to the console. Here's what each of the answers mean:

1. **Total companies**: This is the total number of companies that match the search term "sono".
2. **Active companies**: This is the number of these companies that are currently active.
3. **Average life of dissolved companies**: For companies that are dissolved, this is the average number of days from their incorporation to their cessation.
4. **First limited-partnership creation date**: This is the date when the first limited partnership among these companies was created.
5. **Companies with 'vate' in title**: These are the companies that also have the term "vate" in their title.
6. **Sum for each company type**: For each type of company, this is the sum of numbers derived from the premises part of their address.

## References

- [CompanyHouse API Documentation](https://developer.companieshouse.gov.uk/)
- [CompanyHouse Public Data API Reference](https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference)
