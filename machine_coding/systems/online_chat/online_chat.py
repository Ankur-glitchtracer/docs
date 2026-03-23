from abc import ABC
from datetime import datetime
from enum import Enum
from typing import Dict, List


class RequestStatus(Enum):
    """Represents the status of a friend request."""
    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3


class Message:
    """Represents a single text message within a chat."""

    def __init__(self, message_id: str, message: str, timestamp: datetime) -> None:
        """
        Initializes a Message.

        Args:
            message_id (str): Unique identifier for the message.
            message (str): The content of the message.
            timestamp (datetime): The time the message was sent.
        """
        self.message_id: str = message_id
        self.message: str = message
        self.timestamp: datetime = timestamp


class AddRequest:
    """Represents a friend request from one user to another."""

    def __init__(self, from_user_id: str, to_user_id: str, request_status: RequestStatus, timestamp: datetime) -> None:
        """
        Initializes an AddRequest.

        Args:
            from_user_id (str): ID of the user sending the request.
            to_user_id (str): ID of the user receiving the request.
            request_status (RequestStatus): Current status of the request.
            timestamp (datetime): When the request was created.
        """
        self.from_user_id: str = from_user_id
        self.to_user_id: str = to_user_id
        self.request_status: RequestStatus = request_status
        self.timestamp: datetime = timestamp


class User:
    """Represents a user in the chat system."""

    def __init__(self, user_id: str, name: str, pass_hash: str) -> None:
        """
        Initializes a User.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Display name of the user.
            pass_hash (str): Hashed password for authentication.
        """
        self.user_id: str = user_id
        self.name: str = name
        self.pass_hash: str = pass_hash
        self.friends_by_id: Dict[str, 'User'] = {}
        self.private_chats_by_friend_id: Dict[str, 'PrivateChat'] = {}
        self.group_chats_by_id: Dict[str, 'GroupChat'] = {}
        self.received_friend_requests: Dict[str, AddRequest] = {}
        self.sent_friend_requests: Dict[str, AddRequest] = {}

    def receive_friend_request(self, request: AddRequest) -> None:
        """Stores an incoming friend request."""
        self.received_friend_requests[request.from_user_id] = request

    def send_friend_request(self, request: AddRequest) -> None:
        """Stores an outgoing friend request."""
        self.sent_friend_requests[request.to_user_id] = request


class Chat(ABC):
    """Abstract base class representing a generic chat channel."""

    def __init__(self, chat_id: str) -> None:
        """
        Initializes a Chat.

        Args:
            chat_id (str): Unique identifier for the chat.
        """
        self.chat_id: str = chat_id
        self.users: List[User] = []
        self.messages: List[Message] = []

    def add_message(self, message: Message) -> None:
        """Appends a new message to the chat history."""
        self.messages.append(message)


class PrivateChat(Chat):
    """Represents a 1-on-1 chat between two users."""

    def __init__(self, chat_id: str, user1: User, user2: User) -> None:
        """
        Initializes a PrivateChat.

        Args:
            chat_id (str): Unique identifier for the chat.
            user1 (User): The first participant.
            user2 (User): The second participant.
        """
        super().__init__(chat_id)
        self.users.extend([user1, user2])


class GroupChat(Chat):
    """Represents a multi-user group chat."""

    def __init__(self, chat_id: str) -> None:
        super().__init__(chat_id)

    def add_user(self, user: User) -> None:
        """Adds a user to the group chat."""
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user: User) -> None:
        """Removes a user from the group chat."""
        if user in self.users:
            self.users.remove(user)


class UserService:
    """Service class responsible for managing user interactions and routing."""

    def __init__(self) -> None:
        self.users_by_id: Dict[str, User] = {}

    def add_user(self, user_id: str, name: str, pass_hash: str) -> User:
        """Registers a new user in the system."""
        user = User(user_id, name, pass_hash)
        self.users_by_id[user_id] = user
        return user

    def remove_user(self, user_id: str) -> None:
        """Removes a user from the system."""
        self.users_by_id.pop(user_id, None)

    def send_friend_request(self, from_user_id: str, to_user_id: str) -> None:
        """Orchestrates sending a friend request between two users."""
        from_user = self.users_by_id.get(from_user_id)
        to_user = self.users_by_id.get(to_user_id)
        
        if from_user and to_user:
            request = AddRequest(from_user_id, to_user_id, RequestStatus.UNREAD, datetime.now())
            from_user.send_friend_request(request)
            to_user.receive_friend_request(request)

    def approve_friend_request(self, from_user_id: str, to_user_id: str) -> None:
        """Approves a pending friend request and establishes the connection."""
        from_user = self.users_by_id.get(from_user_id)
        to_user = self.users_by_id.get(to_user_id)
        
        if from_user and to_user:
            request = to_user.received_friend_requests.get(from_user_id)
            if request:
                request.request_status = RequestStatus.ACCEPTED
                from_user.friends_by_id[to_user_id] = to_user
                to_user.friends_by_id[from_user_id] = from_user
