#include <cstdlib>
#include <iostream>

using namespace std;

unsigned long long round_to_granularity(unsigned long long value,
                                        long granularity,
                                        unsigned long long floor_value) {
  if (granularity <= 1)
    return value; // Sem arredondamento se granularidade <= 1
  value = (value < floor_value) ? floor_value : value; // Apply floor
  return (value + granularity / 2) / granularity * granularity;
}

int main(int argc, char *argv[]) {
  if (argc < 3 || argc > 5) {
    cerr << "Uso: " << argv[0]
         << " <seed> <steps> [granularity] [floor]. Both granularity and floor "
            "are optional, defaults are 5 and 4 respectively"
         << endl;
    return 1;
  }

  unsigned long long seed = strtoull(argv[1], nullptr, 10);
  unsigned long long steps = strtoull(argv[2], nullptr, 10);
  long granularity = 5;
  unsigned long long floor_value = 4;

  if (argc >= 4) {
    granularity = strtol(argv[3], nullptr, 10);
    if (granularity <= 0) {
      cerr << "Granularity must be a positive integer" << endl;
      return 1;
    }
  }

  if (argc >= 5) {
    floor_value = strtoull(argv[4], nullptr, 10);
  }

  unsigned long long i = 0;
  unsigned long long last_rounded =
      round_to_granularity(seed, granularity, floor_value);
  cout << last_rounded << " " << i << endl;

  while (steps-- > 0 && seed > 1) {
    if (seed % 2 == 0) {
      seed /= 2;
    } else {
      seed = seed * 3 + 1;
    }
    i++;

    unsigned long long rounded =
        round_to_granularity(seed, granularity, floor_value);
    if (rounded != last_rounded) {
      cout << rounded << " " << i << endl;
      last_rounded = rounded;
    }
  }

  // Imprime o último valor se for diferente, mesmo que não mude o
  // arredondamento
  if (seed > 0 && seed != last_rounded / granularity * granularity) {
    cout << round_to_granularity(seed, granularity, floor_value) << " " << i
         << endl;
  }

  return 0;
}
