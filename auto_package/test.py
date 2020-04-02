import time

from auto_package import AutoPackage

big_list_of_items = [i for i in range(10000000)]

package_size = 10000

def send_package(package):
    print(f'I am "sending" {package_size} items')
    time.sleep(0.01)
    print('Items sent')

auto_package = AutoPackage(send_package=send_package, size=package_size)

for i in big_list_of_items:
    auto_package.add(i)

auto_package.send()
