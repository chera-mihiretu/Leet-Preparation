#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> kmp(string s,int m){
        int n = s.length();
        vector<int> lps(n+1,0);
        for(int i=1;i<n;i++){
            int prev = lps[i-1];
            while(prev>0&&s[i]!=s[prev]){
                prev = lps[prev-1];
            }
            lps[i] = prev+(s[i]==s[prev]);
        }
        return lps;
    }
    int shortestMatchingSubstring(string s, string p) {
        int n = s.length();
        int m = p.length();
        if(m==2){
            return 0;
        }
        vector<int> v;
        for(int i=0;i<m;i++){
            if(p[i]=='*'){
                v.push_back(i);
            }
        }
        string a,b,c;
        a = p.substr(0,v[0]);
        b = p.substr(v[0]+1,v[1]-v[0]-1);
        c = p.substr(v[1]+1,m-(v[1])-1);
        // cout<<a<<" "<<b<<" "<<c<<endl;
        int na = a.size();
        int nb = b.size();
        int nc = c.size();
        vector<int> v1 = kmp(a+'#'+s,na);
        vector<int> v2 = kmp(b+'#'+s,nb);
        vector<int> v3 = kmp(c+'#'+s,nc);
        
        
        v1 = vector<int>(v1.begin()+na+1,v1.end());
        v2 = vector<int>(v2.begin()+nb+1,v2.end());
        v3 = vector<int>(v3.begin()+nc+1,v3.end());
        int res = INT_MAX;
        int i=0,j=0,k=0;
        while(i+nb+nc<v1.size()){
            while(i<v1.size()&&v1[i]!=na){
                i++;
            }
            if(i>=v1.size()) break;
            while(j<v2.size()&&(j<i+nb||v2[j]!=nb)){
                j++;
            }
            if(j>=v2.size()) break;
            while(k<v3.size()&&(k<j+nc||v3[k]!=nc)){
                k++;
            }
            if(k>=v3.size()) break;
            res = min(res,k-i+na);
            i++;
        }
        return res==INT_MAX?-1:res;
    }
};


int main (){
    Solution *s = new Solution();

    cout << s->shortestMatchingSubstring("abaacbaecebce", "ba*c*ce") << endl;
}