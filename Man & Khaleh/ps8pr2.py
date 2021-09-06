#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month=init_month
        self.day=init_day
        self.year=init_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####
    
#3
    def advance_one(self):
        """Using conditional loops all possibilties have been accounted for"""
        if self.month in [1,3,5,7,8,10] and self.day is 31:
            self.month+=1
            self.day=1
            self.year+=1
        elif self.month is 12 and self.day is 31:
            self.month=1
            self.day=1
            self.year+=1
        elif self.month in [4,6,9,11] and self.day is 30:
            self.month+=1
            self.day=1
            self.year+=1
        elif self.month is 2 and self.is_leap_year() is True and self.day is 28:
            self.day=29
        elif self.month is 2 and self.day is 29:
            self.month+=1
            self.day=1
            self.year+=1          
        elif self.month is 2 and self.is_leap_year() is False and self.day is 28:
            self.month+=1
            self.day=1
            self.year+=1
        else:
            self.day+=1

#4
    def advance_n(self, n):
        
        
            
            
        
                        
        
    
