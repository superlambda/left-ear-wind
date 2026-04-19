#include <stdio.h>
#include <string.h>

#define swap(x, y, size) {\
  char temp[size]; \
  memcpy(temp, &y, size); \
  memcpy(&y,   &x, size); \
  memcpy(&x, temp, size); \
}


int main(){
  int a = 1, b = 2;
  swap(a, b, sizeof(int));
  printf("a = %d, b = %d\n", a, b);
  return 0;
}