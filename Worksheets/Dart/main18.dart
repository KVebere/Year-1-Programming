import 'Pract18.dart';

void main() {
  // Student devki = Student('Devki', '07123456789');
  // print(devki.name);
  // print(devki.level);
  // print(devki.phoneNumber); // gets the last 4 digits
  // devki.phoneNumber = ''; // should not set
  // print(devki.phoneNumber); // gets the last 4 digits
  // devki.phoneNumber = '0787654321'; // sets the phone number
  // print(devki.phoneNumber); // gets the last 4 digits

  // Module programming = Module('Programming', credits: 40);
  // Module databases = Module('Databases');
  // Course computing = Course('Computing');
  // computing.addModule(programming);
  // computing.addModule(databases);
  // print(computing);

  Shape square = Shape(1, 1);
  Circle circle = Circle(2, 2, 3);
  print("Square's x: ${square.x}, y: ${square.y}");
  print("Circle's x: ${circle.x}, y: ${circle.y}, radius: ${circle.radius}");
  square.move(2, 2);
  print("Square's x: ${square.x}, y: ${square.y}");
  circle.move(3, 3);
  print("Circle's x: ${circle.x}, y: ${circle.y}, radius: ${circle.radius}");
}
