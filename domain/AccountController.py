class AccountController:
    @staticmethod
    def averageAge(persons: List[Person]) -> float:
        total_age = sum(person.age for person in persons)
        return total_age / len(persons) if persons else 0

all_persons = [s1, s2, s3, s4, s5, s6] 
average_age = AccountController.averageAge(all_persons)
print(f"The average age is: {average_age}")