from suggest import suggest
from user_list import user_list

print('Welcome to MovieMail! Please choose from the following options:')

while True:
    user_in = int(input('\n\t1: View Movie List\n\t2: Add Movie\n\t3: Delete Movie\n\t4: Give Me a Suggestion\n\t5: Exit\n'))
    if user_in == 1:
        for i in user_list:
            print(f'\t- {i}')
    elif user_in == 2:
        movie_in = input('Enter movie: ')
        if movie_in in user_list:
            print('That movie is already in the list!')
        else:
            user_list.append(movie_in)
    elif user_in == 3:
        movie_out = input('Enter movie: ')
        if movie_out not in user_list:
            print('That movie is not in the list!')
        else:
            user_list.remove(movie_out)
    elif user_in == 4:
        movie_sugg = input('Enter movie: ')
        try:
            suggest(movie_sugg)
        except:
            print('Sorry no suggestions available!')
        else:
            suggest(movie_sugg)
    elif user_in == 5:
        break
    else:
        print('Pick a number between 1 and 5')