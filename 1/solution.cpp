#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <ctime>

enum Suit { HEARTS, DIAMONDS, CLUBS, SPADES };
enum Rank { NINE, TEN, JACK, QUEEN, KING, ACE };

std::ostream& operator<<(std::ostream& os, const Suit& suit) {
    switch (suit) {
        case HEARTS:    os << "H"; break;
        case DIAMONDS:  os << "D"; break;
        case CLUBS:     os << "C"; break;
        case SPADES:    os << "S"; break;
    }
    return os;
}

std::ostream& operator<<(std::ostream& os, const Rank& rank) {
    switch (rank) {
        case NINE:   os << "9"; break;
        case TEN:    os << "T"; break;
        case JACK:   os << "J"; break;
        case QUEEN:  os << "Q"; break;
        case KING:   os << "K"; break;
        case ACE:    os << "A"; break;
    }
    return os;
}

class Card {
public:
    Suit suit;
    Rank rank;
    Card() : suit(HEARTS), rank(NINE) {}
    Card(Suit s, Rank r) : suit(s), rank(r) {}

    void display() const {
        std::cout << rank << suit;
    }

    // Function to compare cards, considering trump and following suit
    bool operator>(const Card& other) const {
        return rank > other.rank;
    }
};

class Deck {
public:
    std::vector<Card> cards;

    Deck() {
        for (int s = HEARTS; s <= SPADES; s++) {
            for (int r = NINE; r <= ACE; r++) {
                cards.push_back(Card(static_cast<Suit>(s), static_cast<Rank>(r)));
            }
        }
    }

    void shuffle() {
        std::srand(std::time(0));
        std::random_shuffle(cards.begin(), cards.end());
    }

    Card deal() {
        Card card = cards.back();
        cards.pop_back();
        return card;
    }
};

class Player {
public:
    std::vector<Card> hand;
    std::vector<Card> faceUp;
    std::vector<Card> faceDown;
    int score = 0;
    int tricksWon = 0;

    void displayHand() const {
        std::cout << "Hand: ";
        for (const Card& card : hand) {
            card.display();
            std::cout << " ";
        }
        std::cout << std::endl;

        std::cout << "Face Up: ";
        for (const Card& card : faceUp) {
            card.display();
            std::cout << " ";
        }
        std::cout << std::endl;
    }
};

class Game {
public:
    Player player1;
    Player player2;
    Deck deck;
    Suit trump;
    int currentBid = 0;
    Player* bidder;
    Player* currentPlayer;
    std::vector<Card> currentTrick;
    Suit ledSuit;
    bool trickFinished = false;

    Game() {
        deck.shuffle();
        dealCards();
        currentPlayer = &player2; // Non-dealer starts the bidding
    }

    void dealCards() {
        player1.hand.clear();
        player1.faceUp.clear();
        player1.faceDown.clear();
        player2.hand.clear();
        player2.faceUp.clear();
        player2.faceDown.clear();
        deck = Deck();
        deck.shuffle();

        for (int i = 0; i < 4; i++) {
            player1.hand.push_back(deck.deal());
            player2.hand.push_back(deck.deal());
        }
        for (int i = 0; i < 4; i++) {
            player1.faceDown.push_back(deck.deal());
            player2.faceDown.push_back(deck.deal());
        }
        for (int i = 0; i < 4; i++) {
            player1.faceUp.push_back(deck.deal());
            player2.faceUp.push_back(deck.deal());
        }
    }

