/*
 * author: mwleeds
 * purpose: solve the Grid problem from the 2015 ACM ICPC Southeast D1 Programming Contest
 */

#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>

typedef struct move {
  int i; // row
  int j; // column
  int count; // moves so far
} move;

using namespace std;

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

  // record whether squares have been visited in the search
  bool** visited = new bool*[n];
  for (int i = 0; i < n; ++i) {
    visited[i] = new bool[m];
  }

  // initialize visited to false
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      visited[i][j] = false;
    }
  }

  // initialize a queue of moves
  vector<move> moves_queue;
  move first_move = {0, 0, 0};
  moves_queue.push_back(first_move);

  // do a BFS of the grid
  int result = -1;
  while (!moves_queue.empty()) {
    move the_move = moves_queue.front();
    if (the_move.i == n - 1 && the_move.j == m - 1) {
      result = the_move.count;
      break;
    }
    
    int i = the_move.i;
    int j = the_move.j;
    int c = the_move.count + 1;
    int d = grid[i][j];

    moves_queue.erase(moves_queue.begin());

    if (i + d < n && !visited[i+d][j]) { // try moving down
      visited[i+d][j] = true;
      move new_move = {i+d, j, c};
      moves_queue.push_back(new_move);
    }
    if (i - d >= 0 && !visited[i-d][j]) { // try moving up
      visited[i-d][j] = true;
      move new_move = {i-d, j, c};
      moves_queue.push_back(new_move);
    }
    if (j + d < m && !visited[i][j+d]) { // try moving right
      visited[i][j+d] = true;
      move new_move = {i, j+d, c};
      moves_queue.push_back(new_move);
    }
    if (j - d >= 0 && !visited[i][j-d]) { // try moving left
      visited[i][j-d] = true;
      move new_move = {i, j-d, c};
      moves_queue.push_back(new_move);
    }
  }

  cout << result << endl;

  // free the memory that was allocated
  for (int i = 0; i < n; ++i) {
    delete[] grid[i];
    delete[] visited[i];
  }
  delete[] grid;
  delete[] visited;
  return 0;
}

