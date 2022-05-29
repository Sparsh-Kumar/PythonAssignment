
# Name: Susan Roberts
# Assignment: Week-4
# CMIS 102-6383
# Date: 02/07/2022
# Note - We can also break the given code into seperate modules by just writing seperate classes in seperate files and importing / exporting them.
#      - Also avoided the use of Global variables as using Global variables is not a good practice.

from abc import ABC, abstractmethod

# Service Abstract Class.
# All variables and methods defined in this class are available to child classes.
class Service ( ABC ):
	def __init__ (self, customerAge: int) -> None:
		self.customerAge = customerAge
		self.SENIOR_CITIZEN_AGE = 40 # Setting the SENIOR CITIZEN AGE into abstract parent class, would be available in all child classes.
	def isSeniorCitizen (self) -> bool: # A Common Method to check if a citizen belonging to the category of Senior Citizen.
		return self.customerAge >= self.SENIOR_CITIZEN_AGE
	@abstractmethod
	def calculateDiscount (self) -> float: # Abstract method as all child classes which belong to Service class must have calculateDiscount method.
		pass;
	@abstractmethod
	def getCost (self) -> float: # Abstract method as all child classes which belong to Service class must have a getCost method.
		pass;
	def __del__ (self) -> None: # Destructor
		pass;

# Cleaning Service is a type of Service
class CleaningService ( Service ):
	def __init__ (self, customerAge: int, numberOfRooms: int, fullCleaning: bool) -> None:
		Service.__init__ (self, customerAge) # Calling the constructor of the Parent Class.
		self.numberOfRooms = numberOfRooms
		self.fullCleaning = fullCleaning # If full cleaning, then cost is higher else cost is lower.
		if fullCleaning:
			self.costOfCleaningOneRoom = 20 # In Dollars
		else:
			self.costOfCleaningOneRoom = 10 # In Dollars
		self.seniorCitizenDiscountOnCleaning = 2 # (Percentage) Discount available on Cleaning Service for Senior Citizen is 2 %.
	def calculateDiscount (self) -> float:
		totalDiscount = self.getDiscountBasedOnHouseRooms()
		if self.isSeniorCitizen():
			totalDiscount = totalDiscount + self.seniorCitizenDiscountOnCleaning
		return totalDiscount
	def getDiscountBasedOnHouseRooms (self) -> float:
		discount = 0
		if self.numberOfRooms in range (3, 8): # If House Rooms Count lie b/w 3 to 7, discount is 1 %.
			discount = 1 # In percentage
		elif self.numberOfRooms in range (8, 14): # If House Rooms Count lie b/w 8 to 13, discount is 1.5 %
			discount = 1.5 # In percentage
		elif self.numberOfRooms > 13: # If House Rooms Count are more than 13, discount is 2.5 %
			discount = 2.5 # In percentage
		return discount
	def getCost (self) -> float:
		totalDiscount = self.calculateDiscount() # Getting total calculated discount.
		totalCost = self.costOfCleaningOneRoom * self.numberOfRooms;
		return ((100 - totalDiscount)/100) * totalCost # TotalCost - (totalDiscount/100 * TotalCost)
	def __del__ (self) -> None:
		pass;

# Yard Service is a type of Service
class YardService ( Service ):
	def __init__ (self, customerAge: int, yardLength: int, yardWidth: int, yardService: str = None, numberOfShrubs: int = 0) -> None:
		Service.__init__ (self, customerAge) # Calling the constructor of the Parent Class.
		self.yardLength = yardLength # In Foot
		self.yardWidth = yardWidth # In Foot
		self.yardService = yardService # String value (1, 2 or 3)
		self.numberOfShrubs = numberOfShrubs
		self.costOfMowing = 10 # In Dollars
		self.costOfEdging = 20 # In Dollars
		self.costOfPruning = 20 # In Dollars
		self.seniorCitizenDiscountOnYardService = 3 # (Percentage) Discount available on Yard Service for Senior Citizen is 3 %.
	def calculateDiscount (self) -> float:
		totalDiscount = 0
		if self.isSeniorCitizen():
			totalDiscount = self.seniorCitizenDiscountOnYardService
		return totalDiscount
	def calculateSquareFoot (self) -> float:
		return self.yardLength * self.yardWidth # As length and breadth are in foot, the square foot would be length * breadth.
	def calculateLinearFoot (self) -> float:
		return self.yardLength # As length is in foot, the linear foot is equal to the length of the yard.
	def getCost (self) -> float:
		totalDiscount = self.calculateDiscount() # Getting total calculated discount.
		totalCost = 0
		if self.yardService == '1':
			totalCost = self.costOfMowing * self.calculateSquareFoot()
		elif self.yardService == '2':
			totalCost = self.costOfEdging * self.calculateLinearFoot()
		elif self.yardService == '3':
			totalCost = self.costOfPruning * self.numberOfShrubs
		return ((100 - totalDiscount)/100) * totalCost # TotalCost - (totalDiscount/100 * TotalCost)
	def __del__ (self) -> None:
		pass;

def getServiceType() -> None: # Making use of Recursion to repeatedly showing the prompt to select valid Service Type.
	serviceType = input('Please Enter 1 for Cleaning Service and 2 for Yard Service.\n')
	if serviceType not in ['1', '2']:
		return getServiceType();
	return serviceType

def main():
	serviceType = getServiceType();
	serviceInstance = None
	if serviceType == '1':
		numberOfRooms = int (input('Enter the number of rooms in the house.\n'))
		cleaningType = input('Please enter 1 for Full Cleaning and 2 for Light Cleaning.\n')
		customerAge = int (input('Please enter your age.\n'))
		if cleaningType == '1':
			fullCleaning = True
		else:
			fullCleaning = False
		serviceInstance = CleaningService(customerAge, numberOfRooms, fullCleaning)
	elif serviceType == '2':
		customerAge = int (input('Please enter your age.\n'))
		yardLength = int (input('Enter the length of the yard (in ft.).\n'))
		yardWidth = int (input('Enter the width of the yard (in ft.).\n'))
		yardService = input ('Enter 1 for mowing, 2 for edging, 3 for shrub pruning.\n')
		numberOfShrubs = 0
		if yardService == '3':
			numberOfShrubs = int (input('Please enter number of shrubs for shrub pruning.\n'))
		serviceInstance = YardService(customerAge, yardLength, yardWidth, yardService, numberOfShrubs)
	serviceCost = serviceInstance.getCost()
	print (f'Your Service Cost = {serviceCost}')

if __name__ == '__main__':
	main()
