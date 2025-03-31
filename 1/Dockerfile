
# Use an official GCC image
FROM gcc:latest

# Install necessary packages, including CMake and git
RUN apt-get update && apt-get install -y cmake git

# Clone Google Test repository
RUN git clone https://github.com/google/googletest.git /googletest

# Build Google Test and Google Mock
RUN cd /googletest && \
    cmake -DCMAKE_CXX_STANDARD=14 CMakeLists.txt && \
    make && \
    make install

# Set the working directory inside the container
WORKDIR /app

# Copy all source files to the container
COPY . .

# Build the solution and unit test executables
# Specify C++14 standard for compilation
RUN g++ -std=c++14 -o eval eval.cpp -lgtest -lgtest_main -pthread

# Run the unit tests
CMD ["/bin/bash", "run.sh"]

