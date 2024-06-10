import 'dart:io';

void basicCalculator(int a, int b, String operation) {
  switch (operation) {
    case 'sum':
      print('Result: ${a + b}');
      break;
    case 'subtract':
      print('Result: ${a - b}');
      break;
    case 'multiply':
      print('Result: ${a * b}');
      break;
    case 'divide':
      if (b != 0) {
        print('Result: ${a / b}');
      } else {
        print('Error: Division by zero');
      }
      break;
    default:
      print('Error: Unknown operation');
  }
}

void main(List<String> arguments) {
  if (arguments.length != 3) {
    print('Usage: dart calculator.dart <operation> <num1> <num2>');
    exit(1);
  }

  int a = int.parse(arguments[1]);
  int b = int.parse(arguments[2]);
  String operation = arguments[0];
  basicCalculator(a, b, operation);
}
