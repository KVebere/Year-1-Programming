//import 'dart:math';

//y = 3x + 2

// void main() {
//   double y = getY(45);
//   print(y.toStringAsFixed(2));
// }

void main() {
  print("X | y");
  for (double i = -10; i <= 10; i += .5) {
    double y = getY(i);
    print("${i.toStringAsFixed(2)} | ${y.toStringAsFixed(2)}");
  }
}

double getY(double x) {
  return 3 * x + 2;
}