    void bidding() {
        bool passed = false;
        switchPlayer();

        while (passed == false) {
            std::cout << "Player " << (currentPlayer == &player1 ? 1 : 2) << ", your hand:" << std::endl;
            currentPlayer->displayHand();
            std::cout << "Current bid is " << currentBid << ". Enter your bid (7-12, or 'pass'): ";
            std::string input;
            std::cin >> input;

            if (input == "pass") {
                passed = true;
                if (currentBid == 0) {
                    std::cout << "Both players passed. Re-dealing..." << std::endl;
                    dealCards();
                    switchPlayer();
                }
                continue;
            }

            int bid;
            try {
                bid = std::stoi(input);

                if (bid >= 7 && bid <= 12 && bid > currentBid) {
                    currentBid = bid;
                    bidder = currentPlayer;
                    switchPlayer();
                } else {
                    std::cout << "Invalid bid. Please enter a number between 7 and 12, and higher than the current bid." << std::endl;
                    continue;
                }
            } catch (const std::invalid_argument& e) {
                std::cout << "Invalid input. Please enter a number or 'pass'." << std::endl;
                continue;
            }
        }

        std::cout << "Player " << (bidder == &player1 ? 1 : 2) << " wins the bid with " << currentBid << " tricks." << std::endl;
        chooseTrump();
    }

    void chooseTrump() {
        std::cout << "Player " << (bidder == &player1 ? 1 : 2) << ", choose trump (H, D, C, S): ";
        char trumpInput;
        std::cin >> trumpInput;

        switch (trumpInput) {
            case 'H': trump = HEARTS; break;
            case 'D': trump = DIAMONDS; break;
            case 'C': trump = CLUBS; break;
            case 'S': trump = SPADES; break;
            default:
                std::cout << "Invalid input. Please enter H, D, C, or S." << std::endl;
                chooseTrump();
                return;
        }

        std::cout << "Trump is " << trump << std::endl;
    }

    // Function to get the card index from the player's input
    int getCardIndex(const std::string& input) {
        if (input.size() != 2) {
            return -1; // Invalid input format
        }

        Rank rank;
        switch (input[0]) {
            case '9': rank = NINE; break;
            case 'T': rank = TEN; break;
            case 'J': rank = JACK; break;
            case 'Q': rank = QUEEN; break;
            case 'K': rank = KING; break;
            case 'A': rank = ACE; break;
            default: return -1; // Invalid rank
        }

        Suit suit;
        switch (input[1]) {
            case 'H': suit = HEARTS; break;
            case 'D': suit = DIAMONDS; break;
            case 'C': suit = CLUBS; break;
            case 'S': suit = SPADES; break;
            default: return -1; // Invalid suit
        }

        // Find the index of the card in the player's hand and faceUp cards
        for (size_t i = 0; i < currentPlayer->hand.size(); ++i) {
            if (currentPlayer->hand[i].rank == rank && currentPlayer->hand[i].suit == suit) {
                return i;
            }
        }
        for (size_t i = 0; i < currentPlayer->faceUp.size(); ++i) {
            if (currentPlayer->faceUp[i].rank == rank && currentPlayer->faceUp[i].suit == suit) {
                return i + currentPlayer->hand.size(); // Add hand size to differentiate
            }
        }

        return -1; // Card not found
    }

     void playCard() {
        std::cout << "Player " << (currentPlayer == &player1 ? 1 : 2) << ", your hand:" << std::endl;
        currentPlayer->displayHand();
        std::cout << "Enter the card to play (e.g., AH for Ace of Hearts): ";
        std::string input;
        std::cin >> input;

        int cardIndex = getCardIndex(input);
        if (cardIndex == -1) {
            std::cout << "Invalid card input or card not found." << std::endl;
            playCard(); // Ask for input again
            return;
        }

        Card playedCard;
        if (cardIndex < currentPlayer->hand.size()) {
            playedCard = currentPlayer->hand[cardIndex];
            currentPlayer->hand.erase(currentPlayer->hand.begin() + cardIndex);
        } else {
            cardIndex -= currentPlayer->hand.size(); // Adjust index for faceUp cards
            playedCard = currentPlayer->faceUp[cardIndex];
            currentPlayer->faceUp.erase(currentPlayer->faceUp.begin() + cardIndex);
            // Make the faceDown card available
            if (!currentPlayer->faceDown.empty()) {
               currentPlayer->hand.push_back(currentPlayer->faceDown[cardIndex]);
               currentPlayer->faceDown.erase(currentPlayer->faceDown.begin() + cardIndex);
            }
        }

        currentTrick.push_back(playedCard);
        std::cout << "Player " << (currentPlayer == &player1 ? 1 : 2) << " played ";
        playedCard.display();
        std::cout << std::endl;

        if (currentTrick.size() == 1) {
            ledSuit = playedCard.suit; // Set the led suit for the trick
        }

        //Check for valid move and must follow rule here

        if (currentTrick.size() == 2) {
            trickFinished = true;
            Player* winningPlayer = determineTrickWinner();
            std::cout << "Player " << (winningPlayer == &player1 ? 1 : 2) << " wins the trick!" << std::endl;
            winningPlayer->tricksWon++;
            player1.displayHand();
            player2.displayHand();
            currentTrick.clear();
            ledSuit = HEARTS;
            trickFinished = false;
        }

        switchPlayer();
    }

