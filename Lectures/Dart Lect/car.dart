// class Car {
//   String colour = '';
//   double speed = 0.0;

// // Shorter version of the constructor
//   Car(this.colour, this.speed);

//   // Car(String colour, double speed) {
//   //   this.colour = colour;
//   //   this.speed = speed;
//   // }

//   void accelerate(double inc) {
//     speed += inc;
//   }

//   void brake() {
//     speed = 0;
//   }

//   String toString() {
//     return 'Car(colour: $colour, speed: $speed)';
//   }
// }

class BankAccount {
  String owner;
  double _balance = 0.0;

  BankAccount(this.owner);

    void deposit(double amount) => _balance += amount;

  void withdraw(double amount) {
    if (_balance - amount >= 0) {
      _balance -= amount;
    }
  }

  double getBalance() => _balance;
}


