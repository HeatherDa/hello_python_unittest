# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

    def __init__(self, id, make, model):
        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None


    def assign(self, employee_id):
        self.employee_id = employee_id


    def is_assigned(self):
        return self.employee_id is not None


    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []


    def add_employee(self, employee):
        #  raise exception if two employees with same ID are added
        for em in self.employees:
            if em.id==employee.id:
                raise PhoneError('An employee with this ID has already been added to this list')

        if employee in self.employees:
            raise PhoneError('This employee has already been added')
        else:
            self.employees.append(employee)


    def add_phone(self, phone):
        # raise exception if two phones with same ID are added
        for p in self.phones:
            if p.id==phone.id:
                raise PhoneError ("This phone's id is already in use.")
        if phone in self.phones:
            print(phone,'\t:\t',self.phones)
            raise PhoneError('This phone has already been added')
        else:
            self.phones.append(phone)

    def assign(self, phone_id, employee):
        # Find phone in phones list
        # if phone is already assigned to an employee, do not change list, raise exception
        # if employee already has a phone, do not change list, and raise exception
        # if employee already has this phone, don't make any changes. This should NOT raise an exception.

        for phone in self.phones:
            if phone.id == phone_id:
                if (phone.is_assigned() == True) : #(this phone is assigned)
                    if PhoneAssignments.phone_info(self,employee) is None: #no phone assigned to this employee, so this phone isn't assigned to them
                        raise PhoneError ('This phone is already assigned to someone else.')
                    elif (PhoneAssignments.phone_info(self,employee) is not None) & (PhoneAssignments.phone_info(self,employee).id != phone_id): #employee has a phone other than this one assigned
                        raise PhoneError ('This employee already has a phone.')
                    else: #this employee already has this phone assigned, so do nothing
                        return
                elif (PhoneAssignments.phone_info(self,employee) is not None) & (PhoneAssignments.phone_info(self,employee) != phone_id): #this phone isn't assigned to someone else, but this employee already has a phone
                    raise PhoneError('This employee already has a phone assigned to them.')
                else: #This phone isn't assigned to someone else, and this employee doesn't have a phone.
                    phone.assign(employee.id)
                return


    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)   # Assign to None


    def phone_info(self, employee):
        # find phone for employee in phones list
        #   should return None if the employee does not have a phone
        #   the method should raise an exception if the employee does not exist
        count=0
        if employee not in self.employees:
            raise PhoneError('This employee has not been added yet.')
        else:
            for phone in self.phones:
                if phone.employee_id == employee.id: #should tell me if this phone is assigned to this employee
                    return phone
            return None #phone wasn't assigned to this employee, but the employee exists


class PhoneError(Exception):
    pass
