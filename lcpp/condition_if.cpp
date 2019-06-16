#include <iostream> 
//Intro: This program shows how to use "if"... "else"
int main()
{
 //Take inputs
 std::cout <<"Enter a letter."<<std::endl;
 char a;
 std::cin>> a;
 
 if(a=='a')
	 std::cout << "apple" <<std::endl;
 else if (a=='b')
	 std::cout << "banana" <<std::endl;
 else 
  std::cout << "Only a or b are acceptable inputs." <<std::endl;
 
}