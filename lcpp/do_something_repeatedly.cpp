#include <iostream> 
//Intro:
int main()
{
 //Take inputs
 std::cout <<"Enter a sentence to be printed."<<std::endl;
 std::string words;
 getline (std::cin, words);
 
 std::cout <<"How many times do you want to print it?"<<std::endl;
 int num = 0;
 std::cin >> num;
 
 //print repeatedly 
 for ( int i = 0 ; i < num ;++i)
 {
	 std::cout <<  words << std::endl;
 }
}
