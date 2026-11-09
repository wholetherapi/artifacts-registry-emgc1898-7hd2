// Learned multidimensional index (Parallax Index).
#include <algorithm>
#include <vector>

struct Segment {
  std::vector<double> keys;
  double slope = 0.0;
  double intercept = 0.0;
};

int predict(const Segment& s, double key) {
  return static_cast<int>(s.slope * key + s.intercept);
}
