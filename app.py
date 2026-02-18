import streamlit as st

st.set_page_config(layout="wide")
st.title("📘 C++ OOP Quick Revision")

qa = {

"Q1. Define Object Oriented Programming (OOP). Explain its main features with example.": """
Definition

Object Oriented Programming (OOP) is a programming paradigm in which programs are designed using objects instead of functions and procedures.

An object represents a real-world entity and contains:

- Data (variables)

- Functions (methods)

OOP helps in organizing complex programs in a structured and secure way.

**Example of real-world modeling:**

A Student has:

Data → Roll number, Name

Behaviour → Display details

In C++:
```cpp
class Student {

   int roll;
    
   public:

   void display(){

      cout<<"Student Details";

   }

};
```
Main Features of OOP

**1. Encapsulation**

Encapsulation means wrapping data and functions into a single unit called a class.

It protects data from direct access by making it private.

Example:
```cpp
class Account {

   private:

      int balance;

   public:

      void setBalance(int b){

         balance = b;

      }

};
```
Here, balance cannot be accessed directly from outside the class.

This improves data security.

**2. Abstraction**

Abstraction means hiding internal implementation details and showing only essential features.

Example:

When we call:

obj.display();

we don’t know how the function works internally.

Example:
```cpp
class Car {

public:

   void start(){

      cout<<"Car Started";

   }

};
```
User only calls start() without knowing engine logic.

**3. Inheritance**

Inheritance allows one class to acquire properties and behaviour of another class.

It supports code reusability.

Example:
```cpp
class Animal {

public:

   void eat(){

      cout<<"Eating";

   }

};

class Dog : public Animal {

};
```
Here, Dog can use eat() function.

**4. Polymorphism**

Polymorphism means one function behaving differently in different situations.

Example:
```cpp
int add(int a,int b){

   return a+b;

}

float add(float a,float b){

   return a+b;

}
```
Same function name → Different behavior.

**Main Features of OOP**

| Feature        | Description                                      |
|---------------|--------------------------------------------------|
| Encapsulation | Wrapping data and functions into a single unit   |
| Abstraction   | Hiding internal implementation details           |
| Inheritance   | One class acquiring properties of another class  |
| Polymorphism  | One function behaving differently in situations  |


**Conclusion**

**OOP provides:**

- Better security

- Code reusability

- Easy maintenance

- Real-world problem solving

It makes programming structured and efficient.
""",

"Q2. Differentiate between Procedural Programming and Object Oriented Programming with example.": """

Programming languages are broadly classified into:

- Procedural Programming (POP)

  Procedural Programming focuses on functions and follows a step-by-step method to solve a problem.

- Object Oriented Programming (OOP)
   
 Object Oriented Programming focuses on objects that combine data and functions together.

**Difference Between POP and OOP**

| Procedural Programming (POP) | Object Oriented Programming (OOP) |
|------------------------------|-----------------------------------|
| Focuses on functions         | Focuses on objects                |
| Uses Top-Down approach       | Uses Bottom-Up approach           |
| Data is globally shared      | Data is hidden                    |
| No concept of inheritance    | Supports inheritance              |
| Less secure                  | More secure                       |
| Difficult to modify large programs | Easy to maintain           |
| Example: C                   | Example: C++                      |

Example

Procedural Programming Example (C-style)
```cpp
int add(int a, int b){

   return a+b;

}

int main(){

   int result = add(5,3);

   cout<<result;

}
```
Here, program is divided into functions.

**Object Oriented Programming Example**
```cpp
class Calculator {

public:

   int add(int a, int b){

      return a+b;

   }

};

int main(){

   Calculator obj;

   cout<<obj.add(5,3);

}
```
Here, program is organized using class and object.

**Conclusion**

- Procedural Programming is suitable for small programs.

- Object Oriented Programming is suitable for large and complex programs because it provides:

- Security

- Reusability

- Maintainability
""",

"Q3. Explain Encapsulation and Abstraction with example.": """
Encapsulation and Abstraction are two important features of Object Oriented Programming that help in making programs secure and easy to manage.

**Encapsulation**

Encapsulation means wrapping data and functions together into a single unit called a class.

It also protects data by restricting direct access from outside the class.

Data is kept private and accessed using public functions.

**Example of Encapsulation**
```cpp
class Account {

private:

   int balance;

public:

   void setBalance(int b){

      balance = b;

   }

   void showBalance(){

      cout << balance;

   }

};
```
Here:

balance is private → cannot be accessed directly

It can only be accessed using setBalance() and showBalance()

This protects data from misuse.

**Abstraction**

Abstraction means hiding internal working details and showing only necessary features to the user.

User only interacts with what is required.

**Example of Abstraction**
```cpp
class Car {

public:

   void start(){

      cout << "Car Started";

   }

};
```
**User only calls:**

obj.start();

User does not know how engine works internally.

Complexity is hidden.

- Encapsulation protects data,

- Abstraction simplifies usage.

**Encapsulation vs Abstraction**

| Encapsulation        | Abstraction         |
|----------------------|---------------------|
| Hides data           | Hides implementation|
| Uses access specifiers | Uses functions    |
| Focus on security    | Focus on simplicity |

""",

"Q4. What is Namespace? Explain its need with example.": """
A namespace in C++ is used to organize code and avoid naming conflicts.

In large programs, different libraries or parts of code may use the same variable or function name. Namespace helps prevent confusion by grouping identifiers under a unique name.

**Example Without Namespace**
```cpp
int display(){

   return 1;

}

int display(){

   return 2;

}
```
This creates an error because names are same.

**Example With Namespace**
```cpp
namespace A {

   int display(){

      return 1;

   }

}

namespace B {

   int display(){

      return 2;

   }

}

int main(){

   cout << A::display();

   cout << B::display();

}
```
**Namespace helps in:**

- Avoiding name conflicts

- Organizing large programs

- Improving code readability
""",

"Q5 . Define Class and Object with example.": """
**Definition of Class**

A class is a user-defined data type that acts as a blueprint for creating objects.

It contains:

- Data members (variables)

- Member functions (functions)

Class does not occupy memory.

**Definition of Object**

An object is an instance of a class.

It represents a real-world entity and occupies memory.

Objects are used to access class members.
```cpp
class Car {

public:

   int speed;

   void show(){

      cout << "Speed = " << speed;

   }

};
```
**Creating Object**
```cpp
int main(){

   Car c1;

   c1.speed = 80;

   c1.show();

}
```
**Conclusion**

- Class defines structure.

- Object brings it to real use.
""",

"Q6. Explain Access Specifiers in C++ with example.": """
Access specifiers control the visibility and accessibility of class members.

There are three types:

1. Private

2. Public

3. Protected

**1. Private**

- Accessible only inside the class

- Cannot be accessed from outside

- Used for data security.

**2. Public**

- Accessible anywhere in the program

- Used to provide access to private data

**3. Protected**

- Accessible inside class

- Accessible in derived class

- Not accessible from main()

- Used in inheritance.
```cpp
class A {

private:

   int x;

public:

   int y;

protected:

   int z;

};
```

**Access Specifiers control the visibility and accessibility of class members.**

| Access Specifier | Accessibility                          | Purpose              |
|------------------|----------------------------------------|----------------------|
| Private          | Accessible only inside the class       | Data security        |
| Public           | Accessible anywhere in the program     | Provide access       |
| Protected        | Accessible in class & derived class    | Used in inheritance  |

Access specifiers help in:

- Data protection

- Controlled access

- Secure programming
""",

"Q7. What is a Constructor? Explain its types with example.": """

**Definition:**

A constructor is a special member function of a class used to initialize objects.

It has the same name as the class and is automatically called when an object is created.

**Constructor has:**

- No return type

- Same name as class

Types of Constructors

**1. Default Constructor**

It takes no arguments.

Example:

```cpp
class A {

public:

   A(){

      cout << "Default Constructor";

   }

};

```
**2. Parameterized Constructor**

It takes arguments to initialize values.

Example:

```cpp
class A {

public:

   int x;

   A(int a){

      x = a;

   }

};
```

**3. Copy Constructor**

It copies values from one object to another.

Example:

```cpp
class A {

public:

   int x;

   A(int a){

      x = a;

   }

   A(A &obj){

      x = obj.x;

   }

};
```
**Constructors are used to:**

- Initialize objects

- Save coding time

- Improve efficiency
""",

"Q8. What is a Destructor? Explain with example.": """

**Definition**

A destructor is a special member function used to destroy an object and release resources when the object goes out of scope.

It has:

- Same name as the class

- Prefixed with a tilde (~)

- No return type

- No arguments

**Destructor is used to:**

- Free memory

- Close files

- Release resources

**Example**

```cpp
class A {

public:

   ~A(){

      cout << "Object Destroyed";

   }

};

int main(){

   A obj;

}
```
**Constructor → Creates object**

**Destructor → Destroys object**
""",

"Q9. Explain Static Data Members and Static Member Functions with example.": """

**Static Data Member**

- A static data member is shared by all objects of a class.

- Only one copy exists, no matter how many objects are created.

Example

**Static Data Member**

```cpp
class A {

public:

   static int count;

};

int A::count = 0;

int main(){

   A obj1, obj2;

   obj1.count++;

   obj2.count++;

   cout << A::count;

}
```

**Static Member Function**

- A static member function can access only static data members.

**Static Member Function**

```cpp
class A {

public:

   static int x;

   static void show(){

      cout << x;

   }

};

int A::x = 10;

int main(){

   A::show();

}
```

**Static members help in:**

- Memory saving

- Sharing data among objects
""",

"Q10. Explain Dynamic Memory Allocation in C++ with example.": """
Dynamic Memory Allocation means allocating memory during runtime instead of compile time.

In C++, dynamically allocated memory is created in heap memory, while normal variables and objects are created in stack memory.

**In C++, it is done using:**

- new → to allocate memory

- delete → to free memory

**Stack vs Heap**

**Stack Memory**

- Used for normal variables and objects

- Automatically created and destroyed

- No need to delete manually
**Example:**

- Demo obj;   // stored in stack

**This object is automatically removed when it goes out of scope.**

**Heap Memory**

- Used for dynamic allocation

- Created using new

- Must be removed using delete

**Operators Used**

- new → Allocates memory from heap

- delete → Releases memory back to heap

**Example (Normal Object - Stack)**

- Demo obj;   // stored in stack

**No need to delete — it is automatically destroyed.**

**Example (Dynamic Object - Heap)**

```cpp
#include <iostream>
using namespace std;

class Demo {
public:
    void show() {
        cout << "Dynamic Object" << endl;
    }
};

int main() {

    Demo *obj;
    obj = new Demo();   // stored in heap

    obj->show();

    delete obj;         // must delete manually

    return 0;
}

```
**Explanation**

- Stack objects are automatically removed

- Heap objects remain until explicitly deleted

- If delete is not used → memory leak occurs

**Key Idea**

- Normal objects in stack are removed automatically,
- But dynamically created objects in heap must be deleted manually.

**In short, dynamic memory allocation uses heap memory and requires manual deletion, unlike stack memory which is managed automatically.**
""",

"Q11. Explain Reference Variable in C++ with example.": """

- A reference variable is an alias (another name) for an existing variable.

- It does not store a separate value. it simply refers to an already existing variable.

- Both the reference and the original variable share the same memory location.

**Syntax**

- datatype &reference_name = original_variable;

**Example**
```cpp

#include <iostream>
using namespace std;

int main() {

    int x = 10;
    int &y = x;   // y is reference to x

    cout << "x = " << x << endl;
    cout << "y = " << y << endl;

    y = 20;   // changing reference

    cout << "x = " << x << endl;
    cout << "y = " << y << endl;

    return 0;
}
```
**Output**
```cpp
x = 10
y = 10
x = 20
y = 20
```
**Explanation**

- Here, y is a reference to x.

- So when y is changed, x is also updated because both refer to the same memory location.

**Key Points**

- A reference must be initialized when declared.

- It cannot refer to another variable later.

- It does not occupy separate memory.
""",

"Q12. Explain Function Overloading with example.": """

Function overloading means using the same function name to perform different tasks by changing the parameter list.

Multiple functions can have the same name if their parameters are different.

**Example**

```cpp
#include <iostream>
using namespace std;

class Demo {
public:

    int add(int a, int b) {
        return a + b;
    }

    float add(float a, float b) {
        return a + b;
    }

    int add(int a, int b, int c) {
        return a + b + c;
    }
};

int main() {
    Demo obj;

    cout << obj.add(2,3) << endl;        // calls int version
    cout << obj.add(2.5f,3.5f) << endl;  // calls float version
    cout << obj.add(1,2,3) << endl;      // calls 3-parameter version
}
```
**Output**
```cpp
5
6
6
```
**Explanation**

**All functions have the same name add, but differ in:**

- Number of parameters

- Type of parameters

- The compiler selects the correct function based on the arguments passed.

**This is called compile-time polymorphism.**

**Note:** Return type may differ in overloaded functions, but it is not considered for function overloading — the parameter list must be different.
""",

"Q13. Explain Inline Function.": """

**DEFINITION**

Inline function is a function defined using the `inline` keyword.

The compiler replaces the function call with the actual function body during compilation.

This avoids function call overhead and improves execution speed for small functions.

---

**SYNTAX**

```cpp
inline return_type function_name(parameters){

   // function body

}
```

```cpp
#include<iostream>
using namespace std;

inline int square(int x){

   return x*x;

}

int main(){

   cout << square(5);

}

```
It improves speed for small functions.
""",

"Q14. Differentiate between Macro and Inline Function.": """

**Macro vs Inline Function**

| Macro                     | Inline Function        |
|---------------------------|------------------------|
| Uses #define              | Uses inline            |
| Preprocessor handles      | Compiler handles       |
| No type checking          | Type safe              |
| Text replacement          | Function replacement   |
| No concept of scope       | Follows function scope |

**Example**

**1. Macro**

```cpp
#define SQR(x) x*x

int main(){

   int a = 5;

   cout << SQR(a);

}
```
**2. Inline Function**

```cpp
inline int sqr(int x){

   return x*x;

}

int main(){

   cout << sqr(5);

}

```
""",

"Q15 Explain Friend Function.": """
**DEFINITION**

A friend function is a non-member function that is allowed to access the private and protected members of a class.

Normally, private data cannot be accessed outside the class, but a friend function can access it.

---

**SYNTAX**

Friend function is declared inside the class using the keyword `friend`.

```cpp
class ClassName {

   friend return_type function_name(parameters);

};
```

```cpp
#include<iostream>
using namespace std;

class A {

   private:
      int x = 5;

   public:
      friend void show(A obj);

};

void show(A obj){

   cout << obj.x;

}

int main(){

   A obj;

   show(obj);

}
```
""",
"Q16. What is Array of Objects? Explain with example.":"""

- An array of objects is a collection of objects of the same class stored together.

- Instead of creating separate objects, we can create multiple objects using an array.

- Each object in the array can store different data but belongs to the same class.

**Example**

```cpp
#include <iostream>
using namespace std;

class Student {
public:
    int id;

    void setData(int i) {
        id = i;
    }

    void showData() {
        cout << "ID = " << id << endl;
    }
};

int main() {

    Student s[3];   // array of objects

    for(int i=0; i<3; i++) {
        s[i].setData(i+1);
    }

    for(int i=0; i<3; i++) {
        s[i].showData();
    }

    return 0;
}
```
- Here, three objects of class Student are created using an array, and each object stores its own data.

""",

"Q17. Explain the Program Structure of C++.": """

- A C++ program is organized into different sections to make the program easy to understand and manage.

- The basic structure of a C++ program includes the following parts:

**1. Documentation Section**

- This section contains comments that describe the program.

**Example:**
```cpp

// Program to display Hello

```
**2. Link Section**

- This section includes header files required for the program.

**Example:**

```cpp
#include <iostream>
```
**3. Definition Section**

- This section defines symbolic constants or namespaces.

**Example:**

```cpp

using namespace std;

```
**4. Global Declaration Section**

- Global variables and function declarations are written here.

**Example:**

```cpp
int x;

```
**5. Class Declaration Section**

**In C++, a class is divided into two parts:**

- Data Members → store data

- Member Functions → perform operations on data

- Member functions can be written in two ways:

**Inside the class (Inline):**

```cpp
class Demo {
public:
    void show() {
        cout << "Hello";
    }
};
```
**Outside the class using Scope Resolution Operator:**

```cpp

class Demo {
public:
    void show();
};

void Demo::show() {
    cout << "Hello";
}

```
**6. main() Function Section**

- This is the starting point of the program.
- Execution begins from here.

**Example:**

```cpp

int main() {
    Demo obj;
    obj.show();
    return 0;
}

```
- Thus, a C++ program follows a structured format where classes contain data members and member functions defined either inside or outside the class.

"""

}


left, right = st.columns([1,2])

if "selected" not in st.session_state:
    st.session_state.selected = None

with left:
    st.subheader("Questions")
    for q in qa:
        if st.button(q):
            st.session_state.selected = q

with right:
    st.subheader("Answer")
    if st.session_state.selected:
        st.write(f"### {st.session_state.selected}")
        st.markdown(qa[st.session_state.selected])
    else:
        st.info("Click any question to view the answer.")
st.markdown("---")
st.markdown("<p style='text-align:center'><b>App Created by Dr. Priyang Bhatt</b></p>", unsafe_allow_html=True)

