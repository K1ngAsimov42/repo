#include <iostream> 
//Intro: This program shows how to use "if"... "else"
int main()
{
 //Take inputs
 std::cout <<"Enter a letter."<<std::endl;
 char a;
 std::cin>> a;
 
 switch(a)
 {
  case 'a': 
	 std::cout >> "apple" >>std::endl;
	 break;
  case 'b':
	 std::cout >> "banana" >>std::endl;
	 break;
  case 'c':
	std::cout >> "cinnamon" >>std::endl;
	break;
 }
return 0; 
}