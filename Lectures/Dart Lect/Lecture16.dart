void main() {
  double gradient = 3;
  double yIntercept = -2;

  //print("y = ${gradient}x + ${yIntercept}");
  //print("${getY(x, gradient, yIntercept)} = ${gradient} * ${x} ${yIntercept}");

  print("(x, y)");

  for (double x = 45.56; x < 78.56; x += 0.1) {
    double y = getY(x, gradient, yIntercept);
    print("(${x.toStringAsFixed(2)}, ${y.toStringAsFixed(2)})");
  }
}

double getY(double x, double gradient, double yIntercept) {
  return gradient * x + yIntercept; //y = 3x + 2, x = 45.56
}
