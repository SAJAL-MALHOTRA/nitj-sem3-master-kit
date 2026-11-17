#include<iostream>
using namespace std;

class student
{
  string name;
  int age, roll_no;
  string grade;

  public:
  void setname(string s){
    if(s.size()==0){
      cout<<"invalid name"<<endl;
    }
    else{
      name=s;
    }
  }

  void setage(int a){
    if(a<=0){
      cout<<"invalid age"<<endl;
    }
    else{
      age=a;
    }
  }

  void setroll_no(int r){
    if(r<=0){
      cout<<"invalid roll number"<<endl;
    }
    else{
      roll_no=r;
    }
  }

  void setgrade(string g){
    if(g.size()==0){
      cout<<"invalid grade"<<endl;
    }
    else{
      grade=g;
    }
  }

  void getname(){
    cout<<name<<endl;
  }

  void getage(){
    cout<<age<<endl;
  }

  void getroll_no(){
    cout<<roll_no<<endl;
  }

  void getgrade(int pin){
    if(pin!=1234){
      cout<<"invalid pin"<<endl;
    }
    else{
      cout<<grade<<endl;
    }
  }
};

int main(){
  student s1;
  s1.setname("John");
  s1.setage(20);
  s1.setroll_no(101);
  s1.setgrade("A");
  s1.getname();
  s1.getage();
  s1.getroll_no();
  s1.getgrade(1234);
  cout<<endl;
}