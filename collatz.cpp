#include <cstdlib>
#include <iostream>

using namespace std;

unsigned long long round_to_granularity(unsigned long long value, long granularity) {
    if (granularity <= 1) return value; // Sem arredondamento se granularidade <= 1
    return (value + granularity/2) / granularity * granularity;
}

int main(int argc, char *argv[]) {
    if (argc < 3 || argc > 4) {
        cerr << "Uso: " << argv[0] 
             << " <seed> <steps> [granularity]. Granularity is optional, default is 5" 
             << endl;
        return 1;
    }

    unsigned long long seed = strtoull(argv[1], nullptr, 10);
    unsigned long long steps = strtoull(argv[2], nullptr, 10);
    long granularity = 5;

    if (argc == 4) {
        granularity = strtol(argv[3], nullptr, 10);
        if (granularity <= 0) {
            cerr << "Granularity must be a positive integer" << endl;
            return 1;
        }
    }

    unsigned long long i = 0;
    unsigned long long last_rounded = round_to_granularity(seed, granularity);
    cout << last_rounded << " " << i << endl;

    while (steps-- > 0 && seed > 1) {
        if (seed % 2 == 0) {
            seed /= 2;
        } else {
            seed = seed * 3 + 1;
        }
        i++;

        unsigned long long rounded = round_to_granularity(seed, granularity);
        if (rounded != last_rounded) {
            cout << rounded << " " << i << endl;
            last_rounded = rounded;
        }
    }

    // Imprime o último valor se for diferente, mesmo que não mude o arredondamento
    if (seed > 0 && seed != last_rounded / granularity * granularity) {
        cout << round_to_granularity(seed, granularity) << " " << i << endl;
    }

    return 0;
}
