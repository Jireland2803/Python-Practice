#List of imports used.
import time
import sys

#Variable declaration

base_url = 'https://api.education.gov.uk/statistics/'
api_version = 'v1'
dataset_id = '63629501-d3ca-c471-9780-ec4cb6fdf172'
data_set_version = '1.0'


def main():
    print('Welcome!')
    time.sleep(0.5)

    while True:

        endpoint = input('Please enter endpoint: ').lower() #Asks the user to enter the endpoint of the URL.

        #Selection statements relative to the entered endpoint

        if endpoint == 'csv':
            csv()
            False
        
        elif endpoint == 'meta':
            meta()
            False
        
        elif endpoint == 'query':
            query()
            False

        elif endpoint == 'summary':
            summary()
            False
        
        else:
            print('Please enter a valid response.')
            True


def csv():

    total_url = base_url + api_version + '/data-sets/' + dataset_id + '/csv?datasetVersion=' + data_set_version #Concatenates the URL elements to form a full URL.
    end(total_url)

def meta():

    total_url = base_url + api_version + '/data-sets/' + dataset_id + '/meta?datasetVersion=' + data_set_version #Concatenates the URL elements to form a full URL.
    end(total_url)

def query():
    total_url = base_url + api_version + '/data-sets/' + dataset_id + '/query?datasetVersion=' + data_set_version #Concatenates the URL elements to form a full URL.
    end(total_url)

def summary():
    total_url = base_url + api_version + '/data-sets/' + dataset_id  #Concatenates the URL elements to form a full URL.
    end(total_url)


def end(url):
    time.sleep(0.5)
    print(f'The URL linked to your endpoint is: {url}') #Prints out the concatenated URL
    time.sleep(0.5)
    while True:
        repeat = input('Would you like to run the program again (y/n)?').lower() #Asks the user if they would like to repeat the code
        
        #If the user enters 'y' (yes) the code repeats from the beginning.
        if repeat == 'y':
            print('Repeating...')
            time.sleep(0.5)
            main()
            False
        #If the user enters 'n' (no) the code ends and will not repeat.
        elif repeat == 'n':
            print('exiting the program.')
            sys.exit()
        
        #If the user does not enter 'y' or 'n', requests that the user enters a valid response, repeats the question.
        else:
            print('Please enter a valid response.')
            True


#--------------------------------------------------------Main program----------------------------------------------


main()