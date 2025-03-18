import sqlite3

file_name  = "Youtube.txt"

con = sqlite3.connect('youtube.db')
curser = con.cursor()

curser.execute('''
CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
''')

# List all the data from the file
def list_all_video():
    curser.execute('SELECT * FROM videos')
    for row in curser.fetchall():
        print(row)

# Add video to list
def add_video(name, time):
    curser.execute('INSERT INTO videos(name, time) VALUES(?, ?)', (name, time))
    con.commit()

# Update video in list
def update_video(video_id, new_name, new_time):
    curser.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (new_name, new_time, video_id))
    con.commit()

# Delete video from list
def delete_video(video_id):
    curser.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    con.commit()

def main():

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
                list_all_video()

            case '2':
                name = input("\nEnter video name: ")
                time = input("Enter video duration: ")  
                add_video(name, time)

            case '3':
                index = int(input("Enter the index of the video you want to update: "))
                name = input("\nEnter your new video name:")
                time = input("Enter your new video duration:")
                update_video(index, name, time)

            case '4':
                index = int(input("Enter the index of the video you want to delete: "))
                delete_video(index)
            case '5':
                break
            case _:
                print("Invalid choice.")

    con.close()

# Run the main function
if __name__ == "__main__":
    main()