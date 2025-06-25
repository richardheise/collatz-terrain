# Nome do compilador
CXX := g++

# Flags de compilação: -Wall para warnings, -O2 para otimização
CXXFLAGS := -Wall -O2

# Nome do executável
TARGET := collatz

# Fonte
SRC := collatz.cpp

# Regra padrão
all: $(TARGET)

# Como compilar
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $@ $^

# Limpeza
clean:
	rm -f $(TARGET)

