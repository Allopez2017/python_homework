# Task 1
def hello():
	return 'Hello!'

# Task 2
def greet(name):
	return 'Hello, ' + name + '!'

# Task 3
def calc(a, b, calculate='multiply'):
    try:
        match calculate:
            case 'add':
                    return a + b
            case 'subtract':
                    return a - b
            case 'multiply':
                    return a * b
            case 'divide':
                    return a / b
            case 'power':
                    return a ** b
            case 'modulo':
                    return a % b
            case 'int_divide':
                    return a // b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#Task 4
def data_type_conversion(value, data_type):
    try:
      if data_type == 'float':
            return float(value)
      elif data_type == 'int':
            return int(value)
      else:
            return str(value)
    except (ValueError, TypeError):
            return f"You can't convert {value} into a {data_type}."
    
#Task 5
def grade(*args):
    if not all(isinstance(x, (int)) for x in args):
        return "Invalid data was provided."
    average = sum(args)/len(args)
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
#except typerror

#Task 6
def repeat(string, count):
    output = ''
    for i in range(count):
        output += string
    return output

#Task 7
def student_scores(score, **kwargs):
    if score == 'best':
        best_student_score = max(kwargs, key=kwargs.get)
        return best_student_score
    elif score == 'mean':
        average_student_score = sum(kwargs.values()) / len(kwargs)
        return average_student_score
    else:
        return "Invalid score type"
     
#Task 8
def titleize(string):
    words = string.split()
    lower_words = {'a', 'on', 'an', 'the', 'of', 'and', 'is', 'in'}
    for index, word in enumerate(words):
        if index == 0 or index == len(words) -1:
            words[index] = word.capitalize()
        elif word.lower() not in lower_words:
            words[index] = word.capitalize()
        else:
            words[index] = word.lower()
    return ' '.join(words)

#Task 9
def hangman(secret, guess):
    output = ''
    for letter in secret:
        if letter in guess:
            output += letter
        else:
            output += '_'
    return output

#Task 10
#def pig_latin(word):
    #special_characters = 'aeiou'
   # if word.startswith('qu'):
    #    return word[2:] + 'quay'
    #else:
     #   if word.startswith('squ'):
      #      return word[3:] + word[0] + 'quay'
       # if word[0] in special_characters:
        #    return word + 'ay'
        #else:
         #   for i in range(len(word)):
          #      if word[i] in special_characters:
           #         return word[i:] + word[:i] + 'ay'

#def pig_latin(word):
 #   vowels = 'aeiou'
  #  if word[:2] == 'qu':
   #     return word[2:] + 'quay'
    #if word[0] in vowels:
     #   return word + 'ay'
    #for i in range(len(word)):
     #   if word[i] in vowels:
      #      return word[i:] + word[:i] + 'ay'
    
def pig_latin(sentence):
    def convert_word(word):
        vowels = "aeiou"
        if word[:2] == 'qu':
            return word[2:] + 'quay'
        if word.startswith('squ'):
            return word[3:] + word[0] + 'quay'
        if word[0] in vowels:
            return word + 'ay'
        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'
    words = sentence.split()
    pig_latin_words = [convert_word(word) for word in words]
    return ' '.join(pig_latin_words)   
    


