/*
 * author: mwleeds
 * purpose: solve the Grid problem from the 2015 ACM ICPC Southeast D1 Programming Contest
 */

#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

void check_adjacent(int** grid, int** moves, int i, int j, int n, int m);

int main() {
  // get the grid's dimensions from stdin
  int n;
  cin >> n;
  int m;
  cin >> m;
  //
  // allocate memory for the grid
  int** grid = new int*[n];
  for (int i = 0; i < n; ++i) {
    grid[i] = new int[m];
  }

  // get values (0-9) from stdin to fill the grid
  for (int i = 0; i < n; ++i) {
    string input;
    cin >> input;
    for (int j = 0; j < m; ++j) {
      grid[i][j] = input[j] - '0'; // convert char to int
    }
  }

  /* print out the grid
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      cout << grid[i][j] << " ";
    }
    cout << endl;
  }*/

  // allocate memory for a secondary grid to hold partial numbers of moves
  int** moves = new int*[n];
  for (int i = 0; i < n; ++i) {
    moves[i] = new int[m];
  }

  // initialize the moves grid with a number higher than the maximum possible number of moves
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      moves[i][j] = n + m;
    }
  }
  moves[0][0] = 0; // start at the top-left

  // traverse grid, updating moves as we go
  check_adjacent(grid, moves, 0, 0, n, m);
    
  // check the value in the bottom-right corner to conclude the shortest path
  if (moves[n-1][m-1] == n + m) {
    cout << "-1" << endl;
  } else {
    cout << moves[n-1][m-1] << endl;
  }

  // free the memory that was allocated
  for (int i = 0; i < n; ++i) {
    delete[] grid[i];
    delete[] moves[i];
  }
  delete[] grid;
  delete[] moves;
  return 0;
}

void check_adjacent(int** grid, int** moves, int i, int j, int n, int m) {
  if (i + grid[i][j] < n) { // try moving down
    int new_i = i + grid[i][j];
    if (moves[i][j] + 1 < moves[new_i][j]) { // found a faster route
      moves[new_i][j] = moves[i][j] + 1;
      // recursively check all paths from that square
      check_adjacent(grid, moves, new_i, j, n, m);
    }
  }
  if (i - grid[i][j] >= 0) { // try moving up
    int new_i = i - grid[i][j];
    if (moves[i][j] + 1 < moves[new_i][j]) {
      moves[new_i][j] = moves[i][j] + 1;
      check_adjacent(grid, moves, new_i, j, n, m);
    }
  }
  if (j + grid[i][j] < m) { // try moving right
    int new_j = j + grid[i][j];
    if (moves[i][j] + 1 < moves[i][new_j]) {
      moves[i][new_j] = moves[i][j] + 1;
      check_adjacent(grid, moves, i, new_j, n, m);
    }
  }
  if (j - grid[j][j] >= 0) { // try moving left
    int new_j = j - grid[i][j];
    if (moves[i][j] + 1 < moves[i][new_j]) {
      moves[i][new_j] = moves[i][j] + 1;
      check_adjacent(grid, moves, i, new_j, n, m);
    }
  }
}
