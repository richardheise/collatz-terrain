#include <cstdlib> // Para atoi()
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  if (argc != 3) {
    cerr << "Uso: " << argv[0] << " <seed> <steps>" << endl;
    return 1;
  }

  unsigned long long seed = strtoull(argv[1], nullptr, 10);
  unsigned long long steps = strtoull(argv[2], nullptr, 10);

  unsigned long long i = 0;
  while (steps-- > 0 && seed > 1) {
    if (seed % 2 == 0) {
      seed /= 2;
    } else {
      seed = seed * 3 + 1;
    }

    i += 1;
    cout << seed << " " << i << endl;
  }

  return 0;
}
