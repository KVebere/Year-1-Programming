import 'dart:io';

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

void burgerOrder() {
  print('Enter the price of a burger:');
  double burgerPrice = double.parse(stdin.readLineSync()!);

  print('Enter the amount of money you have:');
  double userMoney = double.parse(stdin.readLineSync()!);

  int numberOfBurgers = howManyBurgers(burgerPrice, userMoney);
  displayBurgerOrder(numberOfBurgers, burgerPrice);
}

void main() {
  burgerOrder();
}