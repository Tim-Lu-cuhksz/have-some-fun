#include "tictactoe.h"
#include <iostream>
#include "error.h"
#include "simpio.h"
#include "console.h"
using namespace std;

/* Constants */
const char COMPUTER_MOVE = 'X';
const char HUMAN_MOVE = 'O';
const char BLANK = ' ';
const Player INITIAL_PLYAER = COMPUTER;

const int N_POS = 9;
const int DIMENSION = 3;
const int MAX_DEPTH = DIMENSION * DIMENSION;

const int WINNING_POSITION = 1000;
const int NEUTRAL_POSITION = 0;
const int LOSING_POSITION = -WINNING_POSITION;

TicTacToe::TicTacToe()
{
    board.resize(DIMENSION, DIMENSION);
    setUpTable();
}

void TicTacToe::play() {
    whoseTurn = INITIAL_PLYAER;
    while (true) {
        int move;
        // Player's move

        if (whoseTurn == HUMAN) {
            cout << "Your move." << endl;
            move = getUserMove();
        } else {
            // The first move goes to 1.
            if (position.size() == 9) move = 1;
            else move = getComputerMove();
        }

        makeMove(move);
        if (whoseTurn == COMPUTER) cout << endl << "I'll move to " << move << "." << endl;

        cout << "The game now looks like this:" << endl << endl;
        displayBoard();
        cout << endl;

        if (gameIsOver()) {
            cout << "The final position looks like this:" << endl << endl;
            displayBoard();
            cout << endl;
            if (outcome == COMPUTER_WINS) cout << "I win." << endl;
            else if (outcome == HUMAN_WINS) cout << "YOU WIN! CONGRATULATIONS!" << endl;
            else cout << "It's a cat's game." << endl;
            break;
        }
        whoseTurn = opponent(whoseTurn);
    }
}

void TicTacToe::printInstructions() {
    cout << "Welcome to TicTacToe, the game of three in a row." << endl;
    cout << "I'll be X and you'll be O." << endl;
    cout << "The squares are numbered like this:" << endl << endl;
}

void TicTacToe::printTable() {
    cout << " " << 1 << " | " << 2 << " | " << 3 << endl;
    cout << "---+---+---" << endl;
    cout << " " << 4 << " | " << 5 << " | " << 6 << endl;
    cout << "---+---+---" << endl;
    cout << " " << 7 << " | " << 8 << " | " << 9 << endl;
}

void TicTacToe::displayBoard() {
   for (int i = 0; i < DIMENSION; i++) {
      if (i != 0) cout << "---+---+---" << endl;
      for (int j = 0; j < DIMENSION; j++) {
         if (j != 0) cout << "|";
         cout << " " << board[i][j] << " ";
      }
      cout << endl;
   }
   cout << endl;
}

void TicTacToe::setUpTable() {
    for (int i = 0; i < DIMENSION; i++) {
        for (int j = 0; j < DIMENSION; j++) {
            board[i][j] = BLANK;
        }
    }
    for (int i = 1; i <= N_POS; i++) {
        position.add(i);
    }
}

int TicTacToe::getUserMove() {
    while (true) {
        int num = getInteger("What square?");
        if (position.contains(num)) return num;
    }
}

Vector<int> TicTacToe::changeToCor(int move) {
    Vector<int> cor(2);
    for (int i = 0; i < DIMENSION; i++) {
        for (int j = 0; j < DIMENSION; j++) {
            move--;
            if (move == 0) {
                cor[0] = i;
                cor[1] = j;
                return cor;
            }
        }
    }
    error("Invalid move!");
}

Player TicTacToe::opponent(Player player) {
    return (player == HUMAN) ? COMPUTER : HUMAN;
}

bool TicTacToe::checkWin(Player player) {
    char mark;
    mark = (player == HUMAN) ? HUMAN_MOVE : COMPUTER_MOVE;
    for (int i = 0; i < DIMENSION; i++) {
        if (rowWin(i, mark)) return true;
    }
    for (int j = 0; j < DIMENSION; j++) {
        if (columnWin(j, mark)) return true;
    }
    if (diagWin(mark)) return true;
    return false;
}

bool TicTacToe::gameIsOver() {
    if (checkWin(HUMAN)) {
        outcome = HUMAN_WINS;
        return true;
    }
    if (checkWin(COMPUTER)) {
        outcome = COMPUTER_WINS;
        return true;
    }
    if (position.isEmpty()) {
        outcome = CATS_GAME;
        return true;
    }
    return false;
}

bool TicTacToe::rowWin(int row, char mark) {
    for (int j = 0; j < DIMENSION; j++) {
        if (board[row][j] != mark) return false;
    }
    return true;
}

bool TicTacToe::columnWin(int col, char mark) {
    for (int i = 0; i < DIMENSION; i++) {
        if (board[i][col] != mark) return false;
    }
    return true;
}

bool TicTacToe::diagWin(char mark) {
    bool diagnal1 = true;
    bool diagnal2 = true;
    for (int i = 0; i < DIMENSION; i++) {
        if (board[i][i] != mark) diagnal1 = false;
    }
    for (int j = 0; j < DIMENSION; j++) {
        if (board[2-j][j] != mark) diagnal2 = false;
    }
    return diagnal1 || diagnal2;
}

void TicTacToe::makeMove(int move) {
    Vector<int> cor(2);
    cor = changeToCor(move);
    switch (whoseTurn) {
    case HUMAN: board[cor[0]][cor[1]] = HUMAN_MOVE; break;
    case COMPUTER: board[cor[0]][cor[1]] = COMPUTER_MOVE; break;
    }
    position.remove(move);
}

void TicTacToe::retractMove(int move) {
    Vector<int> cor(2);
    cor = changeToCor(move);
    board[cor[0]][cor[1]] = BLANK;
    position.add(move);
}

int TicTacToe::getComputerMove() {
    return findBestMove();
}

int TicTacToe::findBestMove() {
    int rating;
    return findBestMove(0, rating);
}

void TicTacToe::generateMoveList(Vector<int> & movelist) {
    if (position.isEmpty()) return;

    for(int pos : position) {
        movelist.add(pos);
    }
}

int TicTacToe::findBestMove(int depth, int & rating) {
    Vector<int> moveList;
    generateMoveList(moveList);
    if (moveList.isEmpty()) error("No moves are available!!!");

    int bestMove;
    int minRating = WINNING_POSITION + 1;

    for (int currentMove : moveList) {
        makeMove(currentMove);
        whoseTurn = opponent(whoseTurn);

        // Evaluate in opponent's perspective
        int moveRating = evaluatePosition(depth + 1);

        if (moveRating < minRating) {
            bestMove = currentMove;
            minRating = moveRating;
        }

        whoseTurn = opponent(whoseTurn);
        retractMove(currentMove);
    }
    rating = -minRating;
    return bestMove;
}

int TicTacToe::evaluatePosition(int depth) {
    if (gameIsOver() || depth >= MAX_DEPTH) {
        return evaluateStaticPosition();
    }
    int rating;
    findBestMove(depth, rating);
    return rating;
}

int TicTacToe::evaluateStaticPosition() {
    Player oPlayer = opponent(whoseTurn);
    if (checkWin(oPlayer)) return LOSING_POSITION;

    if (position.isEmpty()) return NEUTRAL_POSITION;

    return WINNING_POSITION;
}

PROVIDED_TEST("tic tac toe", TTT) {
    TicTacToe game;
    game.printInstructions();
    game.printTable();
    game.play();
}

