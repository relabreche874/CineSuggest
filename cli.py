import csv

from suggest import suggest_cli
from user_list import user_list


def cli_menu():
    print('Welcome to MovieMail! Please choose from the following options:')

    while True:
        print('\n----------------------------------------------------------------------')
        user_in = int(input('\n1: View Movie List\n2: Add Movie\n3: Delete Movie\n4: Recommend NOW\n5: Exit\n\n--> '))

        if user_in == 1:
            print('Your Movie List:\n')
            with open('movie_list.csv', newline='') as f:
                reader = csv.reader(f)
                for movie in reader:
                    print('\n'.join(movie))
        elif user_in == 2:
            movie_in = input('Enter movie: ').strip()
            with open('movie_list.csv', 'r') as f:
                reader = csv.reader(f)
                movies = [row[0] for row in reader]
            if movie_in in movies:
                print('That movie is already in the list!')
            else:
                with open('movie_list.csv', 'a', newline='') as f:
                    write = csv.writer(f)
                    write.writerow([movie_in])
        elif user_in == 3:
            movie_out = input('Enter movie: ')
            with open('movie_list.csv', 'r') as f:
                reader = csv.reader(f)
                movies = [row[0] for row in reader]
                if movie_out not in movies:
                    print('That movie is not in the list!')
                else:
                    movies.remove(movie_out)
                    with open('movie_list.csv', 'w', newline='') as f:
                        writer = csv.writer(f)
                        for movie in movies:
                            writer.writerow([movie])
        elif user_in == 4:
            movie_sugg = input('Enter movie: \n')
            try:
                suggest_cli(movie_sugg)
            except:
                print('Sorry no suggestions available!')
        elif user_in == 5:
            break
        else:
            print('Pick a number between 1 and 5')

cli_menu()