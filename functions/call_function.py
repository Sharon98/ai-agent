def call_function(function_call_part, verbose=False):
    """
    Calls a function based on the provided function call part.

    Args:
        function_call_part (dict): The part of the function call to execute.
        verbose (bool): If True, prints additional information.

    Returns:
        The result of the function call.
    """
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Calling function: {function_call_part.name}")

    # Extract the function name and arguments
    function_name = function_call_part.name
    arguments = function_call_part.args

    arguments["working_directory"] = "./calculator"
    # Call the function dynamically
    #if hasattr(functions, function_name):
    #    func = getattr(functions, function_name)    
    #function_name(**arguments)            
    # else:


    raise ValueError(f"Function '{function_name}' not found in functions module.")