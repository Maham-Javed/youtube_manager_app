import json

def load_data():
    try:
        with open("Youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_all_video(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    while True:
        print("/n Toutube Manager App | Choose an option: ")
        print("1. List all Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

        videos = load_data()
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice.")

if "__name__" == "__main__":
    main()