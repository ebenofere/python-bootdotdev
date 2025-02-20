Python doesn't have to be your first language, but I think it's the best first language for most developers. It gets out of your way so you can focus on learning fundamental programming concepts.

But just because Python is simple doesn't mean it's not useful! Python is an extremely popular language in the industry, and is well-known for:
-	Backend web servers
-	DevOps and cloud engineering
-	Machine learning
-	Scripting and automation
-	etc...
On the other hand, it's not particularly well-known for front-end development. While it's possible to do so, Python isn't typically used to build user interfaces.

"Syntax" is jargon for "valid code that the computer can understand". It’s the rules for how expressions and statements should be structured in a language.

Syntax errors aren't the only kind of problems you can run into when coding, for example:
-	A bug in your logic. Your code is valid, and will run, but it does something unexpected.
-	It's too slow. Your code is valid and does what's expected, but it does it slowly

You wouldn't deploy code to end users without testing... right? So don't submit code without running it first!

Variables
Variables are how we store data as our program runs.
Variables should be descriptive and consist of a single "token", meaning continuous text with underscores separating the words.
Variables are called "variables" because they can hold any value and that value can change (it varies).

Python is dynamically typed, which means a variable can store any type, and that type can change.

In almost all circumstances, it's a bad idea to change the type of a variable. The "proper" thing to do is to just create a new one.

Languages that aren't dynamically typed are statically typed, such as Go. In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash the program.

When working with strings the + operator performs a "concatenation", which is a fancy word that means "joining two strings". Generally speaking, it's better to use string interpolation with f-strings over + concatenation.



Printing vs. Returning
Some new developers get hung up on the difference between print() and return.

It can be particularly confusing when the test suite we provide simply prints the output of your functions to the console. It makes it seem like print() and return are interchangeable, but they are not!

print() is a function that:
-	Prints a value to the console
-	Does not return a value

return is a keyword that:
-	Ends the current function's execution
-	Provides a value (or values) back to the caller of the function
-   Does not print anything to the console (unless the return value is later print()ed)



Printing to Debug Your Code
Printing values and running your code is a great way to debug your code. You can see what values are stored in various variables, find your mistakes, and fix them. Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.
In the real world it's rare to leave print() statements in your code when you're done debugging. 

Code executes in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after the definition.



Order of Functions
All functions must be defined before they're used.
You might think this would make structuring Python code hard because the order of the functions needs to be just right. As it turns out, there's a simple trick that makes it super easy.
Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function last. That way, all of the functions have been read by the Python interpreter before the first one is called.

When you write Python code, functions do not need to be defined in the specific order that they are called. What does matter is that a function is defined somewhere in your program before it is executed.

Why do we often define all functions first?
Because this practice prevents any possibility of functions being undefined when they're called! It’s a convention that keeps things clean and reliable.



It's totally normal to look stuff up online as you work. It's not cheating. It's impossible to memorize everything, and it's frankly just not necessary, even as a professional developer. Second, sometimes you just need a human. 

When no return value is specified in a function, it will automatically return None. For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value.

Parameters vs Arguments
Parameters are the names used for inputs when defining a function. Arguments are the values of the inputs supplied when a function is called.

