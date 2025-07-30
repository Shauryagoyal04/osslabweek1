#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int i=1;
    int ans=0;
    int j=2;
    for(int i=1;i<=3;i++){
        int x = n%10;
        n=n/10;
        int ans = ans+(x*pow(10,j));
        j--;
    }
    cout<<ans;
}