    Player* determineTrickWinner() {
       if (currentTrick.size() != 2) {
            std::cerr << "Error: determineTrickWinner called with incomplete trick." << std::endl;
            return nullptr;
        }
        Card card1 = currentTrick[0];
        Card card2 = currentTrick[1];
        Player* player1Ptr = (currentPlayer == &player2) ? &player1 : &player2;
        Player* player2Ptr = currentPlayer;

        // Check if the led suit is the trump suit
        bool ledSuitIsTrump = (ledSuit == trump);
        bool card1IsTrump = (card1.suit == trump);
        bool card2IsTrump = (card2.suit == trump);

        // 1. If a trump card is played, the highest trump wins
        if (card1IsTrump || card2IsTrump) {
            if (card1IsTrump && card2IsTrump) {
                // Both cards are trump, compare ranks
                if (card1 > card2) {
                    return player1Ptr;
                } else {
                    return player2Ptr;
                }
            } else if (card1IsTrump) {
                return player1Ptr;
            } else {
                return player2Ptr;
            }
        } else {
            // 2. If no trump is played, the highest card of the led suit wins
            if (card1.suit == ledSuit && card2.suit == ledSuit) {
                // Both cards are of the led suit, compare ranks
                if (card1 > card2) {
                    return player1Ptr;
                } else {
                    return player2Ptr;
                }
            } else if (card1.suit == ledSuit) {
                return player1Ptr;
            } else {
                return player2Ptr;
            }
        }
    }

    void switchPlayer() {
        currentPlayer = (currentPlayer == &player1) ? &player2 : &player1;
    }

     void playGame() {
        while (player1.hand.size() + player1.faceUp.size() + player2.hand.size() + player2.faceUp.size() > 0) {
            switchPlayer(); // Ensure the correct player starts each trick
             playCard();
            if (trickFinished) {
                if (player1.hand.empty() && player1.faceUp.empty() && player2.hand.empty() && player2.faceUp.empty())
                    break;
            }
        }
         // After all tricks are played, calculate and display scores
        calculateScore();
        displayScore();
    }

    void calculateScore() {
        int bidTricks = currentBid;

        if (bidder->tricksWon >= bidTricks) {
            if (bidTricks == 7) bidder->score += 1;
            if (bidTricks == 8) bidder->score += 2;
            if (bidTricks == 9) bidder->score += 3;
            if (bidTricks == 10) bidder->score += 4;
            if (bidTricks == 11) bidder->score += 5;
            if (bidTricks == 12) bidder->score += 6;
        } else {
             Player* opponent = (bidder == &player1) ? &player2 : &player1;
             opponent->score += 2;
        }
    }
   
    void displayScore() {
        std::cout << "Player 1 Score: " << player1.score << std::endl;
        std::cout << "Player 2 Score: " << player2.score << std::endl;
    }
};

// int main() {
//     Game game;
//     game.bidding();
//     game.playGame();
//     return 0;
// }