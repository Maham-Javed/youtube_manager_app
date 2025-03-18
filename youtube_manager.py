import json

file_name  = "Youtube.txt"

# Load data from file
def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to file
def save_data_helper(videos):
    with open(file_name, 'w') as file:
        # dump is the json func, which will write data to the file
        json.dump(videos, file)

# List all the data from the file
def list_all_video(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"\n {index}. {video['name']}, Duration: {video['time']}")

# Add video to list
def add_video(videos):
    name = input("\n Enter video name: ")
    time = input("Enter video duration: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)
    print("\t Video added successfully!")

# Update video in list
def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the index of the video you want to update: "))
    if 1 <= index <= len(videos):
        name = input("\nEnter your new video name:")
        time = input("Enter your new video duration:")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
        print("\t Video updated successfully!")
    else:
        print("Invalid index")

# Delete video from list
def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the index of the video you want to delete: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
        print("\t Video deleted successfully!")
    else:
        print("Invalid index")

def main():
    videos = load_data()

    while True:
        print("\nToutube Manager App | Choose an option: ")
        print("1. List all Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit")

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

# Run the main function
if __name__ == "__main__":
    main()