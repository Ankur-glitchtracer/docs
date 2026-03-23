import random
from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional


class Suit(Enum):
    """Represents the standard suits of a playing card."""
    HEART = 0
    DIAMOND = 1
    CLUB = 2
    SPADE = 3


class Card(ABC):
    """Abstract base class representing a generic playing card."""

    def __init__(self, value: int, suit: Suit) -> None:
        self._value: int = value
        self.suit: Suit = suit
        self.is_available: bool = True

    @property
    @abstractmethod
    def value(self) -> int:
        """Abstract property: specific games dictate how a card's value is resolved."""
        pass


class BlackJackCard(Card):
    """Represents a card implementing Blackjack-specific scoring rules."""

    def __init__(self, value: int, suit: Suit) -> None:
        """
        Initializes a Blackjack card.

        Args:
            value (int): The face value (1 for Ace, 11-13 for Face cards).
            suit (Suit): The suit of the card.
        
        Raises:
            ValueError: If the card value falls outside standard deck bounds.
        """
        if not (1 <= value <= 13):
            raise ValueError(f"Invalid card value: {value}")
        super().__init__(value, suit)

    def is_ace(self) -> bool:
        return self._value == 1

    def is_face_card(self) -> bool:
        """Jack = 11, Queen = 12, King = 13"""
        return 11 <= self._value <= 13

    @property
    def value(self) -> int:
        """Resolves the face value into a Blackjack integer score."""
        if self.is_ace():
            return 1  # Base value for Ace; BlackJackHand resolves the 1 vs 11 duality
        elif self.is_face_card():
            return 10
        return self._value


class Hand:
    """Base collection representing a player's current held cards."""

    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        self.cards: List[Card] = cards if cards is not None else []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def score(self) -> int:
        """Standard cumulative scoring fallback."""
        return sum(card.value for card in self.cards)


class BlackJackHand(Hand):
    """Extended Hand that implements dynamic Blackjack scoring resolution."""

    BLACKJACK_TARGET = 21

    def __init__(self, cards: Optional[List[BlackJackCard]] = None) -> None:
        # Type hinting overridden purely for domain specificity
        super().__init__(cards)  # type: ignore

    def score(self) -> int:
        """
        Calculates the optimal Blackjack score.
        Selects the highest possible score under 21, or the lowest bust if unavoidable.
        """
        possible_scores = self.possible_scores()
        best_under = 0
        min_over = float('inf')

        for s in possible_scores:
            if s <= self.BLACKJACK_TARGET:
                best_under = max(best_under, s)
            else:
                min_over = min(min_over, s)

        return best_under if best_under > 0 else int(min_over)

    def possible_scores(self) -> List[int]:
        """Generates a branching list of all possible scores due to the Ace 1/11 duality."""
        scores = [0]
        for card in self.cards:
            new_scores = []
            for current_score in scores:
                new_scores.append(current_score + card.value)
                
                # Branch the score calculation if the card is a dual-value Ace
                if isinstance(card, BlackJackCard) and card.is_ace():
                    new_scores.append(current_score + 11)
            scores = new_scores
        return scores


class Deck:
    """Manages a collection of Cards, representing a dealer's shoe or deck."""

    def __init__(self, cards: List[Card]) -> None:
        self.cards: List[Card] = cards
        self.deal_index: int = 0

    def remaining_cards(self) -> int:
        """Calculates undealt inventory."""
        return len(self.cards) - self.deal_index

    def deal_card(self) -> Optional[Card]:
        """
        Pulls the next available card from the top of the deck.
        
        Returns:
            Card if available, otherwise None if the deck is exhausted.
        """
        if self.deal_index < len(self.cards):
            card = self.cards[self.deal_index]
            card.is_available = False
            self.deal_index += 1
            return card
        return None

    def shuffle(self) -> None:
        """Shuffles only the remaining, undealt cards in the shoe."""
        remaining = self.cards[self.deal_index:]
        random.shuffle(remaining)
        self.cards = self.cards[:self.deal_index] + remaining
