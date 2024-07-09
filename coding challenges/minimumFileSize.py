import math

def convert_size_to_readable(size_bytes):
    """
    Convert the size in bytes to a human-readable format (e.g., GB, MB, KB).

    Parameters:
        size_bytes (int): Size in bytes.

    Returns:
        str: Readable size string with appropriate units.
    """
    if size_bytes < 1024:
        return "{0} bytes".format(size_bytes)
    elif size_bytes < 1024 ** 2:
        return "{0:.0f} KB".format(size_bytes / 1024)
    elif size_bytes < 1024 ** 3:
        return "{0:.0f} MB".format(size_bytes / (1024 ** 2))
    else:
        return "{0:.0f} GB".format(size_bytes / (1024 ** 3))

def calculate_minimum_file_size(vocabulary_size, target_accuracy_range, average_token_size):
    """
    Calculate the minimum file size of text data needed to achieve context accuracy
    when training a Language Model (LLM).

    Parameters:
        vocabulary_size (int): The size of the vocabulary used in the Language Model.
        target_accuracy_range (tuple): The range of target accuracy from 0 to 1 (e.g., (0.8, 0.9)).
        average_token_size (float): The average size of a token in bytes.

    Returns:
        str: Readable minimum file size with appropriate units.
    """
    # Convert the target accuracy range to perplexity range
    perplexity_range = tuple(math.exp(-math.log(accuracy)) for accuracy in target_accuracy_range)
    
    # Calculate the minimum number of tokens needed
    min_tokens = vocabulary_size * (math.log(vocabulary_size) + sum(perplexity_range)) * average_token_size
    
    return convert_size_to_readable(min_tokens)

# Example parameters
vocabulary_size = 10000            # Example vocabulary size
target_accuracy_range = (0.01, 0.1)  # Example target accuracy range (lower is better)
average_token_size = 8             # Example average token size in bytes (assuming UTF-8 encoding)

# Calculate the minimum file size
min_file_size = calculate_minimum_file_size(vocabulary_size, target_accuracy_range, average_token_size)
print("Minimum file size needed:", min_file_size)
