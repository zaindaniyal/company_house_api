import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import re
from dotenv import load_dotenv
import os

load_dotenv() 


def get_company_information(search_term, api_key):
    """
    Fetch company information based on search term using API call

    Args:
        search_term (str): The term to search
        api_key (str): The API key for authentication

    Returns:
        all_results (list): The list of companies information
    """

    base_url = "https://api.companieshouse.gov.uk"
    search_endpoint = "/search/companies"
    params = {
        "q": search_term,
        "items_per_page": 100,
        "start_index": 0,
    }

    all_results = []

    while True:
        response = requests.get(
            f"{base_url}{search_endpoint}",
            params=params,
            auth=HTTPBasicAuth(api_key, ''),
        )
        if response.status_code == 200:
            results = response.json()
            total_results = results.get("total_results", 0)
            items = results.get("items", [])
            all_results.extend(items)

            params["start_index"] += params["items_per_page"]

            if len(all_results) >= total_results:
                break
        else:
            return None

    return all_results


def main():
    """
    Main function to execute the script
    """

    api_key = os.getenv("HOUSE_API_KEY")
    search_term = "sono"

    company_information = get_company_information(search_term, api_key)

    if company_information:
        print(f"Question 1: How many companies are there which match the search term {search_term}?")
        print(f"Answer 1: Total Companies with term {search_term}: {len(company_information)}")

        active_companies = []
        total_duration = 0
        dissolved_count = 0
        first_lp_creation_date = None
        companies_with_vate = []
        company_type_sums = {}

        for company in company_information:
            if 'date_of_creation' in company and 'date_of_cessation' not in company:
                active_companies.append(company['title'])

            if 'date_of_creation' in company and 'date_of_cessation' in company:
                creation_date = datetime.strptime(company['date_of_creation'], '%Y-%m-%d')
                cessation_date = datetime.strptime(company['date_of_cessation'], '%Y-%m-%d')
                duration = (cessation_date - creation_date).days
                total_duration += duration
                dissolved_count += 1

            if company['company_type'] == 'limited-partnership':
                creation_date = datetime.strptime(company['date_of_creation'], '%Y-%m-%d')
                if first_lp_creation_date is None or creation_date < first_lp_creation_date:
                    first_lp_creation_date = creation_date

            if 'vate' in company['title'].lower():
                companies_with_vate.append(company['title'])

            if "address" in company and company["address"] is not None:
                premises = company['address'].get('premises', '')
                digits = re.findall(r'\d+', premises)
                premises_sum = sum(int(digit) for digit in digits)
                company_type = company['company_type']

                if company_type not in company_type_sums:
                    company_type_sums[company_type] = 0

                company_type_sums[company_type] += premises_sum

        print(f"Question 2: How many of these companies are active?")
        print(f"Answer 2: Total Active Companies: {len(active_companies)}")

        print("Question 3: What is the average life of the company (incorporation date to cessation date) in days of those dissolved ?")
        if dissolved_count > 0:
            average_life = total_duration / dissolved_count
            print(f"Answer 3: The average life of dissolved companies is {average_life:.2f} days.")
        else:
            print("Answer 3: No dissolved companies found.")

        print("Question 4: When was the first limited-partnership created?")
        if first_lp_creation_date is not None:
            print(f"Answer 4: The first limited partnership was created on {first_lp_creation_date.strftime('%Y-%m-%d')}.")
        else:
            print("Answer 4: No limited partnerships found.")

        print("Question 5: Which companies also have \"vate\" in their title?")
        if companies_with_vate:
            print("Answer 5: Companies with 'vate' in their title:", len(companies_with_vate))
        else:
            print("Answer 5: No companies found with 'vate' in their title.")

        print("Question 6: Taking the digits from the premises part of the address to make a number for each company, what is the sum for each company type?")
        print("Answer 6: Sum of premises digits for each company type:")
        for company_type, premises_sum in company_type_sums.items():
            print(f"{company_type}: {premises_sum}")

    else:
        print("Error occurred while making the API request.")


if __name__ == "__main__":
    main()
