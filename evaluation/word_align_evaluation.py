import csv

#file_name is name of csv file
def create_aligned_matrix(file_name, num_eng_words, top_n):
    with open(file_name, 'r') as csvFile:
        csvreader = csv.reader(csvFile, delimiter = ' ')
        #row_count = sum(1 for row in csvreader) # number of rows in csv file
        matrix = []
        line_count = 1
        my_list = []
        for row in csvreader:
            vals = row[0].split("\t")
            if(line_count <= (num_eng_words * top_n)): # and line_count <= row_count  
                if line_count % top_n == 1:
                    my_list.append(vals[0])  # english word
                    my_list.append(vals[1])  # first translated word
                else:
                    my_list.append(vals[1])  # just translated word
                    if (line_count/top_n).is_integer():
                        matrix.append(my_list)
                        my_list = []
                line_count += 1
        return matrix


def get_user_input(matrix):
    for row in matrix:
        print("Please evaluate the following translations for '" + row[0] + "': " + ', '.join(row[1:]))
        user_input = input('''
        (a) At least one translation is correct, regardless of exceptions.
        (b) All translations are incorrect but have no exceptions.
        (c) Exceptions or uncertainties (e.g. punctuation, misc character, close translations etc)
        ''')
        lower_user_input = user_input.lower()
        if lower_user_input != "a" and lower_user_input != "b" and lower_user_input != "c" and lower_user_input != "d":
            print("Value not accepted. Please try again.")
            get_user_input(matrix)
        else:
            row.append(user_input)
        if lower_user_input == "a":
            correct_values = input("Which translations (1-5) are correct? Separate inputs with a comma.")
            row.append(correct_values)
        elif lower_user_input == "c":
            exception_values = input("Which translations (1-5) have exceptions or uncertainties? Separate inputs with a comma.")
            row.append(exception_values)
        else:
            row.append("-")
    return matrix # with added user input values


def write_user_input(matrix, output):
    with open(output, 'wt', encoding='utf-8') as output_file:
        output_writer = csv.writer(output_file, delimiter='\t')
        for row in matrix:
            output_writer.writerow(row)
    output_file.close()


def get_accuracy_rate(matrix):
    correct_count = 0
    for row in matrix:
        if(row[6] == "a"):
            correct_count += 1
    accuracy_percent = correct_count/len(matrix)*100
    return accuracy_percent


def write_accuracy_rate(matrix):
    acc = str(get_accuracy_rate(matrix)) + "%"
    with open('word-align-eval.csv', 'a', encoding='utf-8') as output_file:
        output_writer = csv.writer(output_file, delimiter='\t')
        output_writer.writerow(["accuracy percentage: ", acc])
    output_file.close()

if __name__ == '__main__':
    mat = get_user_input(create_aligned_matrix("../align_models/word-align.csv", 50, 5))
    write_user_input(mat, "word-align-eval.csv")
    write_accuracy_rate(mat)
