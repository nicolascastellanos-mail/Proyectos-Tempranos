def compile(expression, label):
	def ToList(expression):
		counter = 0
		numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		simbols = ["+", "-", "*", "/", "^", "√", "(", ")", "[", "]", "{", "}"]
		listed = []
		temp = []

		while counter < len(expression):
			if expression[counter] in numbers:
				temp.append(expression[counter])
				counter += 1
			elif expression[counter] in simbols:
				if temp:
					listed.append("".join(temp))
					temp = []
				listed.append(expression[counter])
				counter += 1
			else:
				counter += 1

		if temp:
			listed.append("".join(temp))
		return listed

	def ToList_braces(expression, braces, position1, position2):
		new_expression = []
		counter = 0

		while counter < len(expression):
			if counter == position1:
				new_expression.extend(braces)
				while counter <= position2:
					counter += 1
				continue
			else:
				new_expression.append(expression[counter])
			counter += 1

		return new_expression

	def ToList_brackets(expression, brackets, position1, position2):
		new_expression = []
		counter = 0

		while counter < len(expression):
			if counter == position1:
				new_expression.extend(brackets)
				while counter <= position2:
					counter += 1
				continue
			else:
				new_expression.append(expression[counter])
			counter += 1

		return new_expression

	def ToList_parenthesis(expression, parenthesis, position1, position2):
		new_expression = []
		counter = 0

		while counter < len(expression):
			if counter == position1:
				new_expression.extend(parenthesis)
				while counter <= position2:
					counter += 1
				continue
			else:
				new_expression.append(expression[counter])
			counter += 1

		return new_expression

	def hierarchy(expression):
		def solve_braces(expression, position1, position2):
			counter = position1 + 1
			braces = []

			while counter < position2:
				braces.append(expression[counter])
				counter += 1

			braces = hierarchy(braces)
			expression = ToList_braces(expression, braces, position1, position2)

			return hierarchy(expression)

		def solve_brackets(expression, position1, position2):
			counter = position1 + 1
			brackets = []

			while counter < position2:
				brackets.append(expression[counter])
				counter += 1

			brackets = hierarchy(brackets)
			expression = ToList_brackets(expression, brackets, position1, position2)

			return hierarchy(expression)

		def solve_parenthesis(expression, position1, position2):
			counter = position1 + 1
			parenthesis = []

			while counter < position2:
				parenthesis.append(expression[counter])
				counter += 1

			parenthesis = hierarchy(parenthesis)
			expression = ToList_parenthesis(expression, parenthesis, position1, position2)

			return hierarchy(expression)

		def solve_root(expression, position):
			num1 = float(expression[position - 1])
			num2 = float(expression[position + 1])
			result =  num2 ** (1 / num1)
			new_expression = []
			counter = 0

			while counter < len(expression):
				if counter == position - 1:
					new_expression.append(str(result))
					counter += 2
				else:
					new_expression.append(expression[counter])

				counter += 1

			return new_expression

		def solve_poten(expression, position):
			num1 = float(expression[position - 1])
			num2 = float(expression[position + 1])
			result =  num1 ** num2
			new_expression = []
			counter = 0

			while counter < len(expression):
				if counter == position - 1:
					new_expression.append(str(result))
					counter += 2
				else:
					new_expression.append(expression[counter])

				counter += 1

			return new_expression

		def solve_multip(expression, position):
			num1 = float(expression[position - 1])
			num2 = float(expression[position + 1])
			result =  num1 * num2
			new_expression = []
			counter = 0

			while counter < len(expression):
				if counter == position - 1:
					new_expression.append(str(result))
					counter += 2
				else:
					new_expression.append(expression[counter])

				counter += 1

			return new_expression

		def solve_division(expression, position):
			num1 = float(expression[position - 1])
			num2 = float(expression[position + 1])
			result =  num1 / num2
			new_expression = []
			counter = 0

			while counter < len(expression):
				if counter == position - 1:
					new_expression.append(str(result))
					counter += 2
				else:
					new_expression.append(expression[counter])

				counter += 1

			return new_expression

		def solve_sum(expression, position):
			num1 = float(expression[position - 1])
			num2 = float(expression[position + 1])
			result =  num1 + num2
			new_expression = []
			counter = 0

			while counter < len(expression):
				if counter == position - 1:
					new_expression.append(str(result))
					counter += 2
				else:
					new_expression.append(expression[counter])

				counter += 1

			return new_expression

		def solve_rest(expression, position):
			num1 = float(expression[position - 1])
			num2 = float(expression[position + 1])
			result =  num1 - num2
			new_expression = []
			counter = 0

			while counter < len(expression):
				if counter == position - 1:
					new_expression.append(str(result))
					counter += 2
				else:
					new_expression.append(expression[counter])

				counter += 1

			return new_expression

		if "{" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "{":
					pos1 = counter
				elif expression[counter] == "}":
					pos2 = counter
					expression = solve_braces(expression, pos1, pos2)
					return hierarchy(expression)
				else:
					pass
				counter += 1
		
		elif "[" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "[":
					pos1 = counter
				elif expression[counter] == "]":
					pos2 = counter
					expression = solve_brackets(expression, pos1, pos2)
					return hierarchy(expression)
				else:
					pass
				counter += 1
		
		elif "(" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "(":
					pos1 = counter
				elif expression[counter] == ")":
					pos2 = counter
					expression = solve_parenthesis(expression, pos1, pos2)
					return hierarchy(expression)
				else:
					pass
				counter += 1

		elif "^" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "^":
					expression = solve_poten(expression, counter)
					return hierarchy(expression)
				counter += 1

		elif "√" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "√":
					expression = solve_root(expression, counter)
					return hierarchy(expression)
				counter += 1

		elif "*" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "*":
					expression = solve_multip(expression, counter)
					return hierarchy(expression)
				counter += 1

		elif "/" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "/":
					expression = solve_division(expression, counter)
					return hierarchy(expression)
				counter += 1

		elif "+" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "+":
					expression = solve_sum(expression, counter)
					return hierarchy(expression)
				counter += 1

		elif "-" in expression:
			counter = 0
			while counter < len(expression):
				if expression[counter] == "-":
					expression = solve_rest(expression, counter)
					return hierarchy(expression)
				counter += 1

		return expression

	listed = ToList(expression)
	result = hierarchy(listed)

	return label.config(text=result)