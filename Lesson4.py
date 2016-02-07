class Pet:
    number_of_legs = 0

    def sleep(self):
        print "zzz"

    def count_legs(self):
        print "I have %s legs" % self.number_of_legs


class Dog(Pet):

    def bark(self):
        print "woof"

doug = Dog()
doug.number_of_legs = 4
doug.count_legs()
doug.bark()
doug.sleep()
