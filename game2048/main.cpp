#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <thread>

using namespace std;

/* Constant */
int const DIMENSION = 4;

/* Global variable */
int static score = 0;

/* Function Prototype */
void printInstruction();
void initTable(int table[][DIMENSION]);
void printTable(int table[][DIMENSION]);
bool gameOver(int table[][DIMENSION]);
void nextStage(int table[][DIMENSION]);

bool moveUp(int table[][DIMENSION]);
bool moveDown(int table[][DIMENSION]);
bool moveLeft(int table[][DIMENSION]);
bool moveRight(int table[][DIMENSION]);

void upCheck(int const table[][DIMENSION],
             int &zero,int &num, int col, bool &flag);

void downCheck(int const table[][DIMENSION],
               int &zero,int &num, int col, bool &flag);

void leftCheck(int const table[][DIMENSION],
               int &zero,int &num, int row, bool &flag);

void rightCheck(int const table[][DIMENSION],
                int &zero,int &num, int row, bool &flag);

/* Main function */
int main()
{
    int table[DIMENSION][DIMENSION]
            = {{0,4,0,0},
               {0,0,2,0},
               {0,0,0,0},
               {0,0,0,0}};

    printInstruction();
    initTable(table);
    cout << "The initial state is shown as follows." << endl;
    cout << endl;
    printTable(table);
    cout << endl;
    if (gameOver(table)) cout << "game over." << endl;

    string s;
    bool movable;
    while (true) {
        cout << "Enter your move: ";
        while (true) {
            cin >> s;
            if (s[0] == 'w') {
                movable = moveUp(table);
                break;
            }
            else if (s[0] == 's') {
                movable = moveDown(table);
                break;
            }
            else if (s[0] == 'a') {
                movable = moveLeft(table);
                break;
            }
            else if (s[0] == 'd') {
                movable = moveRight(table);
                break;
            }
            else {
                cout << "Invalid input! Enter agian: ";
            }
        }
        if (!movable) continue;
        nextStage(table);
        cout << endl;
        printTable(table);
        cout << "Scores: " << score << endl << endl;

        if (gameOver(table)) {
            cout << "Game over! See u next time!!!" << endl;
            break;
        }
    }   

    return 0;
}

/* Implementation details */
void initTable(int table[][DIMENSION]) {
    for (int row = 0; row < DIMENSION; row++) {
        for (int col = 0; col < DIMENSION; col++) {
            table[row][col] = 0;
        }
    }
    /* Generate "2" at random position */
    int r1 = 0; int c1 = 0;
    int r2 = 0; int c2 = 0;
    srand(time(0));
    r1 = rand() % DIMENSION; c1 = rand() % DIMENSION;
    r2 = rand() % DIMENSION; c2 = rand() % DIMENSION;
    while ((r1 == r2) && (c1 == c2)) {
        r2 = rand() % DIMENSION;
        c2 = rand() % DIMENSION;
    }
    table[r1][c1] = 2;
    table[r2][c2] = 2;
}

void printTable(int table[][DIMENSION]) {
    cout << left; // left aligned the number
    for (int row = 0; row < DIMENSION; row++) {
        for (int col = 0; col < DIMENSION; col++) {
            if (table[row][col] != 0){
               cout << setw(4) << table[row][col] << " | ";
            } else {
                cout << setw(4) << " " << " | ";
            }
        }
        cout << endl;
        cout << "-----+------+------+------+";
        cout << endl;
    }
}

bool gameOver(int table[][DIMENSION]) {
    // Check empty space
    for (int row = 0; row < DIMENSION; row++) {
        for (int col = 0; col < DIMENSION; col++) {
            if (table[row][col] == 0) return false;
            if (col < DIMENSION - 1 &&
                    table[row][col] == table[row][col+1])
            {return false;}
            if (row < DIMENSION - 1 &&
                    table[row][col] == table[row+1][col])
            {return false;}
        }
    }
    return true;
}

