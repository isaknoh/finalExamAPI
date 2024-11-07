import requests
from webexteamssdk import WebexTeamsAPI

def get_access_token():
    choice = input("Do you want to use a hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
    else:
        access_token = "ZTNmYjkzYWEtMGM0Yi00MGU4LWE1NDQtYmJkOTRiYTdiNmE3YzNhMzYwOGYtNTgz_P0A1_856a32b6-339b-4d3d-89fb-dabbd25aff7b"
    return access_token

def create_room(api):
    room_name = input("Enter the name of the room you want to create: ").strip()
    try:
        room = api.rooms.create(room_name)
        print(f"Room '{room.title}' created successfully with ID: {room.id}")
        return room.id
    except Exception as e:
        print(f"Error creating room: {e}")
        return None

def send_welcome_message(api, room_id):
    welcome_message = input("Enter the welcome message you want to send: ").strip()
    try:
        api.messages.create(room_id, text=welcome_message)
        print("Welcome message sent successfully.")
    except Exception as e:
        print(f"Error sending welcome message: {e}")

def add_participant_to_room(room_id, person_email, access_token):
    url = "https://webexapis.com/v1/memberships"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "roomId": room_id,
        "personEmail": person_email
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print(f"Participant {person_email} added successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error adding participant: {e}")

def list_room_messages(api, room_id):
    try:
        messages = api.messages.list(room_id)
        if messages:
            print("\nList of messages in the room:")
            for message in messages:
                print(f"Message ID: {message.id}, Text: {message.text}")
        else:
            print("No messages found in this room.")
    except Exception as e:
        print(f"Error retrieving messages: {e}")

def delete_message(api, message_id):
    try:
        api.messages.delete(message_id)
        print(f"Message with ID {message_id} has been deleted.")
    except Exception as e:
        print(f"Error deleting message: {e}")

def main():
    access_token = get_access_token()
    print(f"Using Access Token: {access_token[:10]}...")
    api = WebexTeamsAPI(access_token=access_token)

    # Create a room
    room_id = create_room(api)
    if not room_id:
        return

    # Send a welcome message
    send_welcome_message(api, room_id)

    # Add multiple participants
    while True:
        person_email = input("Enter participant's email (or type 'done' to finish): ").strip()
        if person_email.lower() == "done":
            break
        add_participant_to_room(room_id, person_email, access_token)

    # List all room messages
    list_room_messages(api, room_id)

    # Option to delete a specific message
    delete_choice = input("\nDo you want to delete a message? (y/n): ").strip()
    if delete_choice.lower() == 'y':
        message_id = input("Enter the message ID to delete: ").strip()
        delete_message(api, message_id)

if __name__ == "__main__":
    main()
