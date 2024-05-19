#include <stdio.h>
#include <time.h>

void loop_asm(int count) {
  asm volatile(
    "mov %%edi, %%ecx\n"  
    "loop:\n"             
      "dec %%ecx\n"         
      "jnz loop\n"            
    :                      
    : "A" (count)            
    : "ecx"                 
  );
}

int main() {
  clock_t start = clock();  
  int count = 200000000; // 200 million
  loop_asm(count);
  printf("Loop finished.\n");

  clock_t end = clock();
  double elapsedMilliseconds = ((double) (end - start) * 1000) / CLOCKS_PER_SEC;
  printf("Time taken: %.20f milliseconds\n", elapsedMilliseconds);
  return 0;
}