void printInstruction() {
    cout << "Welcome to the game of 2048!!!" << endl;
    cout << "You can use w,s,a,d for UP, DOWN, LEFT, RIGHT move.";
    cout << endl << endl;
}

bool moveUp(int table[][DIMENSION]) {
    bool movable = false;
    for (int col=0; col<DIMENSION; col++) {
        // return the index of zero
        int zero_index;
        // return the index of first non-zero num
        int num_index;
        // true if we can move, otherwise cannot
        bool flag;
        while (true) {
            upCheck(table, zero_index, num_index, col, flag);
            if (!flag) break;
            table[zero_index][col] = table[num_index][col];
            table[num_index][col] = 0;
            movable = true;
        }
        /* Merge process */
        for (int row=0; row<DIMENSION-1; row++) {
            if (table[row][col] == table[row+1][col] &&
                    table[row][col] != 0) {
                int sum = 2 * table[row][col];
                table[row][col] = sum;
                score += sum;
                table[row+1][col] = 0;
                movable = true;
            }
        }
        // Reorder again
        while (true) {
            upCheck(table, zero_index, num_index, col, flag);
            if (!flag) break;
            table[zero_index][col] = table[num_index][col];
            table[num_index][col] = 0;
        }

    }
    return movable;
}

void upCheck(int const table[][DIMENSION],int &zero,
             int &num, int col, bool &flag){
    int zero_index_1st = -1;
    int num_after_zero = -1;
    bool flagt = false;

    for (int row=0; row<DIMENSION; row++) {
        if (table[row][col]==0) {
            zero_index_1st = row;
            break;
        }
    }
    for (int row=zero_index_1st+1; row<DIMENSION; row++) {
        if (table[row][col]!=0) {
            num_after_zero = row;
            break;
        }
    }

    if (zero_index_1st != -1 && num_after_zero != -1) {
        flagt = true;
    }
    zero = zero_index_1st;
    num = num_after_zero;
    flag = flagt;
}

bool moveDown(int table[][DIMENSION]) {
    bool movable = false;
    for (int col=0; col<DIMENSION; col++) {
        // return the index of zero
        int zero_index;
        // return the index of first non-zero num
        int num_index;
        // true if we can move, otherwise cannot
        bool flag;
        while (true) {
            downCheck(table, zero_index, num_index, col, flag);
            if (!flag) break;
            table[zero_index][col] = table[num_index][col];
            table[num_index][col] = 0;
            movable = true;
        }
        //printTable(table);
        /* Merge process */
        for (int row=DIMENSION-1; row>0; row--) {
            if (table[row][col] == table[row-1][col] &&
                    table[row][col] != 0) {
                int sum = 2 * table[row][col];
                table[row][col] = sum;
                score += sum;
                table[row-1][col] = 0;
                movable = true;
            }
        }
        //printTable(table);
        // Reorder again
        while (true) {
            downCheck(table, zero_index, num_index, col, flag);
            if (!flag) break;
            table[zero_index][col] = table[num_index][col];
            table[num_index][col] = 0;
        }
    }
    return movable;
}

void downCheck(int const table[][DIMENSION],int &zero,
             int &num, int col, bool &flag){
    int zero_index_1st = DIMENSION;
    int num_after_zero = DIMENSION;
    bool flagt = false;

    for (int row=DIMENSION-1; row>=0; row--) {
        if (table[row][col]==0) {
            zero_index_1st = row;
            break;
        }
    }
    for (int row=zero_index_1st-1; row>=0; row--) {
        if (table[row][col]!=0) {
            num_after_zero = row;
            break;
        }
    }

    if (zero_index_1st != DIMENSION &&
            num_after_zero != DIMENSION) {
        flagt = true;
    }
    zero = zero_index_1st;
    num = num_after_zero;
    flag = flagt;
}

