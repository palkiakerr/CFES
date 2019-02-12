#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <getopt.h>
using namespace std;

void print_usage() {
  cout << "Usage: ./temperature -c <temp> | temp -f <temp>" << endl;
  exit(2);
}

void print_fahrenheit(float temp) {
  float f = ((temp*9)/5)+32;
  cout << temp <<  " centigrade is " << f << " fahrenheit" << endl;
}

void print_centigrade(float temp) {
  float c = ((temp-32)*5)/9;
  cout << temp << " fahrenheit is " << c << " centigrade" << endl;
}

int main(int argc, char **argv) {

  cout << fixed;
  cout << setprecision(2);

  if (argc < 2) {
    print_usage();
  }

  int option;
  int cflag=0;
  int fflag=0;
  while ((option = getopt(argc, argv, "c:f:")) != -1) {
    switch (option) {
    case 'c' : 
      if (cflag) {
	print_usage();
      } else {
	cflag++;
	fflag++;
      }
      print_fahrenheit(atof(optarg));
      break;
    case 'f' :
      if (fflag) {
	print_usage();
      } else {
	cflag++;
	fflag++;
      }
      print_centigrade(atof(optarg));
      break;
    default :
      cout << "Error" << endl;
    }
  }

  return 0;
}
