from classes import Movie, MovieCollection

def main():
    collection = MovieCollection()

    while True: #пока цикл выполняется, давать выбор пользователю при взаимодйствии с программой
        print("\n====== Меню ======")
        print("1. Добавить фильм")
        print("2. Удалить фильм")
        print("3. Добавить фильм в коллекцию")
        print("4. Удалить фильм из коллекции")
        print("5. Найти фильмы по жанру")
        print("6. Найти фильмы по году")
        print("7. Найти фильмы по ключевому слову в названии")
        print("8. Показать все фильмы")
        print("9. Показать все коллекции")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Название фильма: ")
            genre = input("Жанр: ")
            year = int(input("Год: "))
            collection.add_movie(Movie(title, genre, year))
            print("Фильм добавлен!")

        elif choice == "2":
            title = input("Название фильма для удаления: ")
            collection.remove_movie(title)
            print("Фильм удалён!")

        elif choice == "3":
            title = input("Название фильма: ")
            col_name = input("Название коллекции: ")
            collection.add_to_collection(col_name, title)
            print("Добавлено в коллекцию!")

        elif choice == "4":
            title = input("Название фильма: ")
            col_name = input("Название коллекции: ")
            collection.remove_from_collection(col_name, title)
            print("Удалено из коллекции!")

        elif choice == "5":
            genre = input("Жанр: ")
            results = collection.search_by_genre(genre)
            for m in results:
                print(m)

        elif choice == "6":
            year = int(input("Год: "))
            results = collection.search_by_year(year)
            for m in results:
                print(m)

        elif choice == "7":
            keyword = input("Ключевое слово: ")
            results = collection.search_by_keyword(keyword)
            for m in results:
                print(m)

        elif choice == "8":
            print("\nВсе фильмы:")
            for movie in collection: #перебор с помощью итератора
                print(movie)

        elif choice == "9":
            collection.list_collections()

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Повторите.")


if __name__ == "__main__":
    main()