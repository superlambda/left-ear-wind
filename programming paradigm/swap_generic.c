#include <stdio.h>
#include <string.h>

void swap(void* x, void* y, size_t size)
{
     char tmp[size];
     memcpy(tmp, y, size);
     memcpy(y, x, size);
     memcpy(x, tmp, size);
}

int main(){
  int a = 1, b = 2;
  swap(&a, &b, sizeof(int));
  printf("a = %d, b = %d\n", a, b);
  return 0;
}

