import 'dart:io';
import 'dart:math';

// void main() {
//   // int x = 5;
//   // int result = multiplyBy2(x);
//   // // print('Result: $result');
//   // double distance = 100;
//   // double time = 9.58;
//   // speedCalculator(distance, time);
//   // typeConversion();
//   // String greetings = getGreetings();
//   // print(greetings);
//   // birthdayMessage('Alice', 20);
//   // askForStudentNumber();
//   // circumferenceOfCircle();
//   printNumbers(10);
// }

int multiplyBy2(int number) {
  return number * 2;
}

void speedCalculator(double distance, double time) {
  double speed = distance / time;
  print('Speed: $speed');
}

void typeConversion() {
  int i = 5;
  double d = 10.65;
  print("i: $i, d: $d");

  // to integer
  int dAsInt = d.toInt(); // 10
  int dFloor = d.floor(); // 10
  int dCeil = d.ceil(); // 11
  int dRounded = d.round(); // 11
  print("dAsInt: $dAsInt, dFloor: $dFloor, dCeil: $dCeil, dRounded: $dRounded");

  // to double
  double iAsDouble = i.toDouble(); // 5.0
  print("iAsDouble: $iAsDouble");

  // to string
  String iAsString = i.toString(); // "5"
  String dAsString = d.toString(); // "10.65"
  String dAsFixed = d.toStringAsFixed(1); // "10.7"
  print("iAsString: $iAsString, dAsString: $dAsString, dAsFixed: $dAsFixed");

  // from string
  i = int.parse(iAsString); // 5
  d = double.parse(dAsString); // 10.65
  print("i: $i, d: $d");
}

String getGreetings() {
  String arabic = 'مرحبا';
  String hindi = 'नमस्ते';
  String russian = 'Привет';
  String chinese = '你好';
  String emoji = '👋';

  return '$arabic, $hindi, $russian, $chinese, $emoji';
}

void birthdayMessage(String name, int ageLastYear) {
  print("Happy " + (ageLastYear + 1).toString() + "th birthday, " + name + "!");
  print("Happy ${ageLastYear + 1}th birthday, $name!");
}

void askForStudentNumber() {
  print("What is your student number?");
  String? input = stdin.readLineSync();
  int studentNumber = int.parse(input!);
  print("Your student number is $studentNumber");
}

void circumferenceOfCircle() {
  print('Enter the radius of a circle:');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double circumference = 2 * pi * radius;
  print('Circumference: ${circumference.toStringAsFixed(2)}');
}

// void main() {
//   pizzaOrder();
// }

// String getPizzaType() {
//   print('What type of pizza do you want?');
//   String? input = stdin.readLineSync();
//   return input!;
// }

// int getPizzaSize() {
//   print('Enter the diameter of the pizza:');
//   String? input = stdin.readLineSync();
//   return int.parse(input!);
// }

// double getPizzaPrice(int radius) {
//   double pricePerSquareInch = 0.05;
//   double area = pi * pow(radius / 2, 2);
//   return area * pricePerSquareInch;
// }

// void pizzaOrder() {
//   String pizzaType = getPizzaType();
//   int pizzaSize = getPizzaSize();
//   double pizzaPrice = getPizzaPrice(pizzaSize);
//   print('A $pizzaSize inch £$pizzaType pizza '
//       'costs £${pizzaPrice.toStringAsFixed(2)}');
// }

void printNumbers(int n) {
  for (int i = 1; i <= n; i++) {
    stdout.write("$i ");
  }
}

void main() {
  // String name = sayName("Keita");
  // String details = studentDetails();
  // print("$name\n$details");
  // double pounds = eurosToPounds(20);
  // print("£20 is €$pounds");
  // double celsius = fahrenheitToCelsius(100);
  // print("100°F is $celsius°C");
  // infoOfTheCircle();
  // displayBurgerOrder(3, 5.89);
  // print(howManyBurgers(5.89, 20.0));
  print(hypotenuseOfTriangle(3, 4));
}

String sayName(String name) {
  return "My name is $name";
}

String studentDetails() {
  return "My student number is 2202994\nMy email address is: up2202994@myport.ac.uk";
}

double eurosToPounds(double euros) {
  return euros * 0.86;
}

double fahrenheitToCelsius(double fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

double areaOfCircle(double radius) {
  return pi * pow(radius, 2);
}

double calculateCircumference(double radius) {
  return 2 * pi * radius;
}

void infoOfTheCircle() {
print("Enter the radius of the circle:");
String? input = stdin.readLineSync();
double radius = double.parse(input!);
double area = areaOfCircle(radius);
double circumference = calculateCircumference(radius);
print("The area of the circle is $area");
print("The circumference of the circle is $circumference");
}

void displayBurgerOrder(int numberOfBurgers, double pricePerBurger) {
  double totalCost = numberOfBurgers * pricePerBurger;
  print('🍔' * numberOfBurgers);
  print('Order: $numberOfBurgers burgers');
  print('Price per burger: \$${pricePerBurger.toStringAsFixed(2)}');
  print('Total cost: \$${totalCost.toStringAsFixed(2)}');
}

int howManyBurgers(double burgerPrice, double userMoney) {
  return (userMoney / burgerPrice).floor();
}


double hypotenuseOfTriangle(double side1, double side2) {
  return sqrt(pow(side1, 2) + pow(side2, 2));
}

