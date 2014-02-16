'''
Created on Feb 16, 2014

@author: jbarker
'''
def findPayment(loan, r, m):
    """assumes loan and r are floats, m an int, returns monthly
    payment for a loan of principal size loan at monthly rate of r for
    m months"""
    return loan*((r*(1+r)**m/((1+r)**m)-1))
class Mortgage(object):
    """ abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
        """ create a new loan"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #description of loan
    def makePayment(self):
        """make a pyament"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    def getTotalPaid(self):
        """ return the total paid so far"""
        return sum(self.paid)
    def __str__(self):
        return self.legend
    
findPayment(32000,6.99,120)
    