# auto-package
When dealing with big data, you can't hold all data in memory before sending somewhere. This package will automatically send itself when full and free memory.  

# usage

```python
from auto_package import AutoPackage

package_size = 10000

def send_package(package):
    # code to send the package

auto_package = AutoPackage(send_package=send_package, size=package_size)

for i in range(1000000):
    auto_package.add(i)

# if you haven't filled the package, you need to send it manunally
auto_package.send()
```

# parameters
Sometimes you want to pass some parameters to the function.  
The best solution is creating a class to hold these values.  

```python
from auto_package import AutoPackage

package_size = 10000

class Sender():
    def __init__(self, arg1, agr2):
        self.arg1 = arg1
        self.arg2 = arg2

    def send_package(self, package):
        # code to send the package

sender = Sender(arg1, arg2)

auto_package = AutoPackage(send_package=sender.send_package, size=package_size)

for i in range(1000000):
    auto_package.add(i)

# if you haven't filled the package, you need to send it manunally
auto_package.send()
```
