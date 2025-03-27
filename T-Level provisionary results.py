import matplotlib.pyplot as plt
import pandas as pd
import time
import sys

def main():
    print('Welcome!\nPlease select what you would like to view:')
    time.sleep(0.5)
    
    print('(1) Results per core component')
    time.sleep(0.5)
    print('(2) ')
    time.sleep(0.5)
    print('(3) ')

    choice = input('Please enter your choice here:')

    if choice == '1':
        coreresults()
    
    elif choice =='2':
        'a'
    
    elif choice =='3':
        'a'
    
    else:
        print('Please enter a valid response')
        main()

def coreresults():
    while True:
        print('Which core component would you like to view the data for?')
        time.sleep(0.5)
        print('(1) Design, Surveying and Planning')
        time.sleep(0.5)
        print('(2) Digital Production, Design and Development')
        time.sleep(0.5)
        print ('(3) Education and Early Years')
        time.sleep(0.5)
        print('(4) Building Services Engineering')

        view = int(input('Enter your choice here:'))

        if view == '1':
            view = '"Design, Surveying and Planning"'
        
        elif view == '2':
            view = '"Digital Production, Deisgn and Development"'
        
        elif view == '3':
            view = 'Education and Early Years'
        
        elif view == '4':
            view = 'Building Services Engineering'
        
        
        if view in file('tlevel_results_core.csv'):
            file = pd.read_csv('tlevel_results_core.csv')
            data = file[file['core_component'] == view]
            data = pd.DataFrame(data)
            print(data)
            #plt.scatter(data["Attack"], data["Defense"])
            #plt.title(f'Attack vs Defense for gen {view} Pokemon:')
            #plt.xlabel('Attack Power')
            #plt.ylabel('Defense')
            #plt.show()


main()