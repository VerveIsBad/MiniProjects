#include <cmath>
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;


int get_rows() {
    /*
    Gets the number of rows the user wants in their matrix from input.
    */
    int rows;
    cout << "input rows\n";
    cin >> rows;
    return rows;
}

int get_collums() {
    /*
    Gets the number of collums the user want in their matrix from input.
    */
    int collums;
    cout << "input collums\n";
    cin >> collums;
    return collums;
}

void create_matrix(int rows, int collums) {
    /*
    Creates a matrix given x rows and y collums 
    and then prints the matrix. Does not return it.
    matrix is then deletd
    */
    int arr[rows] [collums];
    cout << "input elements\n"; // Gets the elemets of the matrix
    for (int i = 0; i < rows; i++) { // loops times number of rows
        for (int j = 0; j < collums; j++) { // loops times number of collums
            cout << "Currently on row:" << " " << i << " " << "and collum: " << " " << j << "\n";
            cin >> arr[i] [j]; // gets the element of row [i] and collum [j] from user input
        }
    }
    cout << "Your matrix:\n"; // prints the matrix in a nice manner.
    for (int i = 0; i < rows; i++) {
        cout << "[";
        for (int j = 0; j < collums; j++) {
            if (j == collums-1) {
                cout << arr[i][j];
            } else {
                cout << arr[i][j] << ",";
            }
        }
        cout << "]\n";  
    }
}

void matrix_stuff() {
    /*
    Creates a matrix by calling:
    get_rows()
    get_collums()
    and create_matrix with arr[rows][collums]
    */
    int rows = get_rows();
    int collums = get_collums();
    create_matrix(rows, collums);
}

int add(int a=0, int b=0) {
    /*
    Adds two ints
    */
    return a + b;
}

float add(float a=0.0, float b=0.0) {
    /*
    adds two floats
    */
    return a + b;
}

double add(double a=0.0, double b=0.0) {
    /*
    adds two doubles
    */
    return a + b;
}

void overload() {
    /*
    gets the type of the two numbers to add.
    creates the numbers with said type via console
    stores the result of add(a,b) in "sum" and prints sum
    */
    string input;
    cout << "Input number type (float, int, double)" << endl; // gets num type
    cin >> input;

    if (input == "int") { // creates and add two numbers of given input.
        int a;
        int b;
        cout << "Input two numbers to add\n";
        cin >> a;
        cin >> b;
        int sum;
        sum = add(a,b);
        cout << "Your total of" << " " << a << " " << "and" << " " << b << " " << "is" << " " << sum << endl;
    } else if (input == "float") {
        float a;
        float b;
        cout << "Input two numbers to add\n";
        cin >> a;
        cin >> b;
        float sum = add(a,b);
        cout << "Your total of" << " " << a << " " << "and" << " " << b << " " << "is" << " " << sum << endl;
    } else if (input == "double") {
        double a;
        double b;
        cout << "Input two numbers to add\n";
        cin >> a;
        cin >> b;
        double sum = add(a,b);
        cout << "Your total of" << " " << a << " " << "and" << " " << b << " " << "is" << " " << sum << endl;
    } else {
        cout << "error, please make sure to select from the orginal prompt. (float, int, double)\n";
    }
}

int factorial(int n=0) {
    /*
    Gets the factorial of a given number n
    */
    if (n==1) {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}

void display_array(int arr[], int size) {
    /*
    Displays an array
    */
    cout << "[";
    for (int i = 0; i < size; i++) {
        if (i == (size - 1)) {
            cout << arr[i];
        } else {
            cout << arr[i] << ",";
        }
    }
    cout << "]\n";
}

int main() {
    create_matrix(3,3);
}