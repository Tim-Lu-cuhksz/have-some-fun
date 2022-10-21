#ifndef TICTACTOE_H
#define TICTACTOE_H
#include "grid.h"
#include "vector.h"
#include "set.h"

#include "testing/SimpleTest.h"

enum Player {
    COMPUTER,
    HUMAN,
};

enum Outcome { HUMAN_WINS, COMPUTER_WINS, CATS_GAME };

class TicTacToe
{
private:
    /* Instance variables */
    Player whoseTurn;
    Grid<char> board;
    Set<int> position;
    Outcome outcome;

    /* Methods */

    // Initialize table
    void setUpTable();

    // Get move from user or computer
    int getUserMove();
    int getComputerMove();

    // Display current board
    void displayBoard();

    // Return opponent
    Player opponent(Player player);

    // Change the move into coordinate
    Vector<int> changeToCor(int move);

    // Check whether the player wins the game
    bool checkWin(Player player);
    bool gameIsOver();

    // Check whether row, column or diagonal satisfies wining
    bool rowWin(int row, char mark);
    bool columnWin(int col, char mark);
    bool diagWin(char mark);

    void makeMove(int move);
    void retractMove(int move);

    // Find best move using minimax algorithm
    int findBestMove();
    int findBestMove(int depth, int & rating);
    int evaluatePosition(int depth);

    // Evaluate rating in current player's perspective
    int evaluateStaticPosition();
    void generateMoveList(Vector<int> & movelist);

public:
    TicTacToe();
    // Print game table.
    void printTable();
    // Play the game.
    void play();
    // Print game intructions.
    void printInstructions();
};


#endif // TICTACTOE_H
