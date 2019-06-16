#include <iostream> 
//Intro:

class Car
{
	public:
		void SetNumberOfWheels(int n);
		void SetHorsePower(float h);
		void SetMaxSpeed(float s);

		int GetNumberOfWheels();
		float GetHorsePower();
		float GetMaxSpeed();
        void Describe();
	private:
		int no_of_wheels;
		float hp;
		float mx_speed;
};

void Car::SetNumberOfWheels(int n)
{
	no_of_wheels = n;
}
void Car::SetHorsePower(float hp_in)
{
	hp = hp_in;
}
void Car::SetMaxSpeed(float s)
{
	mx_speed = s;
}

int Car::GetNumberOfWheels()
{
	return no_of_wheels;
}
float Car::GetHorsePower()
{
	return hp;
}
float Car::GetMaxSpeed()
{
	return mx_speed;
}
				
void Car::Describe()
{
  auto n = GetNumberOfWheels();
  auto h = GetHorsePower();
  auto s = GetMaxSpeed(); 
  std::cout << "The number of wheels are " << n << std::endl;
  std::cout << "The horse power is " << h << std::endl;
  std::cout << "The max speed is " << s << std::endl;  
} 
				
int main()
{
 //Take inputs
 std::cout <<"Enter number of wheels."<<std::endl;
 int n=0;
 std::cin >> n;
 
 std::cout <<"Enter horse power." << std::endl;
 float h = 0.0;
 std::cin >> h;
 
 
 std::cout <<"Enter speed." << std::endl;
 float s = 0.0;
 std::cin >> s;

  Car c1;
  c1.SetNumberOfWheels(n);
  c1.SetHorsePower(h);
  c1.SetMaxSpeed(s);  
  std::cout << "We created a car."<< std::endl;  
  c1.Describe();
}
