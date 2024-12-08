def combine_files(file_list, output_file):
    files_info = sorted(
        ((file, len(lines := open(file, 'r' , encoding='utf-8').readline()), lines) for file in file_list),
        key = lambda x: x[1]
    )
    with open(output_file, 'w', encoding = 'utf-8') as output:
        for file_name , line_count, lines in files_info:
            output.write(f'{file_name}\n{line_count}\n')
            output.writelines(lines)

combine_files([r'C:\Users\XXX\Desktop\Files\1.txt', r'C:\Users\XXX\Desktop\Files\2.txt', r'C:\Users\XXX\Desktop\Files\3.txt'], r'C:\Users\XXX\Desktop\Files\result.txt')
