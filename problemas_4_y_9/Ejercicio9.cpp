#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
cin.tie(nullptr);
int n, x;
cin >> n;
vector<int> p;
while(n--){
    cin >> x;
    p.push_back(x);
}
sort(p.begin(), p.end());
p.erase(unique(p.begin(), p.end()), p.end());
cout << p.size() << endl;
return 0;
}
