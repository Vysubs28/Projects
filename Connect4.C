#include <stdio.h>

char board[8][8];
int x = 0;
int y = 0;

void print() {
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      printf("%c", board[i][j]);
    }
    printf("\n");
  }
}

int checkWin(char player) {
  // Check for horizontal win
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 5; j++) {
      if (board[i][j] == player && board[i][j + 1] == player &&
          board[i][j + 2] == player && board[i][j + 3] == player) {
        return 1;  // Win
      }
    }
  }

  // Check for vertical win
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 8; j++) {
      if (board[i][j] == player && board[i + 1][j] == player &&
          board[i + 2][j] == player && board[i + 3][j] == player) {
        return 1;  // Win
      }
    }
  }

  // Check for diagonal win (from top-left to bottom-right)
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
      if (board[i][j] == player && board[i + 1][j + 1] == player &&
          board[i + 2][j + 2] == player && board[i + 3][j + 3] == player) {
        return 1;  // Win
      }
    }
  }

  // Check for diagonal win (from top-right to bottom-left)
  for (int i = 0; i < 5; i++) {
    for (int j = 3; j < 8; j++) {
      if (board[i][j] == player && board[i + 1][j - 1] == player &&
          board[i + 2][j - 2] == player && board[i + 3][j - 3] == player) {
        return 1;  // Win
      }
    }
  }

  return 0;  // No win
}

int main() {
  for (int i = 0; i < 8; i++)
    for (int j = 0; j < 8; j++)
      board[i][j] = '.';

  int moves = 0;
  char currentPlayer = 'R';

  while (moves < 64) {
    scanf("%d", &y);

    // Alternately place 'R' and 'B' in the lowest position of the indicated column
    for (int i = 7; i >= 0; i--) {
      if (board[i][y] == '.') {
        board[i][y] = currentPlayer;
        break;
      }
    }

    print();

    if (checkWin(currentPlayer)) {
      printf("%s wins!\n", (currentPlayer == 'R') ? "Red" : "Black");
      break;
    }

    currentPlayer = (currentPlayer == 'R') ? 'B' : 'R';
    moves++;
  }

  if (moves == 64) {
    printf("It's a tie!\n");
  }

  return 0;
}
