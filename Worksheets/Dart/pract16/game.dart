import 'dart:io';
import 'dart:math';

void main() {
  Random random = new Random();
  int randomNumber = random.nextInt(100) + 1;
  int userGuess;

  print('I\'m thinking of a number between 1 and 100.');
  print('Can you guess what it is?');

  do {
    print('Enter your guess:');
    userGuess = int.parse(stdin.readLineSync() ?? '');

    if (userGuess < randomNumber) {
      print('Too low!');
    } else if (userGuess > randomNumber) {
      print('Too high!');
    }
  } while (userGuess != randomNumber);

  print('Congratulations! You guessed it!');
}
