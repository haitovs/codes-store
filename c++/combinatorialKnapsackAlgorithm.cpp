#include <iostream>
using namespace std;
int n, m, a[100], b[100], c[100], ag, bh, mx, jgag;
string jt, jogt;
int main() {
    // Read the number of items and the weight limit
    cin >> n >> m;

    // Read the weight and value of each item
    for(int i = 1; i <= n; i++) {
        cout << i << " -nji agram: ";
        cin >> a[i];

        cout << i << " -nji baha: ";
        cin >> b[i];
    }

    // Generate all possible combinations of items
    while(c[1] < 2) {
        ag = 0, bh = 0, jt = "";

        // Calculate the total weight and total value for the current combination
        for(int i = 1; i <= n; i++) {
            if(c[i] == 0) {
                ag = ag + a[i];
                bh = bh + b[i];
                jt = jt + to_string(i);
            }
        }

        // Check if the current combination meets the weight limit and has a higher total value than the current maximum
        if(ag < m && bh <= m) {
            mx = bh;
            jgag = ag;
            jogt = jt;
        }

        // Generate the next combination
        a[n]++;
        for(int i = n; i > 1; i--) {
            cout << a[i] << " ";
            if(a[i] > 1) {
                a[i] = 0;
                a[i - 1]++;
            }
        }
        cout << endl;
    }

    // Output the maximum value, the total weight, and the combination of items that achieve this maximum value
    cout << "Jemi Baha: " << mx << endl;
    cout << "Jemi agram: " << jgag << endl;
    cout << "Harytlar: " << jogt << endl;
    return 0;
}
