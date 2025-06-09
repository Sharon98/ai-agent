from functions.get_files_info import get_files_info

def info_tests():
    results = get_files_info("calculator", ".") 
    print(results)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)



if __name__ == "__main__":
    info_tests()