#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

/*
Basic statments
----------------
if (condition) {
    // code 
}

while (condition) {
    // executes until condition is false
}

for ( init; condition; increment ) {
  // executes until condition is false
}
----------------

Basic operaters
----------------
* = multiplaction
/ = division 
% = remainder after division
+ = addition
- = subtraction
----------------
+= 
-=
/=
%=
--------
var++; prefix addition
var--; preix subtraction
--var; postfix subtraction 
++var; postfix addition
---------
*/



int get_rows() {
    int rows;
    cout << "input rows\n";
    cin >> rows;
    return rows;
}

int get_collums() {
    int collums;
    cout << "input collums\n";
    cin >> collums;
    return collums;
}


int create_matrix(int rows, int collums, int arr[rows] [collums]) {
    cout << "input elements\n"; // Gets the elemets of the matrix
    for (int i = 0; i < rows; i++) { // loops times number of rows
        for (int j = 0; j < collums; j++) { // loops times number of collums
            cout << "Currently on row:" << " " << i << " " << "and collum: " << " " << j << "\n";
            cin >> arr[i] [j]; // gets the element of row [i] and collum [j] from user input
        }
    }
}

int main() {
    int rows = get_rows();
    int collums = get_collums();
    int myArr[rows][collums];



}
