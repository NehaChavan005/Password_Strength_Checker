import re
class password:

    def c_passwd_s(self,passwd):
         
         if len(passwd) < 8:
             return "❌Weak: Password must be atleast 8 characters"
         
         if not re.search(r'\d',passwd):          #if not re.search(char.isdigit() for char in passwd):
             return "❌Weak: Password must contain a digit(0-9)"
         
         if not re.search(r'\w',passwd):
             return "❌Weak: Password must contain a character"
         
         if not re.search(r'[A-Z]',passwd):
             return "❌Weak: Password must contain a Uppercase character(A-Z)"
         
         if not re.search(r'[a-z]',passwd):
             return "❌Weak: Password must contain a Lowercase character(a-z)"
         
         if not re.search(r'[!@#$%^&*]',passwd):
             return "❌Weak: Password must contain a Special characters(!@#$%^&*)"
         
         else:
             return "✔️Strong Password"
         
    def strength_score(self, passwd):
        rules = [
            r'.{8,}',
            r'\d',
            r'\w',
            r'[A-Z]',
            r'[a-z]',
            r'[!@#$%^&*]'
        ]
        score = sum(1 for rule in rules if re.search(rule, passwd))
        return score, len(rules)