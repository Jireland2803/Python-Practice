import matplotlib.pyplot as plt
import pandas as pd
import time
import sys


def main():
    print('Welcome!\nPlease select what you would like to view:')
    time.sleep(0.5)
    
    print('(1) View the number of legendaries per generation')
    time.sleep(0.5)
    print('(2) View the average speed per generation')
    time.sleep(0.5)
    print('(3) View the Attack Power vs Defense in a generation of your choice')

    choice = input('Please enter your choice here:')

    if choice == '1':
        legendary()
    
    elif choice =='2':
        avgspeed()
    
    elif choice =='3':
        pokemon_per_generation()
    
    else:
        print('Please enter a valid response')
        main()



def legendary():
    file = pd.read_csv('Pokemon.csv')
    data = file[file['Legendary'] == True]
    data = pd.DataFrame(data)
    data = data['Generation'].value_counts()
    data.plot.bar()
    plt.ylim(0, data.max()+5)
    plt.show()
    

def avgspeed():
    file = pd.read_csv('Pokemon.csv')
    avg_speed = file.groupby('Generation')['Speed'].mean()  # Compute average speed per generation
    avg_speed.plot(kind='bar', color='skyblue')  # Plot as a bar chart
    plt.title('Average Speed per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Average Speed')
    plt.show()

def avgspeed_scatter():
    file = pd.read_csv('Pokemon.csv')
    avg_speed = file.groupby('Generation')['Speed'].mean()  # Compute average speed per generation
    avg_speed.plot(kind='bar', color='skyblue')  # Plot as a bar chart
    plt.title('Average Speed per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Average Speed')
    plt.show()



def pokemon_per_generation():
    view = int(input('Which generation would you like to view? (1-6)'))
    
    if view >= 1 and view <= 6:
        file = pd.read_csv('Pokemon.csv')
        data = file[file['Generation'] == view]
        data = pd.DataFrame(data)
        print(data)
        plt.scatter(data["Attack"], data["Defense"])
        plt.title(f'Attack vs Defense for gen {view} Pokemon:')
        plt.xlabel('Attack Power')
        plt.ylabel('Defense')
        plt.show()




main()

loop1 = True
while loop1 == True:
    time.sleep(0.5)
    repeat = input('Would you like to repeat the program?\n(y/n):')
    
    if repeat == 'y':
        print('Repeating the program')
        time.sleep(0.5)
        main()
        loop1 = False
    
    elif repeat =='n':
        print('Ending the program')
        time.sleep(0.5)
        sys.exit()
        
    
    else:
        print('Please enter a valid response')
        loop1 = True
