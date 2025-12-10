from .utils import greet


def main():
    name = input("¿Cómo te llamás? ")
    print(greet(name))


if __name__ == "__main__":
    main()
