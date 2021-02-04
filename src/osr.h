#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
void delay(int time) {
  usleep(time * 1000);
}
void print(char* text) {
  std::cout << text;
}
void print(int text) {
  std::cout << text;
}
void print(char text) {
  std::cout << text;
}
void clear(void) {
  system("clear");
}
void seed(int seed = (time(NULL))) {
  srand(seed);
}
int random(int min, int max) {
  return (rand() % (max - (min - 1)) + 1) + (min - 1);
}