bool moveRight(int table[][DIMENSION]) {
    bool movable = false;
    for (int row=0; row<DIMENSION; row++) {
        // return the index of zero
        int zero_index;
        // return the index of first non-zero num
        int num_index;
        // true if we can move, otherwise cannot
        bool flag;
        while (true) {
            rightCheck(table, zero_index, num_index, row, flag);
            if (!flag) break;
            table[row][zero_index] = table[row][num_index];
            table[row][num_index] = 0;
            movable = true;
        }
        //printTable(table);
        /* Merge process */
        for (int col=DIMENSION-1; col>0; col--) {
            if (table[row][col] == table[row][col-1] &&
                    table[row][col] != 0) {
                int sum = 2 * table[row][col];
                table[row][col] = sum;
                score += sum;
                table[row][col-1] = 0;
                movable = true;
            }
        }
        //printTable(table);
        // Reorder again
        while (true) {
            rightCheck(table, zero_index, num_index, row, flag);
            if (!flag) break;
            table[row][zero_index] = table[row][num_index];
            table[row][num_index] = 0;
        }
    }
    return movable;
}

void rightCheck(int const table[][DIMENSION],int &zero,
             int &num, int row, bool &flag){
    int zero_index_1st = DIMENSION;
    int num_after_zero = DIMENSION;
    bool flagt = false;

    for (int col=DIMENSION-1; col>=0; col--) {
        if (table[row][col]==0) {
            zero_index_1st = col;
            break;
        }
    }
    for (int col=zero_index_1st-1; col>=0; col--) {
        if (table[row][col]!=0) {
            num_after_zero = col;
            break;
        }
    }

    if (zero_index_1st != DIMENSION &&
            num_after_zero != DIMENSION) {
        flagt = true;
    }
    zero = zero_index_1st;
    num = num_after_zero;
    flag = flagt;
}

bool moveLeft(int table[][DIMENSION]) {
    bool movable = false;
    for (int row=0; row<DIMENSION; row++) {
        // return the index of zero
        int zero_index;
        // return the index of first non-zero num
        int num_index;
        // true if we can move, otherwise cannot
        bool flag;
        while (true) {
            leftCheck(table, zero_index, num_index, row, flag);
            if (!flag) break;
            table[row][zero_index] = table[row][num_index];
            table[row][num_index] = 0;
            movable = true;
        }
        //printTable(table);
        /* Merge process */
        for (int col=0; col<DIMENSION-1; col++) {
            if (table[row][col] == table[row][col+1] &&
                    table[row][col] != 0) {
                int sum = 2 * table[row][col];
                table[row][col] = sum;
                score += sum;
                table[row][col+1] = 0;
                movable = true;
            }
        }
        //printTable(table);
        // Reorder again
        while (true) {
            leftCheck(table, zero_index, num_index, row, flag);
            if (!flag) break;
            table[row][zero_index] = table[row][num_index];
            table[row][num_index] = 0;
        }
    }
    return movable;
}

void leftCheck(int const table[][DIMENSION],int &zero,
             int &num, int row, bool &flag){
    int zero_index_1st = -1;
    int num_after_zero = -1;
    bool flagt = false;

    for (int col=0; col<DIMENSION; col++) {
        if (table[row][col]==0) {
            zero_index_1st = col;
            break;
        }
    }
    for (int col=zero_index_1st+1; col<DIMENSION; col++) {
        if (table[row][col]!=0) {
            num_after_zero = col;
            break;
        }
    }

    if (zero_index_1st != -1 && num_after_zero != -1) {
        flagt = true;
    }
    zero = zero_index_1st;
    num = num_after_zero;
    flag = flagt;
}

void nextStage(int table[][DIMENSION]) {
    int row, col, rand_num;
    srand(time(0));
    row = rand() % DIMENSION;
    col = rand() % DIMENSION;
    rand_num = rand() % 100;
    while (table[row][col] != 0) {
        row = rand() % DIMENSION;
        col = rand() % DIMENSION;
    }
    if (score < 2048) {
        if (rand_num < 95) table[row][col] = 2;
        else table[row][col] = 4;
    } else {
        if (rand_num < 90) table[row][col] = 2;
        else table[row][col] = 4;
    }
}
