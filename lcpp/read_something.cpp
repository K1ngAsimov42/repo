#include <iostream> 
//reading (or taking input)  number.
//Intro: This program takes two number as input and prints sum of those numbers. 
int main()
{
 std::cout <<"Input a number"<<std::endl;
 int i =0;
 std::cin >> i;
 std::cout <<"Input the other number"<<std::endl;
 int j =0;
 std::cin >> j;
 std::cout <<"The sum is: " << i + j << std::endl;
}