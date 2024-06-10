import 'dart:math';
import 'dart:io';

void main() {
  // print(calculateArea(5, 7));

  // int radius = 5;
  // double area = calculateCircleArea(radius);
  // print("The area of a circle with radius $radius is $area");

  // int number = 5;
  // int result = multiplyBy2(number);
  // print("The result is $result");

  // multiLingualGreeting('en');
  // multiLingualGreeting('es');
  // multiLingualGreeting('da');

  // double x = 10;
  // double result = customLog(x, base: 10);
  // print("The logarithm of $x with base 10 is $result");
  // result = customLog(x);
  // print("The natural logarithm of $x is $result");

  // getBoolFromUser();

  // exceptionHandlingDemo();

  // print("The factorial of 5 is ${factorial(5)}");

  // int size = getSize1(); // Try `getSize2()` and `getSize3()`
  // print("The size is $size");

  isPrime(18);
}

void calculateAge(String name, int birthYear) {
  int currentYear = DateTime.now().year;
  int age = currentYear - birthYear;

  print("Hello, $name! You are $age years old.");
}

int calculateArea(int side1, int side2) {
  return side1 * side2;
}

// The same function, but using named parameters
// side1 is required, side2 has a default value of 1
// int calculateArea({required int side1, int side2 = 1}) {
//   return side1 * side2;
// }

// This time, side2 is nullable
// int calculateArea({required int side1, int? side2}) {
//   return side1 * (side2 ?? 1);
// }

// The same function, but using the arrow syntax
// side1 is positional, side2 is named and has a default value of 1
// int calculateArea(int side1, {int side2 = 1}) => side1 * side2;

// This function is imported in `main.dart`.
void birthdayMessage(String name, int age) {
  print("Happy birthday, $name! You're $age years old!");
}

double calculateCircleArea(double radius) {
  return pi * pow(radius, 2);
}

int multiplyBy2(int x) {
  return x * 2;
}

// The same function, but using the arrow syntax
// int multiplyBy2(int x) => x * 2;

void multiLingualGreeting(String language) {
  switch (language) {
    case 'en-gb' || 'en-us':
      print('Hello, world!');
    case 'es':
      print('¡Hola Mundo!');
    case 'fr':
      print('Bonjour le monde!');
    default:
      print('Unknown language');
      print('Please try again');
  }
}

// The same function, but using the switch statement
// void multiLingualGreeting(String language) {
//   switch (language) {
//     case 'en-gb' || 'en-us':
//       print('Hello, world!');
//     case 'es':
//       print('¡Hola Mundo!');
//     case 'fr':
//       print('Bonjour le monde!');
//     default:
//       print('Unknown language');
//       print('Please try again');
//   }
// }

double customLog(double x, {double? base}) {
  switch (base) {
    case null:
      return log(x);
    default:
      return log(x) / log(base);
  }
}

void getBoolFromUser() {
  print('Enter a boolean value:');
  String input = stdin.readLineSync()!;
  bool? isTrue = bool.tryParse(input);
  switch (isTrue) {
    case true:
      print('It is true');
    case false:
      print('It is false');
    // Without the default case, the compiler would complain
    // that the switch statement doesn't cover all cases
    default:
      print('It is not a boolean value');
  }
}

void exceptionHandlingDemo() {
  try {
    var numbers = [1, 2, 3];
    print('The fourth number is ${numbers[3]}');
  } on RangeError {
    print('Caught a RangeError!');
  } catch (e) {
    print('An unknown error occurred: $e');
  } finally {
    print('This line will always be executed');
  }
}

// int factorial(int n) {
//   int result = 1;
//   for (int i = 1; i <= n; i++) {
//     result = result * i;
//   }
//   return result;
// }

int factorial(int n) {
  int result = 1;
  int i = 1;
  while (i <= n) {
    result = result * i;
    i++;
  }
  return result;
}

int getSize1() {
  int size = 0;
  while (size != 5 && size != 7 && size != 9) {
    print("Enter a size (5, 7 or 9):");
    String? input = stdin.readLineSync();
    size = int.parse(input!);
  }
  return size;
}

int getSize2() {
  int size = 0;
  while (size != 5 && size != 7 && size != 9) {
    print("Enter a size (5, 7 or 9):");
    String? input = stdin.readLineSync();
    if (input == null) {
      print("That was not a valid input.");
      continue;
    }
    size = int.parse(input);
  }
  return size;
}

int getSize3() {
  int? size = null;
  while (true) {
    print("Enter a size (5, 7 or 9):");
    String? input = stdin.readLineSync();
    if (input == null) {
      print("That was not a valid input.");
      continue;
    }
    size = int.tryParse(input);
    if (size == null) {
      print("Your input was not a number.");
      continue;
    } else if (size != 5 && size != 7 && size != 9) {
      print("Your number must be 5, 7 or 9.");
      continue;
    } else {
      print("You have selected $size.");
      break;
    }
  }
  return size;
}

int maxNumbers1(int a, int b) {
  if (a > b) {
    return a;
  } else {
    return b;
  }
}

int maxNumbers2(int a, int b) {
  return max(a, b);
}

int daysInMonth(int month) {
  switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      return 31;
    case 4:
    case 6:
    case 9:
    case 11:
      return 30;
    case 2:
      return 28;
    default:
      return 0;
  }
}

int daysInMonth2(int month) {
  if (month == 1 ||
      month == 3 ||
      month == 5 ||
      month == 7 ||
      month == 8 ||
      month == 10 ||
      month == 12) {
    return 31;
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    return 30;
  } else if (month == 2) {
    return 28;
  } else {
    return 0;
  }
}

int multiply2(int x) => x * 2;

void speedCalculator(double distance, double time) => distance / time;

void heartMonitor(int age, int heartRate) {
  if (age <= 20 && heartRate > 170) {
    print("High heart rate for 0-20!");
  } else if (age >= 21 && age <= 40 && heartRate > 155) {
    print("High heart rate for 21-40!");
  } else if (age >= 41 && age >= 60 && heartRate > 140) {
    print("High heart rate for 41-60!");
  } else if (age >= 61 && age <= 80 && heartRate > 130) {
    print("High heart rate for 61-80!");
  } else if (age >= 81 && heartRate > 100) {
    print("High heart rate for 81-100!");
  } else {
    print("Normal heart rate!");
  }
}

void basicCalculator(int a, int b, String operation) {
  switch (operation) {
    case '+':
      print(a + b);
      break;
    case '-':
      print(a - b);
      break;
    case '*':
      print(a * b);
      break;
    case '/':
      print(a / b);
      break;
    default:
      print("Invalid operation");
  }
}

void isPrime(int n) {
  if (n <= 1) {
    print("Not a prime number");
    return;
  }
  for (int i = 2; i <= sqrt(n); i++) {
    if (n % i == 0) {
      print("Not a prime number");
      return;
    }
  }
  print("Prime number");
}

void gcd(int a, int b) {
  while (a != b) {
    if (a > b) {
      a -= b;
    } else {
      b -= a;
    }
  }
  print("The GCD is $a");
}

void customizedGreeting() {
  print("Enter Time:");
  double time = double.parse(stdin.readLineSync()!);
  if (time >= 0 && time < 12) {
    print("Good Morning");
  } else if (time >= 12 && time < 16) {
    print("Good Afternoon");
  } else if (time >= 16 && time < 20) {
    print("Good Evening");
  } else if (time >= 20 && time < 24) {
    print("Good Night");
  } else {
    print("Invalid Time");
  }
}
