#include <iostream>
using namespace std;
struct DataStruct {
    int num;
    float val;
};

class DataClass {
    int num;
    float val;
};

int main() {
    DataStruct s;//  Struct members are public by default
    s.num = 10;   
    s.val = 3.14;

    DataClass c;
    // c.num = 10 will throw COMPILE ERROR: 'num' is private within this context of DataClass
    // c.val = 3.14f will throw COMPILE ERROR: 'val' is private within this context of DataClass
    return 0;
}
