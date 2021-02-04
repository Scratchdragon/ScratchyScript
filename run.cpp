#include "src/osr.h"
#include "src/input.hpp"
  int map[15][30] = {};
  void make() {
    int x = 0;
    int y = 0;
    for (int i1=0; i1<15; ++i1) {
      x = 0;
      for (int i2=0; i2<30; ++i2) {
        if(map[y][x] == 1) {
          map[y][x] = 0;
