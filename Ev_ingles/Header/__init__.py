def headerfile(mensage):
    size = 40
    print('-'*size)
    print(mensage.center(40))
    print('-'*size)


def menu(mensage):
    headerfile('Main Menu')
    print('')
    for posi, item in enumerate(mensage):
        print(f'{posi+1} - {item}')
    option = int(input("\nWhat's your choice? "))
    print('')
    return option
