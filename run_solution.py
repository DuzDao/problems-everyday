import time
import os
import importlib.util
import inspect


def get_latest_solution_file():
    """Get the most recently modified Python file in the src directory."""
    src_dir = os.path.join(os.path.dirname(__file__), "src")
    py_files = [f for f in os.listdir(src_dir) if f.endswith('.py')]
    
    if not py_files:
        raise FileNotFoundError("No Python files found in src folder")
    
    # Find most recently modified file
    latest_file = max(py_files, key=lambda f: os.path.getmtime(os.path.join(src_dir, f)))
    return os.path.join(src_dir, latest_file)

def load_solution_class(file_path):
    """Dynamically import the Solution class from the given file."""
    file_name = os.path.basename(file_path)
    module_name = os.path.splitext(file_name)[0]
    
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    if not hasattr(module, 'Solution'):
        raise ImportError(f"No Solution class found in {file_path}")
    
    return module.Solution

def get_solution_method(solution_instance):
    """Get the first method in the Solution class that is not a built-in method."""
    methods = inspect.getmembers(solution_instance, predicate=inspect.ismethod)
    
    # Filter out built-in methods (those starting with __)
    user_methods = [method for name, method in methods if not name.startswith('__')]
    
    if not user_methods:
        raise AttributeError("No user-defined methods found in Solution class")
    
    return user_methods[0]

def get_method_signature(method):
    """Get the parameter names of the method."""
    sig = inspect.signature(method)
    # Skip 'self' parameter
    params = list(sig.parameters.keys())
    return params

def prompt_for_input(param_name, param_type_hint=None):
    """Prompt the user for input based on parameter name and type hint."""
    type_str = f" ({param_type_hint})" if param_type_hint else ""
    user_input = input(f"Enter value for {param_name}{type_str}: ")
    
    # Try to convert input to the expected type
    if param_type_hint:
        try:
            # Handle common type hints like List[int], etc.
            if hasattr(param_type_hint, "__origin__") and param_type_hint.__origin__ is list:
                inner_type = param_type_hint.__args__[0]
                # Parse list from string input (assuming format like [1,2,3] or 1,2,3)
                clean_input = user_input.strip('[]')
                if clean_input:
                    return [inner_type(item.strip()) for item in clean_input.split(',')]
                return []
            else:
                return param_type_hint(user_input)
        except (ValueError, TypeError):
            print(f"Warning: Could not convert input to {param_type_hint}, using as string")
    
    return user_input

def run_latest_solution():
    """Run the latest Solution from the src directory."""
    try:
        latest_file = get_latest_solution_file()
        print(f"Running solution from: {latest_file}")
        
        # Load the Solution class
        SolutionClass = load_solution_class(latest_file)
        solution = SolutionClass()
        
        # Get the solution method
        solution_method = get_method_signature(get_solution_method(solution))
        method_name = get_solution_method(solution).__name__
        
        # Get method annotations for type hints
        method_annotations = get_solution_method(solution).__annotations__
        
        # Collect inputs for each parameter
        args = []
        for param in solution_method:
            type_hint = method_annotations.get(param, None)
            arg_value = prompt_for_input(param, type_hint)
            args.append(arg_value)
        
        # Call the solution method with the collected arguments
        start_time = time.time()
        result = getattr(solution, method_name)(*args)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.6f} seconds")
        
        print("\nResult:")
        print(result)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_latest_solution()