#!/usr/bin/env python
import os
import sys
import csv
from urllib.error import HTTPError
import urllib.request
from argparse import ArgumentParser
import datetime

if __name__ == "__main__":
    """
    This bulk sample data tool takes in a pipe-separated values file containing
    people data and POSTs them to the registry REST API.
    """
    parser = ArgumentParser()
    parser.add_argument('file', help='Path to file containing sample data.')
    args = parser.parse_args()
    
    url = 'http://127.0.0.1:8000/people/'
    
    with open(args.file, "rt") as csvfile:
        for row in csv.DictReader(csvfile):
            # Extract person data from the CSV
            # TODO: Needs better edge case handling
            id = row['ID']
            first_name = row['First']
            last_name = row['Last']
            age = row['Age']
            github_acct = row['GithubAcct']
            third_grade_grad_date = row['Date of 3rd Grade Graduation']
            # Do some date parsing and mangling to get things into the correct format
            if third_grade_grad_date:
                parsed_datetime = datetime.datetime.strptime(third_grade_grad_date, '%m/%d/%y')
                parsed_date = parsed_datetime.date()
                third_grade_grad_date = parsed_date.strftime('%Y-%m-%d')
            
            # JSONify Person object
            # TODO: This is vulnerable to injection attacks... needs more validation
            person_template = r'{{"id" : "{0}", "first_name" : "{1}", "last_name" : "{2}", "age" : "{3}", "github_acct" : "{4}", "third_grade_grad_date" : "{5}"}}'
            person = person_template.format(id, first_name, last_name, age, github_acct, third_grade_grad_date)
            
            # Send data to server via POST to REST API
            binary_data = person.encode('utf-8')
            req = urllib.request.Request(url, binary_data, {'Content-Type': 'application/json'})
            try:
                response = urllib.request.urlopen(req)
                result = response.read()
                # print(result)
                response.close()
            except HTTPError as e:
                print('Error while loading sample data. Got code: ' + str(e.code) + ' and message: ' + str(e.read()))