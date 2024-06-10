//Most of the operators in Dart are identical to the ones we have already studied in Python: +, -, *, /, % (addition, subtraction, multiplication, division, and modulus). Note that Dart uses ~/ for integer division. Dart has the shorthands ++ and -- to increment and decrement a numeric variable by 1. It also includes compound assignments +=, -=, *=, /=, %=, ~/=.

// Editor
//     print(true && false);
//     print(true || false);
//     print(!true);

// We use && for logical AND, || for OR, and ! for NOT. You will find that this syntax is similar to other languages within the family of C language.

// Editor
// void multiLingualGreeting(String language) {
//   if (language == 'en') {
//     print('Hello, world!');
//   } else if (language == 'es') {
//     print('Hola, mundo!');
//   } else if (language == 'fr') {
//     print('Bonjour, monde!');
//   } else {
//     print('Unknown language');
//     print('Please try again');
//   }
// }

// Note how the syntax differs from Python, with the use of parentheses and curly braces. Try calling the function from main with different argument values.
// switch statement
// switch statements provide a more compact and readable form for handling multiple conditions based on a single variable. 
// Below, we have rewritten the multiLingualGreeting  function above using a switch statement:
// Editor
// void multiLingualGreeting(String language) {
//   switch (language) {
//     case 'en':
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

// for loops
// We’ve already seen for loops in Python. In Dart, the three parts of a loop, initialisation, condition, and update are all enclosed in parentheses and separated by semicolons.
// The factorial function below calculates the factorial of a given number n. It does this by multiplying result by every integer from 1 to n in a for loop. Add it to pract16.dart and test if it returns the factorial of 5 as 120 (recall that 5!= 12345).
// Editor
// int factorial(int n) {
//   int result = 1;
//   for (int i = 1; i <= n; i++) {
//     result = result * i;
//   }
//   return result;
// }

// We also have for-in loops in Dart, but we will see examples of this when we cover collections. 
// while loops
// Similar to Python, while loops allow for repeated execution based on a condition, that might not be known beforehand. 
// Here is a familiar use case. Add the getSize function below to pract16.dart:
// Editor
// int getSize() {
//   int size = 0;
//   while (size != 5 && size != 7 && size != 9) {
//     print("Enter a size (5, 7 or 9):");
//     String? input = stdin.readLineSync();
//     size = int.parse(input!);
//   }
//   return size;
// }

// ~/ integer division
// / regular division
// ++ (increment by 1)
// -- (decrement by 1)
// sin()
// cos()
// pi()

// The indexOf method returns the index of the first
// occurrence of a given code unit.
//
// List<String> customers = [
//   'Ştefan',
//   'Amy',
//   'Jamila',
//   'Amy',
// ];
// print(customers); // [Ştefan, Amy, Jamila, Amy]
// print(customers[2]); // Jamila
// print(customers[4]); // RangeError
//
// List<List<String>> foodDiary = [
// ['🧇', '🧆', '🥗'], // Monday
// ['🍳', '🍛'], // Tuesday
// ['🥯', '🥘', '🥪'], // Wednesday
// ['🍩', '🌯', '🍲'], // Thursday
// ['🧇', '🌮', '🍣'], // Friday
// ['🥞', '🥧', '🍔', '🍟'], // Saturday
// ['🍪', '🥪', '🍝'] // Sunday
//
// Set<String> modules = {
// 'Programming',
// 'Networks',
// 'Core Computing'
// };
// print(modules.length); // 3

// Map<String, List<int>> marksDetailed = {
//   'Programming': [100, 80, 70, 64, 00, 52],
//   'Networks': [90, 85, 95],
//   'Core Computing': [64, 70]
// };
//
// Remember that we need the null assertion operator when using the lists or their elements:
// List<int> prog = marksDetailed['Programming']!;
// print(prog[2]); // 70
// print(marksDetailed['Networks']!.last); // 95
//
// We can also iterate through this Map using:
// for (String module in marksDetailed.keys) {
// print('$module marks: ${marksDetailed[module]}');
// }

// marks = {'Programming': 77, 'Networks': 90,
// 'Core Computing': 64};
// for (String module in marks.keys) {
// print(marks[module]);