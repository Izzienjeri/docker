#include <gtest/gtest.h>
#include <sstream>
#include <iostream>
#include "solution.cpp"  // Include the original game logic

class GameTest : public ::testing::Test {
protected:
    Game game; // Use stack allocation instead of dynamic memory

    void SetUp() override {
        game.currentPlayer = &game.player1;
        std::cout << "[DEBUG] SetUp: Initialized Game instance" << std::endl;
    }
};

// Test Case 1: Valid Card Selection
TEST_F(GameTest, ValidCardSelection) {
   
    game.player1.hand.push_back(Card(HEARTS, TEN));

    std::istringstream input("TH\n");  // Simulate input for Ten of Hearts
    std::streambuf* originalCin = std::cin.rdbuf(input.rdbuf());  // Redirect std::cin

    game.playCard();

    std::cin.rdbuf(originalCin);  // Restore std::cin

    ASSERT_FALSE(game.currentTrick.empty());
    EXPECT_EQ(game.currentTrick.back().rank, TEN);
    EXPECT_EQ(game.currentTrick.back().suit, HEARTS);
    EXPECT_EQ(game.player1.hand.size(), 4);  // The card should be removed

 
}

// Test Case 2: Invalid Card Selection
TEST_F(GameTest, InvalidCardSelection) {
   
    game.player1.hand.push_back(Card(HEARTS, TEN));  // Ensure the player has at least one card

    std::istringstream input("2s\nTH\n");  // First input is invalid, second is valid
    std::streambuf* originalCin = std::cin.rdbuf(input.rdbuf());

    testing::internal::CaptureStdout();
    game.playCard();
    std::string output = testing::internal::GetCapturedStdout();
  
    std::cin.rdbuf(originalCin);  // Restore std::cin

    EXPECT_TRUE(output.find("Invalid card input or card not found.") != std::string::npos);

    
}

// Test Case 3: First Card of Trick - Switch Player
TEST_F(GameTest, FirstCardOfTrickSwitchPlayer) {
  
    game.player1.hand.push_back(Card(HEARTS, TEN));

    std::istringstream input("TH\n");  // Player 1 plays Ten of Hearts
    std::streambuf* originalCin = std::cin.rdbuf(input.rdbuf());
    game.playCard();
    std::cin.rdbuf(originalCin);  // Restore std::cin

    EXPECT_EQ(game.currentPlayer, &game.player2);  // The turn should switch to Player 2

    std::cout << "[DEBUG] Finished FirstCardOfTrickSwitchPlayer Test" << std::endl;
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
