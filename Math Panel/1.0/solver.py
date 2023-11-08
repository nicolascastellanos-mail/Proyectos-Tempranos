def compile(expression, label):
	def list(expression):
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

		listed.append("".join(temp))
		return listed

	def hierarchy(expression):
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

		if "^" in expression:
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

	listed = list(expression)
	result = hierarchy(listed)

	return label.config(text=result)