class Tristate(object):
    def __init__(self, value=None):
       if any(value is v for v in (True, False, None)):
          self.value = value
       else:
           raise ValueError("Tristate value must be True, False, or None")

    def __eq__(self, other):
       if not type(self)==type(other): 
          raise TypeError("eq_ implicit conversion to Tristate not supported!")
       return self.value is other
 

#  def __lt__(self, other):
#         raise TypeError("Tristate value are not ordered and are incomparable")

    def __cmp__(self, other):
         raise TypeError("Tristate value are not ordered and are incomparable")


    def __ne__(self, other):
         if not type(self)==type(other): 
          raise TypeError("ne: implicit conversion to Tristate not supported!")
       return  not self.__eq__(other)

    def __nonzero__(self):   # Python 3: __bool__()
       raise TypeError("nonzero: Tristate value may not be used as implicit Boolean")

    def __bool__(self):   # Python 3: __bool__()
       raise TypeError("bool: Tristate value may not be used as implicit Boolean")

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return "Tristate(%s)" % self.value

